from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from lala.config import Settings
from lala.domain.errors import ExecutionError, LalaError
from lala.domain.models import GenerateAIParameters
from lala.renderers.image_io import ImageAssetValidator, sha256_file
from lala.resilience import SlidingWindowLimit
from lala.storage.workspace import ensure_within

IMAGEGEN_ADAPTER_VERSION = "2.1.0"


@dataclass(frozen=True, slots=True)
class ImagegenResult:
    path: Path
    sha256: str
    execution_mode: str = "codex-imagegen-builtin"
    adapter_version: str = IMAGEGEN_ADAPTER_VERSION


class ImagegenRunner(Protocol):
    def edit(
        self, source: Path, destination: Path, parameters: GenerateAIParameters
    ) -> ImagegenResult: ...


class CodexImagegenRunner:
    """Invoke Codex's built-in $imagegen skill using saved Codex authentication."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
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
        if parameters.execution_mode != "codex-imagegen-builtin":
            raise ExecutionError("Generate AI 실행 모드 계약이 올바르지 않습니다.", retryable=False)
        executable = self._resolve_codex_executable()
        self.quota.consume("global")
        source = ensure_within(source, self.settings.var_dir / "jobs")
        destination = destination.resolve()
        output_root = (self.settings.output_dir / "imagegen").resolve()
        ensure_within(destination, output_root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        prompt = _build_prompt(parameters, source, destination)
        command = [
            str(executable),
            "exec",
            "--ephemeral",
            "--sandbox",
            "workspace-write",
            "--cd",
            str(destination.parent),
            "--skip-git-repo-check",
            "--image",
            str(source.resolve()),
            "-",
        ]
        self._run_with_retries(command, prompt, destination)
        if not destination.is_file():
            raise ExecutionError("Generate AI 결과 파일이 생성되지 않았습니다.", retryable=True)
        try:
            resolved_result = ensure_within(destination.resolve(strict=True), output_root)
        except (OSError, LalaError) as exc:
            raise ExecutionError(
                "Generate AI 결과 경로가 허용된 output 디렉터리를 벗어났습니다.",
                retryable=False,
            ) from exc
        if resolved_result != destination:
            raise ExecutionError("Generate AI 결과가 안전한 일반 파일이 아닙니다.", retryable=False)
        self._strip_generated_metadata(destination)
        return ImagegenResult(path=destination, sha256=sha256_file(destination))

    def _strip_generated_metadata(self, destination: Path) -> None:
        normalized = destination.with_name(f".{destination.stem}.normalized.png")
        normalized.unlink(missing_ok=True)
        try:
            self.validator.normalize(destination, normalized)
            os.replace(normalized, destination)
            self.validator.validate(destination, declared_mime="image/png")
        finally:
            normalized.unlink(missing_ok=True)

    def _run_with_retries(
        self, command: list[str], prompt: str, destination: Path
    ) -> subprocess.CompletedProcess[str]:
        attempts = min(max(1, self.settings.imagegen_max_attempts), 5)
        last: subprocess.CompletedProcess[str] | None = None
        for attempt in range(attempts):
            destination.unlink(missing_ok=True)
            try:
                completed = subprocess.run(
                    command,
                    cwd=self.settings.project_root,
                    env=_subprocess_env(),
                    input=prompt,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="strict",
                    timeout=self.settings.imagegen_timeout_seconds,
                    check=False,
                )
            except subprocess.TimeoutExpired as exc:
                if attempt + 1 < attempts:
                    time.sleep(min(0.25 * (2**attempt), 1.0))
                    continue
                raise ExecutionError(
                    "Codex $imagegen 실행 시간이 초과되었습니다.", retryable=True
                ) from exc
            if completed.returncode == 0 and destination.is_file():
                return completed
            last = completed
            detail = (completed.stderr or completed.stdout)[-2000:]
            retryable = _is_transient_codex_failure(detail)
            if not retryable or attempt + 1 >= attempts:
                raise ExecutionError(
                    "Codex $imagegen 이미지 편집에 실패했습니다.",
                    retryable=retryable,
                    internal=f"codex exec exited {completed.returncode}: {detail}",
                )
            time.sleep(min(0.25 * (2**attempt), 1.0))
        detail = ((last.stderr or last.stdout) if last else "unknown failure")[-2000:]
        raise ExecutionError(
            "Codex $imagegen 이미지 편집에 실패했습니다.", retryable=True, internal=detail
        )

    def _resolve_codex_executable(self) -> Path:
        configured = Path(self.settings.codex_executable).expanduser()
        if configured.is_absolute() and configured.is_file():
            return configured.resolve()
        located = shutil.which(self.settings.codex_executable)
        if located:
            return Path(located).resolve()
        raise ExecutionError(
            "Codex CLI를 찾을 수 없습니다. Codex가 설치되고 로그인되어 있는지 확인해 주세요.",
            retryable=False,
        )


class CopyingImagegenRunner:
    """Deterministic fake used only by contract tests and local dry-runs."""

    def edit(
        self, source: Path, destination: Path, parameters: GenerateAIParameters
    ) -> ImagegenResult:
        del parameters
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        return ImagegenResult(path=destination.resolve(), sha256=sha256_file(destination))


def _build_prompt(parameters: GenerateAIParameters, source: Path, destination: Path) -> str:
    constraints = "; ".join(parameters.constraints) or "없음"
    avoid = "; ".join(parameters.avoid) or "없음"
    return "\n".join(
        [
            "$imagegen",
            (
                "Use the default built-in image generation tool. "
                "Do not use the fallback Image API CLI."
            ),
            f"Use case: {parameters.use_case}",
            "Asset type: 사용자 이미지 편집 결과",
            f"Input images: Image 1 ({source}) is the edit target",
            f"Primary request: {parameters.prompt}",
            f"Constraints: {constraints}",
            f"Avoid: {avoid}",
            "Change only what the primary request asks to change.",
            (
                "Repeat all preservation constraints: keep every unspecified subject, identity, "
                "pose, clothing, composition, geometry, and text unchanged."
            ),
            "Inspect the generated result and retry once only for a clear invariant violation.",
            (
                "This is a project-bound artifact. Copy the final selected PNG to this exact path: "
                f"{destination}"
            ),
            "Do not modify source code or any file other than that final PNG.",
        ]
    )


def _is_transient_codex_failure(detail: str) -> bool:
    normalized = detail.casefold()
    patterns = (
        r"\b429\b",
        r"\b5\d\d\b",
        r"rate.?limit",
        r"too many requests",
        r"timed?\s*out",
        r"timeout",
        r"connection (?:reset|refused|aborted)",
        r"temporar(?:y|ily)",
        r"service unavailable",
    )
    return any(re.search(pattern, normalized) for pattern in patterns)


def _subprocess_env() -> dict[str, str]:
    allowed = {
        "PATH",
        "HOME",
        "CODEX_HOME",
        "USER",
        "HTTPS_PROXY",
        "HTTP_PROXY",
        "NO_PROXY",
        "SSL_CERT_FILE",
        "REQUESTS_CA_BUNDLE",
        "TMPDIR",
        "LANG",
        "LC_ALL",
    }
    environment = {key: value for key, value in os.environ.items() if key in allowed}
    environment["PYTHONIOENCODING"] = "utf-8"
    environment["PYTHONUTF8"] = "1"
    return environment
