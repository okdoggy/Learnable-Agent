from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image
from pydantic import BaseModel, ConfigDict, Field

from lala.renderers.image_io import sha256_file


class ImageInspection(BaseModel):
    model_config = ConfigDict(extra="forbid")

    width: int
    height: int
    mode: str
    mime: str
    sha256: str
    mean_luminance: float = Field(ge=0, le=1)
    median_luminance: float = Field(ge=0, le=1)
    shadow_fraction: float = Field(ge=0, le=1)
    highlight_fraction: float = Field(ge=0, le=1)
    black_clip_fraction: float = Field(ge=0, le=1)
    white_clip_fraction: float = Field(ge=0, le=1)
    mean_saturation: float = Field(ge=0, le=1)
    color_cast: str
    luminance_histogram: list[int]


def inspect_image(path: Path) -> ImageInspection:
    with Image.open(path) as opened:
        opened.load()
        original_mode = opened.mode
        original_width, original_height = opened.size
        sample = opened.convert("RGB")
        sample.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
        rgb = np.asarray(sample, dtype=np.float32) / 255.0
    linear = _srgb_to_linear(rgb)
    luminance = linear[..., 0] * 0.2126 + linear[..., 1] * 0.7152 + linear[..., 2] * 0.0722
    maximum = rgb.max(axis=-1)
    minimum = rgb.min(axis=-1)
    saturation = np.divide(
        maximum - minimum,
        maximum,
        out=np.zeros_like(maximum),
        where=maximum > 1e-6,
    )
    means = rgb.reshape(-1, 3).mean(axis=0)
    red_blue_delta = float(means[0] - means[2])
    green_delta = float(means[1] - (means[0] + means[2]) / 2)
    if abs(green_delta) > 0.06 and abs(green_delta) > abs(red_blue_delta):
        cast = "green" if green_delta > 0 else "magenta"
    elif abs(red_blue_delta) > 0.06:
        cast = "warm" if red_blue_delta > 0 else "cool"
    else:
        cast = "neutral"
    histogram, _ = np.histogram(luminance, bins=64, range=(0.0, 1.0))
    suffix_mime = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
    return ImageInspection(
        width=original_width,
        height=original_height,
        mode=original_mode,
        mime=suffix_mime.get(path.suffix.lower(), "image/png"),
        sha256=sha256_file(path),
        mean_luminance=float(luminance.mean()),
        median_luminance=float(np.median(luminance)),
        shadow_fraction=float((luminance < 0.12).mean()),
        highlight_fraction=float((luminance > 0.82).mean()),
        black_clip_fraction=float((luminance < 0.005).mean()),
        white_clip_fraction=float((luminance > 0.995).mean()),
        mean_saturation=float(saturation.mean()),
        color_cast=cast,
        luminance_histogram=histogram.astype(int).tolist(),
    )


def _srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)
