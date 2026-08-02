from __future__ import annotations

from pathlib import Path

from PIL import Image

from lala.config import Settings
from lala.domain.errors import ExecutionError
from lala.domain.models import GenerateAIParameters
from lala.domain.validation import PlanRuntimeValidator
from lala.hermes.slack import SlackCoordinator
from lala.knowledge.technical import TechnicalLibraryRepository
from lala.renderers.executor import ToolExecutor
from lala.renderers.imagegen import CopyingImagegenRunner, ImagegenResult
from lala.renderers.lut import LutCatalog, LutRenderer
from lala.renderers.remaster import RemasterRenderer
from lala.storage.workspace import WorkspaceManager
from tests.fakes import StaticGeneratePlanner, StaticRemasterPlanner


class FailingImagegenRunner:
    def edit(
        self, source: Path, destination: Path, parameters: GenerateAIParameters
    ) -> ImagegenResult:
        del source, destination, parameters
        raise ExecutionError("이미지 생성 서비스가 일시적으로 응답하지 않습니다.", retryable=True)


def test_slack_returns_explanation_and_existing_result(settings: Settings) -> None:
    workspaces = WorkspaceManager(settings.var_dir / "jobs")
    workspace = workspaces.create("req_slack_test")
    Image.new("RGB", (32, 24), (30, 40, 50)).save(workspace.input_image)
    catalog = LutCatalog(settings.lut_manifest_path)
    library = TechnicalLibraryRepository(settings.technical_library_dir)
    coordinator = SlackCoordinator(
        planner=StaticRemasterPlanner(),
        validator=PlanRuntimeValidator(catalog, library),
        executor=ToolExecutor(
            settings=settings,
            workspaces=workspaces,
            remaster=RemasterRenderer(),
            lut=LutRenderer(catalog),
            imagegen=CopyingImagegenRunner(),
        ),
        workspaces=workspaces,
    )

    response = coordinator.handle(
        request_id="req_slack_test",
        prompt="얼굴을 자연스럽게 밝고 또렷하게 해줘",
    )

    assert response.output_path is not None
    assert response.output_path.is_file()
    assert "추천 도구: Remaster" in response.message_ko
    assert "추천 이유" in response.message_ko
    assert str(response.output_path) in response.message_ko


def test_slack_preserves_recommendation_when_execution_fails(settings: Settings) -> None:
    workspaces = WorkspaceManager(settings.var_dir / "jobs")
    workspace = workspaces.create("req_slack_failure")
    Image.new("RGB", (32, 24), (30, 40, 50)).save(workspace.input_image)
    catalog = LutCatalog(settings.lut_manifest_path)
    library = TechnicalLibraryRepository(settings.technical_library_dir)
    coordinator = SlackCoordinator(
        planner=StaticGeneratePlanner(),
        validator=PlanRuntimeValidator(catalog, library),
        executor=ToolExecutor(
            settings=settings,
            workspaces=workspaces,
            remaster=RemasterRenderer(),
            lut=LutRenderer(catalog),
            imagegen=FailingImagegenRunner(),
        ),
        workspaces=workspaces,
    )

    response = coordinator.handle(
        request_id="req_slack_failure",
        prompt="인물은 유지하고 배경을 바꿔줘",
    )

    assert response.output_path is None
    assert response.execution_error is not None
    assert "추천 도구: Generate AI" in response.message_ko
    assert "편집 실행에 실패했습니다" in response.message_ko
    assert "재시도 가능: 예" in response.message_ko
    assert "req_slack_failure" in response.message_ko
