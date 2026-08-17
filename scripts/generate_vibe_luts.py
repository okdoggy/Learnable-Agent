# ruff: noqa: E501
from __future__ import annotations

from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "luts" / "cubes"
SIZE = 33

# preset: exposure, lift, gamma, gain, saturation, contrast, black lift,
# shadow tint/strength, highlight tint/strength
PRESETS = {
    "teal_orange": (0.0, (-.02, .01, .04), (1.05, .97, .88), (1.10, 1., .82), 1.12, 0., 0., (.20, .55, .70), .12, (.90, .65, .30), .10),

    "fuji_velvia": (0.0, (-.03, -.01, -.02), (1.10, 1.08, 1.05), (1.05, 1.10, .95), 1.35, .25, 0., None, 0., None, 0.),
    "matte_fade": (0.0, (0., 0., .02), (1.02, 1.02, 1.04), (.95, .95, .98), .75, 0., .08, None, 0., None, 0.),

    "moody_dark": (-.25, (-.04, -.02, .02), (.92, .95, 1.05), (.90, .95, 1.05), .85, .35, 0., (.15, .30, .50), .15, (.85, .90, 1.), .06),
    "cold_blue": (0.0, (-.02, 0., .04), (.95, .98, 1.08), (.88, .92, 1.12), .80, .20, 0., None, 0., None, 0.),

    "summer_pastel": (.20, (.01, 0., 0.), (1.05, 1.05, 1.), (1.02, 1.02, .98), .85, 0., .04, None, 0., None, 0.),
    "cyberpunk": (0.0, (-.03, .02, .06), (.90, 1., 1.15), (1.05, .85, 1.20), 1.40, .30, 0., (.10, .30, .70), .20, (1., .40, .90), .10),
    "film_noir": (0.0, (-.04, -.04, -.02), (.95, .95, 1.02), (1., 1., 1.05), .10, .55, 0., None, 0., None, 0.),
    "documentary": (0.0, (0., 0., 0.), (1.02, 1.02, 1.), (1., 1., .98), 1.08, .18, 0., None, 0., None, 0.),
    "horror": (-.15, (-.05, -.01, -.05), (.88, 1.02, .90), (.85, 1.10, .85), .60, .40, 0., None, 0., None, 0.),
    "romance": (.10, (.02, 0., 0.), (1.05, 1., 1.), (1.08, .95, .95), .90, 0., 0., (.80, .55, .55), .08, (1., .90, .90), .10),
    "clean_modern": (0.0, (0., 0., 0.), (1.02, 1.02, 1.02), (1.02, 1.02, 1.02), 1.15, .12, 0., None, 0., None, 0.),
    "apple_neutral": (0.0, (0., 0., .015), (1., 1., 1.), (.99, 1., 1.02), .88, .05, 0., None, 0., None, 0.),
}


def grade(name: str) -> np.ndarray:
    exposure, lift, gamma, gain, saturation, contrast, black, shadow, shadow_amount, highlight, highlight_amount = PRESETS[name]
    values = np.linspace(0., 1., SIZE, dtype=np.float32)
    blue, green, red = np.meshgrid(values, values, values, indexing="ij")
    rgb = np.stack((red, green, blue), axis=-1)
    rgb = np.clip(rgb * (2**exposure) * np.asarray(gain) + np.asarray(lift), 0., 1.)
    rgb = np.power(rgb, 1 / np.asarray(gamma))
    luminance = rgb @ np.asarray((.2126, .7152, .0722), dtype=np.float32)
    if shadow is not None:
        mask = np.clip((.5 - luminance) * 2, 0., 1.)[..., None] * shadow_amount
        rgb += (np.asarray(shadow) - rgb) * mask
    if highlight is not None:
        mask = np.clip((luminance - .5) * 2, 0., 1.)[..., None] * highlight_amount
        rgb += (np.asarray(highlight) - rgb) * mask
    luminance = rgb @ np.asarray((.2126, .7152, .0722), dtype=np.float32)
    rgb = luminance[..., None] + (rgb - luminance[..., None]) * saturation
    if contrast:
        rgb = .5 + np.tanh((rgb - .5) * (1 + contrast * 2)) / 2
    if black:
        rgb = rgb * (1 - black) + black
    return np.clip(rgb, 0., 1.)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for preset in PRESETS:
        filename = "cinematic_teal_orange.cube" if preset == "teal_orange" else f"{preset}.cube"
        table = grade(preset).reshape(-1, 3)
        lines = [f'TITLE "{preset}"', "LUT_3D_SIZE 33", "DOMAIN_MIN 0.0 0.0 0.0", "DOMAIN_MAX 1.0 1.0 1.0"]
        lines.extend(" ".join(f"{value:.8f}" for value in row) for row in table)
        (OUTPUT / filename).write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
