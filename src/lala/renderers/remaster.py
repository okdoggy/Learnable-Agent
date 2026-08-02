from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter, ImageOps

from lala.domain.models import RemasterParameters
from lala.renderers.image_io import sha256_file

REMASTER_ENGINE_VERSION = "1.0.0"


@dataclass(frozen=True, slots=True)
class RenderResult:
    path: Path
    sha256: str
    engine_version: str
    width: int
    height: int


class RemasterRenderer:
    engine_version = REMASTER_ENGINE_VERSION

    def render(
        self, source: Path, destination: Path, parameters: RemasterParameters
    ) -> RenderResult:
        destination.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(source) as opened:
            opened.load()
            image = ImageOps.exif_transpose(opened)
            original_mode = image.mode
            alpha = image.getchannel("A") if "A" in image.getbands() else None
            rgb_image = image.convert("RGB")
            rgb = np.asarray(rgb_image, dtype=np.float32) / 255.0

        adjusted = self._tone_and_color(rgb, parameters)
        encoded = Image.fromarray(
            np.clip(np.rint(adjusted * 255.0), 0, 255).astype(np.uint8), mode="RGB"
        )
        if parameters.denoise:
            radius = 0.25 + parameters.denoise / 35.0
            blurred = encoded.filter(ImageFilter.GaussianBlur(radius=radius))
            encoded = Image.blend(encoded, blurred, parameters.denoise / 100.0)
        if parameters.sharpness:
            encoded = encoded.filter(
                ImageFilter.UnsharpMask(
                    radius=1.0 + parameters.sharpness / 100.0,
                    percent=parameters.sharpness * 2,
                    threshold=2,
                )
            )
        if original_mode in {"L", "LA"} and not any(
            (parameters.saturation, parameters.temperature, parameters.tint)
        ):
            encoded = encoded.convert("L")
        if alpha is not None:
            encoded.putalpha(alpha)
        encoded.save(destination, format="PNG", optimize=False)
        return RenderResult(
            path=destination.resolve(),
            sha256=sha256_file(destination),
            engine_version=self.engine_version,
            width=encoded.width,
            height=encoded.height,
        )

    def _tone_and_color(self, rgb: np.ndarray, parameters: RemasterParameters) -> np.ndarray:
        linear = _srgb_to_linear(rgb)

        if parameters.brightness:
            linear *= 2.0 ** (parameters.brightness / 50.0)

        if parameters.contrast:
            contrast = 2.0 ** (parameters.contrast / 60.0)
            pivot = 0.18
            linear = (linear - pivot) * contrast + pivot

        linear = np.clip(linear, 0.0, 1.0)
        luminance = _luminance(linear)
        tone_delta = np.zeros_like(luminance)
        if parameters.shadows:
            shadow_weight = np.clip((0.55 - luminance) / 0.55, 0.0, 1.0) ** 2
            tone_delta += parameters.shadows / 100.0 * 0.32 * shadow_weight
        if parameters.highlights:
            highlight_weight = np.clip((luminance - 0.35) / 0.65, 0.0, 1.0) ** 2
            tone_delta += parameters.highlights / 100.0 * 0.32 * highlight_weight
        if np.any(tone_delta):
            target_luminance = np.clip(luminance + tone_delta, 0.0, 1.0)
            darken_scale = np.divide(
                target_luminance,
                luminance,
                out=np.ones_like(luminance),
                where=luminance > 1e-5,
            )
            lift = np.maximum(target_luminance - luminance, 0.0)
            lift_fraction = np.divide(
                lift,
                1.0 - luminance,
                out=np.zeros_like(luminance),
                where=luminance < 1.0 - 1e-5,
            )
            lifted = linear + (1.0 - linear) * lift_fraction[..., None]
            linear = np.where(
                (tone_delta >= 0)[..., None],
                lifted,
                linear * darken_scale[..., None],
            )

        if parameters.saturation:
            luminance = _luminance(linear)[..., None]
            saturation = max(0.0, 1.0 + parameters.saturation / 100.0)
            linear = luminance + (linear - luminance) * saturation

        if parameters.temperature or parameters.tint:
            temperature = parameters.temperature / 100.0 * 0.12
            tint = parameters.tint / 100.0 * 0.10
            gains = np.array(
                [1.0 + temperature + tint * 0.25, 1.0 - tint, 1.0 - temperature + tint * 0.25],
                dtype=np.float32,
            )
            linear *= gains

        if parameters.vignette:
            height, width = linear.shape[:2]
            yy, xx = np.ogrid[-1.0 : 1.0 : complex(height), -1.0 : 1.0 : complex(width)]
            radius = np.sqrt(xx * xx + yy * yy) / np.sqrt(2.0)
            edge_weight = np.clip((radius - 0.2) / 0.8, 0.0, 1.0) ** 2
            gain = 1.0 + parameters.vignette / 100.0 * 0.55 * edge_weight
            linear *= gain[..., None]

        return _linear_to_srgb(np.clip(linear, 0.0, 1.0))


def _luminance(linear: np.ndarray) -> np.ndarray:
    return linear[..., 0] * 0.2126 + linear[..., 1] * 0.7152 + linear[..., 2] * 0.0722


def _srgb_to_linear(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.04045, values / 12.92, ((values + 0.055) / 1.055) ** 2.4)


def _linear_to_srgb(values: np.ndarray) -> np.ndarray:
    return np.where(values <= 0.0031308, values * 12.92, 1.055 * values ** (1 / 2.4) - 0.055)
