from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

from lala.domain.models import RemasterParameters
from lala.renderers.remaster import REMASTER_ENGINE_VERSION, RemasterRenderer


def test_remaster_engine_v1_golden_pixels(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    destination = tmp_path / "result.png"
    input_pixels = np.array(
        [
            [[16, 32, 64], [96, 128, 160]],
            [[192, 208, 224], [240, 248, 255]],
        ],
        dtype=np.uint8,
    )
    expected = np.array(
        [
            [[66, 68, 90], [106, 142, 177]],
            [[205, 223, 241], [244, 244, 244]],
        ],
        dtype=np.uint8,
    )
    Image.fromarray(input_pixels, mode="RGB").save(source)
    parameters = RemasterParameters(
        brightness=12,
        contrast=7,
        highlights=-20,
        shadows=18,
        saturation=5,
        temperature=3,
        tint=-2,
        vignette=-6,
    )

    result = RemasterRenderer().render(source, destination, parameters)

    with Image.open(destination) as rendered:
        np.testing.assert_array_equal(np.asarray(rendered), expected)
    assert result.engine_version == REMASTER_ENGINE_VERSION
