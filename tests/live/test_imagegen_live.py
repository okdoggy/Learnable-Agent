from __future__ import annotations

import os
import shutil
from pathlib import Path

import pytest
from PIL import Image

from lala.config import Settings
from lala.domain.models import GenerateAIParameters
from lala.renderers.imagegen import CodexImagegenRunner


@pytest.mark.live
def test_live_codex_builtin_imagegen_contract(settings: Settings) -> None:
    if os.getenv("LALA_RUN_LIVE_IMAGEGEN") != "1":
        pytest.skip("set LALA_RUN_LIVE_IMAGEGEN=1 to run the Codex built-in $imagegen test")
    if shutil.which(settings.codex_executable) is None:
        pytest.skip("Codex CLI is not installed on PATH")
    request_id = "req_live_imagegen"
    source = settings.var_dir / "jobs" / request_id / "input" / "source.png"
    source.parent.mkdir(parents=True)
    fixture = (
        Path(__file__).resolve().parents[1]
        / "fixtures"
        / "imagegen"
        / "backlit-still-life-source.png"
    )
    shutil.copyfile(fixture, source)
    destination = settings.output_dir / "imagegen" / request_id / "result.png"

    result = CodexImagegenRunner(settings).edit(
        source,
        destination,
        GenerateAIParameters(
            use_case="lighting-weather",
            prompt="구도를 유지하면서 머그잔의 어두운 그림자만 자연스럽게 회복",
            constraints=["머그잔, 천, 창문, 카메라 구도와 물체 위치를 유지"],
        ),
    )

    assert result.path.is_file()
    assert result.execution_mode == "codex-imagegen-builtin"
    with Image.open(result.path) as generated:
        generated.load()
        assert generated.format == "PNG"
        assert generated.info == {}
        assert len(generated.getexif()) == 0
