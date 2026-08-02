from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

from lala.domain.models import RemasterParameters
from lala.renderers.remaster import RemasterRenderer


def test_zero_parameters_are_pixel_noop(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    destination = tmp_path / "result.png"
    array = np.arange(8 * 8 * 3, dtype=np.uint8).reshape((8, 8, 3))
    Image.fromarray(array, mode="RGB").save(source)

    RemasterRenderer().render(source, destination, RemasterParameters())

    with Image.open(destination) as result:
        output = np.asarray(result)
    np.testing.assert_array_equal(output, array)


def test_remaster_is_deterministic_and_preserves_alpha(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    first = tmp_path / "first.png"
    second = tmp_path / "second.png"
    Image.new("RGBA", (20, 10), (20, 30, 40, 77)).save(source)
    parameters = RemasterParameters(brightness=10, shadows=20, denoise=5, sharpness=6)
    renderer = RemasterRenderer()

    first_result = renderer.render(source, first, parameters)
    second_result = renderer.render(source, second, parameters)

    assert first_result.sha256 == second_result.sha256
    with Image.open(first) as output:
        assert output.mode == "RGBA"
        assert set(np.asarray(output.getchannel("A")).ravel()) == {77}


def test_positive_brightness_increases_dark_image_luminance(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    destination = tmp_path / "result.png"
    Image.new("RGB", (8, 8), (20, 20, 20)).save(source)
    RemasterRenderer().render(source, destination, RemasterParameters(brightness=20))
    with Image.open(destination) as output:
        assert np.asarray(output).mean() > 20
