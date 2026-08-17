from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

from lala.domain.models import RemasterParameters, SelectiveHslAdjustment
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


def test_selective_hsl_changes_target_hue_without_changing_other_hue(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    destination = tmp_path / "result.png"
    pixels = np.array([[[160, 80, 80], [80, 80, 160]]], dtype=np.uint8)
    Image.fromarray(pixels, mode="RGB").save(source)

    RemasterRenderer().render(
        source,
        destination,
        RemasterParameters(
            hsl_selective=[
                SelectiveHslAdjustment(
                    target_hue=0,
                    hue_range=30,
                    saturation_shift=25,
                    luminance_shift=10,
                )
            ]
        ),
    )

    with Image.open(destination) as output:
        rendered = np.asarray(output)
    assert not np.array_equal(rendered[0, 0], pixels[0, 0])
    np.testing.assert_array_equal(rendered[0, 1], pixels[0, 1])


def test_channel_gain_and_gamma_apply_color_grade_without_global_haze(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    destination = tmp_path / "result.png"
    Image.new("RGB", (8, 8), (80, 80, 80)).save(source)

    RemasterRenderer().render(
        source,
        destination,
        RemasterParameters(gamma_r=1.05, gain_r=1.08, gain_b=0.92),
    )

    with Image.open(destination) as output:
        red, green, blue = np.asarray(output)[0, 0]
    assert red > green > blue


def test_sharpen_amount_increases_soft_edge_separation(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    destination = tmp_path / "result.png"
    row = np.array([40, 80, 120, 160, 200], dtype=np.uint8)
    pixels = np.repeat(row[None, :, None], repeats=3, axis=2)
    pixels = np.repeat(pixels, repeats=9, axis=0)
    Image.fromarray(pixels, mode="RGB").save(source)

    RemasterRenderer().render(source, destination, RemasterParameters(sharpen_amount=0.8))

    with Image.open(destination) as output:
        rendered = np.asarray(output)
    assert rendered[4, 1, 0] < pixels[4, 1, 0]
    assert rendered[4, -2, 0] > pixels[4, -2, 0]
