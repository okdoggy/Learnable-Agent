from __future__ import annotations

import os
import shutil
from pathlib import Path

import pytest
from PIL import Image

from lala.config import Settings
from lala.domain.models import GenerateAIParameters
from lala.renderers.imagegen import OpenAIImagegenRunner

pytestmark = pytest.mark.live


def test_openai_image_api_edit_contract(tmp_path: Path) -> None:
    if os.getenv("LALA_RUN_LIVE_IMAGEGEN") != "1":
        pytest.skip("LALA_RUN_LIVE_IMAGEGEN=1이 아닌 환경에서는 실제 API 비용을 사용하지 않습니다.")
    settings = Settings.from_env(tmp_path)
    if not settings.imagegen_openai_api_key:
        pytest.skip("OPENAI_API_KEY가 설정되지 않았습니다.")
    settings.ensure_directories()

    fixture_root = Path(__file__).resolve().parents[1] / "fixtures" / "imagegen"
    source = settings.var_dir / "jobs" / "live-imagegen" / "input" / "source.png"
    source.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(fixture_root / "backlit-still-life-source.png", source)
    destination = settings.output_dir / "imagegen" / "live-imagegen" / "result.png"
    parameters = GenerateAIParameters(
        execution_mode="openai-image-api",
        use_case="lighting-weather",
        prompt=(
            "Recover only the underexposed shadows on the mug and table so their "
            "detail is natural and visible."
        ),
        constraints=[
            "preserve the mug, cloth, window, warm backlight, geometry, and object positions"
        ],
        avoid=["new objects", "text", "logos", "watermark", "composition changes"],
    )

    result = OpenAIImagegenRunner(settings).edit(source, destination, parameters)

    assert result.path == destination.resolve()
    assert result.model == "gpt-image-2"
    assert result.quality == "low"
    assert result.size == "1024x1024"
    with Image.open(result.path) as image:
        image.load()
        assert image.size == (1024, 1024)
        assert image.format == "PNG"
        assert image.info == {}
        assert len(image.getexif()) == 0
