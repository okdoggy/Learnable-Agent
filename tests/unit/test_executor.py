from __future__ import annotations

from pathlib import Path

from PIL import Image

from lala.domain.models import EditPlan, LutParameters, LutStep, RemasterParameters, RemasterStep
from lala.renderers.executor import ToolExecutor
from lala.renderers.imagegen import CopyingImagegenRunner
from lala.renderers.lut import LutCatalog, LutRenderer
from lala.renderers.remaster import RemasterRenderer
from lala.storage.workspace import WorkspaceManager


def test_executor_runs_remaster_lut_and_detail_remaster_in_order(settings, tmp_path: Path) -> None:
    workspaces = WorkspaceManager(settings.var_dir / "jobs")
    workspace = workspaces.create("req_remaster_lut")
    Image.new("RGB", (32, 24), (60, 80, 100)).save(workspace.input_image)
    catalog = LutCatalog(settings.lut_manifest_path)
    plan = EditPlan(
        request_id="req_remaster_lut",
        summary_ko="기본 보정 뒤 LUT와 디테일 마무리를 적용합니다.",
        steps=[
            RemasterStep(
                order=1,
                tool="remaster",
                parameters=RemasterParameters(brightness=4),
                reason_ko="먼저 기본 노출을 보수적으로 정리합니다.",
                evidence=[],
            ),
            LutStep(
                order=2,
                tool="lut",
                parameters=LutParameters(preset="documentary"),
                reason_ko="기본 톤 위에 승인된 전역 그레이드를 적용합니다.",
                evidence=[],
            ),
            RemasterStep(
                order=3,
                tool="remaster",
                parameters=RemasterParameters(sharpen_amount=0.8),
                reason_ko="마지막에 전역 에지 선명도를 절제해 보완합니다.",
                evidence=[],
            ),
        ],
        overall_reason_ko="기본 보정과 창의적 그레이드 및 디테일 마무리를 분리합니다.",
        confidence=0.7,
    )

    report = ToolExecutor(
        settings=settings,
        workspaces=workspaces,
        remaster=RemasterRenderer(),
        lut=LutRenderer(catalog),
        imagegen=CopyingImagegenRunner(),
    ).execute(plan)

    assert [step.tool for step in report.steps] == ["remaster", "lut", "remaster"]
    assert report.final_path.is_file()
    assert report.final_sha256 == report.steps[-1].output_sha256
