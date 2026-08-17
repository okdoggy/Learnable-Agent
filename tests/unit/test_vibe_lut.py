from __future__ import annotations

from pathlib import Path

import pytest

from lala.domain.errors import LalaError
from lala.domain.models import LutParameters
from lala.renderers.lut import LutCatalog


def test_vibe_lut_parameters_expose_expert_grade_controls() -> None:
    parameters = LutParameters(
        preset="documentary",
        lut_intensity=0.8,
        skin_protection=True,
        grain_amount=0.2,
        halation=0.15,
        use_aces=True,
    )

    assert parameters.preset == "documentary"
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
        "fuji_velvia",
        "matte_fade",
        "moody_dark",
        "cold_blue",
        "summer_pastel",
        "cyberpunk",
        "film_noir",
        "documentary",
        "horror",
        "romance",
        "clean_modern",
        "apple_neutral",
    }


@pytest.mark.parametrize("preset", ["warm_kodak", "golden_hour", "vintage_analog"])
def test_removed_vibe_lut_presets_cannot_be_resolved(preset: str) -> None:
    root = Path(__file__).resolve().parents[2]
    catalog = LutCatalog(root / "luts" / "manifest.yaml")

    with pytest.raises(LalaError, match="승인된 LUT ID"):
        catalog.resolve(preset)
