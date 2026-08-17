from __future__ import annotations

import io
from pathlib import Path

import pytest
from PIL import Image

from lala.config import Settings


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    (tmp_path / "config").mkdir()
    (tmp_path / "luts" / "cubes").mkdir(parents=True)
    (tmp_path / "skills" / "lala-coordinator" / "references").mkdir(parents=True)
    (tmp_path / "skills" / "lala-coordinator" / "references" / "planner-prompt.md").write_text(
        "이미지와 사용자 의도를 전체 문맥으로 판단하고 JSON 계약을 지킨다.\n",
        encoding="utf-8",
    )
    (tmp_path / "config" / "sources.yaml").write_text(
        """
schema_version: "1.0"
sources:
  - id: first
    enabled: true
    types: [official, youtube]
    domains: [example.com]
  - id: second
    enabled: true
    types: [magazine]
    domains: [another.example]
""".lstrip(),
        encoding="utf-8",
    )
    (tmp_path / "config" / "parameter-registry.yaml").write_text(
        """
schema_version: "1.0"
calibration_version: "1.0.0"
remaster_engine_version: "1.0.0"
capabilities:
  remaster:
    scope: global
    unsupported: [semantic-local-masks]
calibration:
  shadows:
    conservative_start_range: [-5, 5]
    caution: global shadow lift also raises background shadows
""".lstrip(),
        encoding="utf-8",
    )
    (tmp_path / "luts" / "manifest.yaml").write_text(
        (
            'schema_version: "1.0"\ncatalog_version: "2026-08-12"\nluts:\n'
            '  - id: documentary\n    title: Documentary\n    path: cubes/documentary.cube\n'
            '    status: approved\n'
        ),
        encoding="utf-8",
    )
    (tmp_path / "luts" / "cubes" / "documentary.cube").write_text(
        "LUT_1D_SIZE 2\n0 0 0\n1 1 1\n",
        encoding="utf-8",
    )
    result = Settings.from_env(tmp_path)
    result.ensure_directories()
    return result


@pytest.fixture
def png_bytes() -> bytes:
    stream = io.BytesIO()
    image = Image.new("RGB", (32, 24), (40, 80, 120))
    image.save(stream, format="PNG")
    return stream.getvalue()


@pytest.fixture
def sample_image(tmp_path: Path) -> Path:
    path = tmp_path / "sample.png"
    Image.new("RGB", (24, 16), (32, 64, 96)).save(path)
    return path
