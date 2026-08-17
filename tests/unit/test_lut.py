from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest
import yaml
from PIL import Image

from lala.domain.errors import LalaError
from lala.domain.models import LutParameters
from lala.renderers.lut import LutCatalog, LutRenderer, apply_cube, parse_cube

IDENTITY_3D = """
TITLE "identity"
LUT_3D_SIZE 2
DOMAIN_MIN 0 0 0
DOMAIN_MAX 1 1 1
0 0 0
1 0 0
0 1 0
1 1 0
0 0 1
1 0 1
0 1 1
1 1 1
""".lstrip()

INVERT_1D = """
TITLE "invert"
LUT_1D_SIZE 2
DOMAIN_MIN 0 0 0
DOMAIN_MAX 1 1 1
1 1 1
0 0 0
""".lstrip()


def _catalog(tmp_path: Path, cube_text: str = IDENTITY_3D) -> LutCatalog:
    cubes = tmp_path / "cubes"
    cubes.mkdir(parents=True)
    cube = cubes / "identity.cube"
    cube.write_text(cube_text, encoding="utf-8")
    manifest = tmp_path / "manifest.yaml"
    manifest.write_text(
        yaml.safe_dump(
            {
                "schema_version": "1.0",
                "catalog_version": "test",
                "luts": [
                    {
                        "id": "identity",
                        "title": "Identity",
                        "path": "cubes/identity.cube",
                        "status": "approved",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return LutCatalog(manifest)


def test_identity_3d_lut_uses_trilinear_interpolation(tmp_path: Path) -> None:
    catalog = _catalog(tmp_path)
    cube = parse_cube(catalog.resolve("identity").path)
    rgb = np.array([[[0.13, 0.52, 0.91]]], dtype=np.float32)
    np.testing.assert_allclose(apply_cube(rgb, cube), rgb, atol=1e-6)


def test_one_dimensional_lut_interpolates_each_channel(tmp_path: Path) -> None:
    catalog = _catalog(tmp_path, INVERT_1D)
    cube = parse_cube(catalog.resolve("identity").path)
    rgb = np.array([[[0.1, 0.4, 0.9]]], dtype=np.float32)

    np.testing.assert_allclose(apply_cube(rgb, cube), 1.0 - rgb, atol=1e-6)


def test_lut_intensity_zero_is_pixel_noop(tmp_path: Path) -> None:
    catalog = _catalog(tmp_path)
    source = tmp_path / "source.png"
    destination = tmp_path / "result.png"
    array = np.array([[[20, 80, 160], [255, 1, 9]]], dtype=np.uint8)
    Image.fromarray(array, mode="RGB").save(source)
    LutRenderer(catalog).render(
        source,
        destination,
        LutParameters(
            preset="identity", lut_intensity=0, skin_protection=False, grain_amount=0, halation=0
        ),
    )
    with Image.open(destination) as result:
        np.testing.assert_array_equal(np.asarray(result), array)


def test_lut_intensity_one_applies_full_transform(tmp_path: Path) -> None:
    catalog = _catalog(tmp_path, INVERT_1D)
    source = tmp_path / "source.png"
    destination = tmp_path / "result.png"
    Image.new("RGB", (1, 1), (20, 80, 160)).save(source)

    LutRenderer(catalog).render(
        source,
        destination,
        LutParameters(
            preset="identity", lut_intensity=1, skin_protection=False, grain_amount=0, halation=0
        ),
    )

    with Image.open(destination) as result:
        assert tuple(np.asarray(result)[0, 0]) == (235, 175, 95)


def test_lut_rejects_nan(tmp_path: Path) -> None:
    catalog = _catalog(tmp_path, IDENTITY_3D.replace("1 1 1", "NaN 1 1"))
    with pytest.raises(LalaError, match="값"):
        parse_cube(catalog.resolve("identity").path)


def test_lut_rejects_invalid_domain(tmp_path: Path) -> None:
    invalid = IDENTITY_3D.replace("DOMAIN_MAX 1 1 1", "DOMAIN_MAX 0 1 1")
    catalog = _catalog(tmp_path, invalid)
    with pytest.raises(LalaError, match="DOMAIN_MAX"):
        parse_cube(catalog.resolve("identity").path)


def test_lut_rejects_malformed_quotes_and_extreme_values(tmp_path: Path) -> None:
    malformed = _catalog(tmp_path / "malformed", 'TITLE "unfinished\nLUT_1D_SIZE 2\n0 0 0\n1 1 1\n')
    with pytest.raises(LalaError, match="1행"):
        parse_cube(malformed.resolve("identity").path)

    extreme_text = INVERT_1D.replace("1 1 1", "1000000 1 1")
    extreme = _catalog(tmp_path / "extreme", extreme_text)
    with pytest.raises(LalaError, match="값"):
        parse_cube(extreme.resolve("identity").path)


def test_manifest_rejects_path_traversal(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.yaml"
    manifest.write_text(
        """
catalog_version: test
luts:
  - id: escape
    title: Escape
    path: ../escape.cube
    status: approved
""".lstrip(),
        encoding="utf-8",
    )
    with pytest.raises(LalaError, match="경로"):
        LutCatalog(manifest).resolve("escape")
