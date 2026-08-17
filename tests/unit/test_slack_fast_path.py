from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest
from PIL import Image

from lala.domain.errors import LalaError
from lala.domain.models import (
    EditPlan,
    LutParameters,
    LutStep,
    RemasterParameters,
    RemasterStep,
    SkillEvidence,
)
from lala.domain.validation import PlanRuntimeValidator
from lala.hermes.slack import SlackCoordinator, format_slack_plan
from lala.knowledge.technical import TechnicalLibraryRepository
from lala.mcp.server import build_runtime, create_mcp
from lala.renderers.executor import ToolExecutor
from lala.renderers.imagegen import CopyingImagegenRunner
from lala.renderers.lut import LutCatalog, LutRenderer
from lala.renderers.remaster import RemasterRenderer
from tests.fakes import StaticRemasterPlanner


class FailingPlanner:
    def plan(self, **_: object) -> None:
        raise LalaError("AGENT_REQUEST_TOO_LARGE", "이미지 처리 요청이 너무 큽니다.", False)


def _cache_image(settings, filename: str = "img_fastpath.jpeg") -> Path:
    cache = settings.project_root / "var" / "slack-cache"
    cache.mkdir(parents=True, exist_ok=True)
    source = cache / filename
    Image.new("RGB", (48, 32), (20, 30, 40)).save(source, format="JPEG")
    return source


def _runtime_with_static_coordinator(settings, planner=None):
    imagegen = CopyingImagegenRunner()
    runtime = build_runtime(settings, imagegen=imagegen)
    catalog = LutCatalog(settings.lut_manifest_path)
    library = TechnicalLibraryRepository(settings.technical_library_dir)
    runtime.slack_coordinator = SlackCoordinator(
        planner=planner or StaticRemasterPlanner(),
        validator=PlanRuntimeValidator(catalog, library),
        executor=ToolExecutor(
            settings=settings,
            workspaces=runtime.workspaces,
            remaster=RemasterRenderer(),
            lut=LutRenderer(catalog),
            imagegen=imagegen,
        ),
        workspaces=runtime.workspaces,
    )
    return runtime


def test_prepare_slack_image_registers_cached_attachment(settings) -> None:
    _cache_image(settings)
    runtime = build_runtime(settings, imagegen=CopyingImagegenRunner())

    prepared = runtime.prepare_slack_image("img_fastpath.jpeg")

    assert prepared.request_id == "req_slack_fastpath"
    assert (
        prepared.input_path
        == (settings.var_dir / "jobs" / "req_slack_fastpath" / "input" / "source.png").resolve()
    )
    with Image.open(prepared.input_path) as image:
        assert image.format == "PNG"
        assert image.size == (48, 32)
        assert image.info == {}
        assert len(image.getexif()) == 0


def test_prepare_slack_image_rejects_path_instead_of_basename(settings) -> None:
    runtime = build_runtime(settings, imagegen=CopyingImagegenRunner())

    with pytest.raises(LalaError, match="첨부파일 이름") as error:
        runtime.prepare_slack_image("../img_escape.jpeg")

    assert error.value.code == "INVALID_SLACK_ATTACHMENT"


@pytest.mark.asyncio
async def test_process_slack_image_executes_complete_edit_in_one_mcp_call(settings) -> None:
    _cache_image(settings)
    runtime = _runtime_with_static_coordinator(settings)

    _, result = await create_mcp(settings, runtime=runtime).call_tool(
        "process_slack_image",
        {
            "cache_filename": "img_fastpath.jpeg",
            "prompt": "야간 분위기를 유지하며 자연스럽게 보정해줘",
            "mode": "edit",
        },
    )

    assert isinstance(result, dict)
    assert result["request_id"] == "req_slack_fastpath"
    assert result["mode"] == "edit"
    assert result["execution_error"] is None
    output_path = Path(result["output_path"])
    assert output_path.is_file()
    assert "추천 도구: LUT" in result["message_ko"]


@pytest.mark.asyncio
async def test_process_slack_image_recommends_without_rendering(settings) -> None:
    _cache_image(settings)
    runtime = _runtime_with_static_coordinator(settings)

    _, result = await create_mcp(settings, runtime=runtime).call_tool(
        "process_slack_image",
        {
            "cache_filename": "img_fastpath.jpeg",
            "prompt": "이 사진을 어떻게 보정하면 좋을까?",
            "mode": "recommend",
        },
    )

    assert isinstance(result, dict)
    assert result["mode"] == "recommend"
    assert result["output_path"] is None
    assert not (settings.var_dir / "jobs" / "req_slack_fastpath" / "output" / "result.png").exists()


@pytest.mark.asyncio
async def test_process_slack_image_returns_request_id_when_planning_fails(settings) -> None:
    _cache_image(settings)
    runtime = _runtime_with_static_coordinator(settings, planner=FailingPlanner())

    _, result = await create_mcp(settings, runtime=runtime).call_tool(
        "process_slack_image",
        {
            "cache_filename": "img_fastpath.jpeg",
            "prompt": "자연스럽게 보정해줘",
            "mode": "edit",
        },
    )

    assert result["request_id"] == "req_slack_fastpath"
    assert result["output_path"] is None
    assert result["execution_error"] == "이미지 처리 요청이 너무 큽니다."
    assert "요청 ID: req_slack_fastpath" in result["message_ko"]


def test_format_slack_plan_includes_referenced_technical_document_title() -> None:
    plan = EditPlan(
        request_id="req_document_title",
        summary_ko="그림자 세부를 보수적으로 회복합니다.",
        steps=[
            LutStep(
                order=1,
                tool="lut",
                parameters=LutParameters(preset="documentary", grain_amount=0, halation=0),
                reason_ko="전역 톤과 색감을 보수적으로 조정합니다.",
                evidence=[SkillEvidence(skill_id="shadow-recovery", version="1.0.0")],
            )
        ],
        overall_reason_ko="노출 상승보다 그림자 구간만 조정하는 편이 적합합니다.",
        confidence=0.8,
    )

    class TitleLibrary:
        def get_note(self, technical_id: str) -> SimpleNamespace:
            assert technical_id == "shadow-recovery"
            return SimpleNamespace(title_ko="그림자 세부 회복")

    message = format_slack_plan(plan, library=TitleLibrary())

    assert "technical-library/shadow-recovery v1.0.0: 그림자 세부 회복" in message


def test_format_slack_plan_describes_remaster_operations() -> None:
    plan = EditPlan(
        request_id="req_remaster_format",
        summary_ko="기본 보정으로 톤과 디테일을 정리합니다.",
        steps=[
            RemasterStep(
                order=1,
                tool="remaster",
                parameters=RemasterParameters(brightness=8, sharpen_amount=0.8),
                reason_ko="밝기와 에지 분리를 절제해 보완합니다.",
                evidence=[],
            )
        ],
        overall_reason_ko="결정론적 기본 보정으로 충분합니다.",
        confidence=0.7,
    )

    message = format_slack_plan(plan)

    assert "추천 도구: Remaster" in message
    assert "밝기: 8" in message
    assert "샤프닝 amount: 0.80" in message
