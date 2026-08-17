from __future__ import annotations

import base64
import binascii
import os
import shutil
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import httpx

from lala.config import Settings
from lala.domain.errors import ExecutionError, LalaError
from lala.domain.models import GenerateAIParameters
from lala.renderers.image_io import ImageAssetValidator, sha256_file
from lala.resilience import SlidingWindowLimit
from lala.storage.workspace import ensure_within

IMAGEGEN_ADAPTER_VERSION = "3.0.0"
OPENAI_IMAGES_EDIT_URL = "https://api.openai.com/v1/images/edits"
IMAGEGEN_1K_SIZES = ("1024x1024", "1536x1024", "1024x1536")


@dataclass(frozen=True, slots=True)
class ImagegenResult:
    path: Path
    sha256: str
    execution_mode: str = "openai-image-api"
    adapter_version: str = IMAGEGEN_ADAPTER_VERSION
    model: str = "gpt-image-2"
    quality: str = "low"
    size: str = "1024x1024"


class ImagegenRunner(Protocol):
    def edit(
        self, source: Path, destination: Path, parameters: GenerateAIParameters
    ) -> ImagegenResult: ...


class OpenAIImagegenRunner:
    """Edit one image through the OpenAI Image API with fixed low/1K settings."""

    def __init__(self, settings: Settings, *, client: httpx.Client | None = None) -> None:
        self.settings = settings
        self.client = client or httpx.Client()
        self.validator = ImageAssetValidator(max_bytes=50 * 1024 * 1024, max_pixels=8_294_400)
        self.quota = SlidingWindowLimit(
            limit=settings.imagegen_max_calls_per_hour,
            window_seconds=3600,
            code="IMAGEGEN_BUDGET_EXCEEDED",
            message_ko="Generate AI 시간당 실행 한도에 도달했습니다.",
        )

    def edit(
        self, source: Path, destination: Path, parameters: GenerateAIParameters
    ) -> ImagegenResult:
        if parameters.execution_mode != "openai-image-api":
            raise ExecutionError("Generate AI 실행 모드 계약이 올바르지 않습니다.", retryable=False)
        if not self.settings.imagegen_openai_api_key:
            raise ExecutionError(
                "Generate AI용 LALA_IMAGEGEN_OPENAI_API_KEY가 설정되지 않았습니다.", retryable=False
            )
        self.quota.consume("global")
        source = ensure_within(source, self.settings.var_dir / "jobs")
        destination = destination.resolve()
        output_root = (self.settings.output_dir / "imagegen").resolve()
        ensure_within(destination, output_root)
        destination.parent.mkdir(parents=True, exist_ok=True)

        size = _closest_supported_size(source)
        response = self._request_with_retries(source, parameters, size=size)
        try:
            encoded = response.json()["data"][0]["b64_json"]
            image_bytes = base64.b64decode(encoded, validate=True)
        except (KeyError, IndexError, TypeError, ValueError, binascii.Error) as exc:
            raise ExecutionError(
                "OpenAI Image API 응답에 유효한 이미지가 없습니다.", retryable=True
            ) from exc

        temporary = destination.with_name(f".{destination.stem}.api-response.png")
        temporary.unlink(missing_ok=True)
        destination.unlink(missing_ok=True)
        try:
            temporary.write_bytes(image_bytes)
            os.replace(temporary, destination)
            resolved_result = ensure_within(destination.resolve(strict=True), output_root)
            if resolved_result != destination:
                raise ExecutionError(
                    "Generate AI 결과가 안전한 일반 파일이 아닙니다.", retryable=False
                )
            actual_size = self._strip_generated_metadata(destination)
        except (OSError, LalaError) as exc:
            if isinstance(exc, ExecutionError):
                raise
            raise ExecutionError(
                "Generate AI 결과 파일을 안전하게 저장하지 못했습니다.", retryable=False
            ) from exc
        finally:
            temporary.unlink(missing_ok=True)

        return ImagegenResult(
            path=destination,
            sha256=sha256_file(destination),
            model=self.settings.imagegen_model,
            quality=self.settings.imagegen_quality,
            size=actual_size,
        )

    def _request_with_retries(
        self, source: Path, parameters: GenerateAIParameters, *, size: str
    ) -> httpx.Response:
        attempts = min(max(1, self.settings.imagegen_max_attempts), 5)
        prompt = _build_api_prompt(parameters)
        for attempt in range(attempts):
            try:
                response = self.client.post(
                    OPENAI_IMAGES_EDIT_URL,
                    headers={"Authorization": f"Bearer {self.settings.imagegen_openai_api_key}"},
                    data={
                        "model": self.settings.imagegen_model,
                        "prompt": prompt,
                        "quality": self.settings.imagegen_quality,
                        "size": size,
                        "output_format": "png",
                    },
                    files={
                        "image[]": (
                            source.name,
                            source.read_bytes(),
                            _image_media_type(source),
                        )
                    },
                    timeout=self.settings.imagegen_timeout_seconds,
                )
            except (httpx.TimeoutException, httpx.TransportError) as exc:
                if attempt + 1 < attempts:
                    time.sleep(min(0.25 * (2**attempt), 1.0))
                    continue
                raise ExecutionError(
                    "OpenAI Image API 연결에 실패했습니다.", retryable=True
                ) from exc
            if response.is_success:
                return response
            retryable = response.status_code == 429 or response.status_code >= 500
            if retryable and attempt + 1 < attempts:
                time.sleep(min(0.25 * (2**attempt), 1.0))
                continue
            raise ExecutionError(
                "OpenAI Image API 이미지 편집에 실패했습니다.",
                retryable=retryable,
                internal=f"OpenAI Images API returned HTTP {response.status_code}",
            )
        raise ExecutionError("OpenAI Image API 이미지 편집에 실패했습니다.", retryable=True)

    def _strip_generated_metadata(self, destination: Path) -> str:
        normalized = destination.with_name(f".{destination.stem}.normalized.png")
        normalized.unlink(missing_ok=True)
        try:
            self.validator.normalize(destination, normalized)
            os.replace(normalized, destination)
            asset = self.validator.validate(destination, declared_mime="image/png")
            return f"{asset.width}x{asset.height}"
        finally:
            normalized.unlink(missing_ok=True)


class CopyingImagegenRunner:
    """Deterministic fake used only by contract tests and local dry-runs."""

    def edit(
        self, source: Path, destination: Path, parameters: GenerateAIParameters
    ) -> ImagegenResult:
        del parameters
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        return ImagegenResult(path=destination.resolve(), sha256=sha256_file(destination))


def _build_api_prompt(parameters: GenerateAIParameters) -> str:
    constraints = "; ".join(parameters.constraints) or "none"
    avoid = "; ".join(parameters.avoid) or "none"
    return "\n".join(
        [
            parameters.prompt,
            f"Use case: {parameters.use_case}",
            f"Preservation constraints: {constraints}",
            f"Avoid: {avoid}",
            "Change only what the request asks and preserve every unspecified element.",
            "Preserve the input composition and aspect ratio.",
        ]
    )


def _closest_supported_size(source: Path) -> str:
    """Choose a renderer-owned 1K size nearest to the input aspect ratio."""
    from PIL import Image

    with Image.open(source) as image:
        width, height = image.size
    source_ratio = width / height
    return min(
        IMAGEGEN_1K_SIZES,
        key=lambda size: abs(source_ratio - _aspect_ratio(size)),
    )


def _aspect_ratio(size: str) -> float:
    width, height = (int(value) for value in size.split("x"))
    return width / height


def _image_media_type(source: Path) -> str:
    suffix = source.suffix.casefold()
    return {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(suffix, "image/png")
