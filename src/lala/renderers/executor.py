from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from lala.config import Settings
from lala.domain.errors import ExecutionError
from lala.domain.models import EditPlan, GenerateAIStep, LutStep
from lala.renderers.image_io import sha256_file
from lala.renderers.imagegen import ImagegenRunner
from lala.renderers.lut import LutRenderer
from lala.storage.workspace import WorkspaceManager, ensure_within


@dataclass(frozen=True, slots=True)
class ExecutedStep:
    order: int
    tool: str
    output_path: Path
    output_sha256: str
    engine_version: str
    renderer_size: str | None = None


@dataclass(frozen=True, slots=True)
class ExecutionReport:
    request_id: str
    steps: tuple[ExecutedStep, ...]
    final_path: Path
    final_sha256: str


class ToolExecutor:
    def __init__(
        self,
        *,
        settings: Settings,
        workspaces: WorkspaceManager,
        lut: LutRenderer,
        imagegen: ImagegenRunner,
        remaster: object | None = None,
    ) -> None:
        del remaster
        self.settings = settings
        self.workspaces = workspaces
        self.lut = lut
        self.imagegen = imagegen

    def execute(self, plan: EditPlan) -> ExecutionReport:
        workspace = self.workspaces.get(plan.request_id)
        source = self.workspaces.require_input(plan.request_id)
        executed: list[ExecutedStep] = []
        for index, step in enumerate(plan.steps):
            final = index == len(plan.steps) - 1
            if isinstance(step, GenerateAIStep):
                output_root = ensure_within(
                    self.settings.output_dir / "imagegen" / plan.request_id,
                    self.settings.output_dir / "imagegen",
                )
                destination = ensure_within(output_root / "result.png", output_root)
                result = self.imagegen.edit(source, destination, step.parameters)
                engine_version = result.adapter_version
                renderer_size = result.size
                output_hash = result.sha256
            elif isinstance(step, LutStep):
                destination = workspace.output() if final else workspace.intermediate(step.order)
                result = self.lut.render(source, destination, step.parameters)
                engine_version = result.engine_version
                renderer_size = None
                output_hash = result.sha256
            else:  # pragma: no cover - discriminated union makes this unreachable
                raise ExecutionError("알 수 없는 편집 도구입니다.", retryable=False)
            if not destination.is_file():
                raise ExecutionError("편집 결과 파일이 생성되지 않았습니다.", retryable=True)
            executed.append(
                ExecutedStep(
                    order=step.order,
                    tool=step.tool,
                    output_path=destination.resolve(),
                    output_sha256=output_hash,
                    engine_version=engine_version,
                    renderer_size=renderer_size,
                )
            )
            source = destination.resolve()
        final_path = executed[-1].output_path
        return ExecutionReport(
            request_id=plan.request_id,
            steps=tuple(executed),
            final_path=final_path,
            final_sha256=sha256_file(final_path),
        )
