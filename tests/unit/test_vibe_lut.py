from __future__ import annotations

from pathlib import Path

from lala.domain.models import LutParameters
from lala.renderers.lut import LutCatalog


def test_vibe_lut_parameters_expose_expert_grade_controls() -> None:
    parameters = LutParameters(
        preset="warm_kodak",
        lut_intensity=0.8,
        skin_protection=True,
        grain_amount=0.2,
        halation=0.15,
        use_aces=True,
    )

    assert parameters.preset == "warm_kodak"
    assert parameters.lut_intensity == 0.8
    assert parameters.skin_protection is True
    assert parameters.grain_amount == 0.2
    assert parameters.halation == 0.15
    assert parameters.use_aces is True


def test_vibe_lut_catalog_contains_all_supported_presets() -> None:
    root = Path(__file__).resolve().parents[2]
    catalog = LutCatalog(root / "luts" / "manifest.yaml")

    assert {entry.lut_id for entry in catalog.approved_entries()} == {
        "teal_orange",
        "warm_kodak",
        "fuji_velvia",
        "matte_fade",
        "golden_hour",
        "moody_dark",
        "cold_blue",
        "vintage_analog",
        "summer_pastel",
        "cyberpunk",
        "film_noir",
        "documentary",
        "horror",
        "romance",
        "clean_modern",
        "apple_neutral",
    }
