from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from lala.domain.errors import InvalidImageError
from lala.renderers.image_io import ImageAssetValidator


def test_validator_rejects_mime_magic_mismatch(sample_image: Path) -> None:
    validator = ImageAssetValidator(max_bytes=1_000_000, max_pixels=1_000_000)
    with pytest.raises(InvalidImageError, match="MIME"):
        validator.validate(sample_image, declared_mime="image/jpeg")


def test_normalize_applies_exif_orientation_and_strips_metadata(tmp_path: Path) -> None:
    source = tmp_path / "oriented.jpg"
    image = Image.new("RGB", (2, 3), (200, 100, 50))
    exif = Image.Exif()
    exif[274] = 6
    exif[270] = "private description"
    image.save(source, exif=exif)
    destination = tmp_path / "normalized.png"
    validator = ImageAssetValidator(max_bytes=1_000_000, max_pixels=1_000_000)

    result = validator.normalize(source, destination)

    assert (result.width, result.height) == (3, 2)
    with Image.open(destination) as normalized:
        assert normalized.getexif().get(274) is None
        assert normalized.getexif().get(270) is None


def test_validator_rejects_declared_size_mismatch(sample_image: Path) -> None:
    validator = ImageAssetValidator(max_bytes=1_000_000, max_pixels=1_000_000)
    with pytest.raises(InvalidImageError, match="파일 크기"):
        validator.validate(sample_image, expected_bytes=1)
