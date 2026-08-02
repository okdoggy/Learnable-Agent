from __future__ import annotations

import hashlib
import io
import warnings
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageCms, ImageOps, UnidentifiedImageError

from lala.domain.errors import InvalidImageError, UnsupportedFormatError

SUPPORTED_FORMATS = {"JPEG": "image/jpeg", "PNG": "image/png", "WEBP": "image/webp"}
SUPPORTED_MIME = frozenset(SUPPORTED_FORMATS.values())


@dataclass(frozen=True, slots=True)
class ValidatedImage:
    path: Path
    sha256: str
    byte_size: int
    mime: str
    format: str
    width: int
    height: int
    mode: str


class ImageAssetValidator:
    def __init__(self, *, max_bytes: int, max_pixels: int) -> None:
        self.max_bytes = max_bytes
        self.max_pixels = max_pixels

    def validate(
        self,
        path: Path,
        *,
        declared_mime: str | None = None,
        expected_sha256: str | None = None,
        expected_bytes: int | None = None,
    ) -> ValidatedImage:
        resolved = path.resolve()
        try:
            byte_size = resolved.stat().st_size
        except OSError as exc:
            raise InvalidImageError("이미지 파일을 읽을 수 없습니다.") from exc
        if byte_size <= 0 or byte_size > self.max_bytes:
            raise InvalidImageError("이미지 파일 크기가 허용 범위를 벗어났습니다.")
        if expected_bytes is not None and byte_size != expected_bytes:
            raise InvalidImageError("신고된 파일 크기와 실제 파일 크기가 다릅니다.")
        digest = sha256_file(resolved)
        if expected_sha256 and digest.lower() != expected_sha256.lower():
            raise InvalidImageError("이미지 SHA-256이 업로드 요청과 일치하지 않습니다.")
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error", Image.DecompressionBombWarning)
                with Image.open(resolved) as image:
                    image_format = image.format or ""
                    width, height = image.size
                    mode = image.mode
                    if image_format not in SUPPORTED_FORMATS:
                        raise UnsupportedFormatError()
                    if width <= 0 or height <= 0 or width * height > self.max_pixels:
                        raise InvalidImageError("이미지 해상도가 허용 범위를 벗어났습니다.")
                    image.verify()
        except UnsupportedFormatError:
            raise
        except (Image.DecompressionBombError, Image.DecompressionBombWarning) as exc:
            raise InvalidImageError("압축 폭탄 가능성이 있는 이미지입니다.") from exc
        except (UnidentifiedImageError, OSError, SyntaxError, ValueError) as exc:
            raise InvalidImageError() from exc
        detected_mime = SUPPORTED_FORMATS[image_format]
        if declared_mime and declared_mime.lower() != detected_mime:
            raise InvalidImageError("MIME 형식과 이미지 매직바이트가 일치하지 않습니다.")
        return ValidatedImage(
            path=resolved,
            sha256=digest,
            byte_size=byte_size,
            mime=detected_mime,
            format=image_format,
            width=width,
            height=height,
            mode=mode,
        )

    def normalize(self, source: Path, destination: Path) -> ValidatedImage:
        self.validate(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            with Image.open(source) as opened:
                opened.load()
                image = ImageOps.exif_transpose(opened)
                image = _to_srgb(image)
                if image.mode not in {"RGB", "RGBA", "L", "LA"}:
                    image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
                image.save(destination, format="PNG", optimize=False)
        except (OSError, ValueError) as exc:
            raise InvalidImageError("이미지를 안전한 sRGB PNG로 정규화하지 못했습니다.") from exc
        return self.validate(destination, declared_mime="image/png")


def _to_srgb(image: Image.Image) -> Image.Image:
    profile_bytes = image.info.get("icc_profile")
    if not profile_bytes:
        return image.copy()
    alpha = image.getchannel("A") if "A" in image.getbands() else None
    color = image.convert("RGB")
    try:
        source_profile = ImageCms.ImageCmsProfile(io.BytesIO(profile_bytes))
        target_profile = ImageCms.createProfile("sRGB")
        converted = ImageCms.profileToProfile(
            color, source_profile, target_profile, outputMode="RGB"
        )
    except (ImageCms.PyCMSError, OSError, ValueError):
        converted = color
    if alpha is not None:
        converted.putalpha(alpha)
    return converted


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
