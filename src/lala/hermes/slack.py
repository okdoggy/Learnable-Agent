from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path

from lala.domain.errors import LalaError
from lala.domain.models import EditPlan, GenerateAIStep, LutStep
from lala.domain.validation import PlanRuntimeValidator
from lala.hermes.planner import Planner
from lala.knowledge.technical import TechnicalLibraryRepository
from lala.observability.audit import audit_event
from lala.observability.metrics import METRICS
from lala.renderers.executor import ToolExecutor
from lala.renderers.inspection import inspect_image
from lala.storage.workspace import WorkspaceManager


@dataclass(frozen=True, slots=True)
class SlackResponse:
    request_id: str
    plan: EditPlan
    message_ko: str
    output_path: Path | None
    execution_error: str | None = None


class SlackCoordinator:
    def __init__(
        self,
        *,
        planner: Planner,
        validator: PlanRuntimeValidator,
        executor: ToolExecutor,
        workspaces: WorkspaceManager,
    ) -> None:
        self.planner = planner
        self.validator = validator
        self.executor = executor
        self.workspaces = workspaces

    def handle(self, *, request_id: str, prompt: str, execute: bool = True) -> SlackResponse:
        started = time.monotonic()
        image_path = self.workspaces.require_input(request_id)
        inspection = inspect_image(image_path)
        plan = self.planner.plan(
            request_id=request_id,
            prompt=prompt,
            image_path=image_path,
            inspection=inspection,
        )
        plan = self.validator.validate(plan)
        if not execute:
            METRICS.increment("lala_edit_requests_total", channel="slack", status="recommended")
            audit_event(
                "edit_request_recommended",
                request_id=request_id,
                channel="slack",
                tools=[step.tool for step in plan.steps],
                latency_ms=round((time.monotonic() - started) * 1000, 2),
            )
            return SlackResponse(
                request_id, plan, format_slack_plan(plan, library=self.validator.library), None
            )
        try:
            report = self.executor.execute(plan)
        except LalaError as exc:
            error_message = exc.user_message_ko
            retryable = exc.retryable
            error_code = exc.code
        except Exception as exc:
            error_message = "편집 실행 중 내부 오류가 발생했습니다."
            retryable = True
            error_code = "INTERNAL_ERROR"
            audit_event(
                "slack_execution_exception",
                request_id=request_id,
                exception_type=type(exc).__name__,
            )
        else:
            message = format_slack_plan(plan, library=self.validator.library)
            for step in report.steps:
                if step.tool == "generate_ai" and step.renderer_size:
                    message += f"\n\n실행 설정\n- Generate AI 출력 크기: {step.renderer_size}"
            message += f"\n\n결과 이미지\n{report.final_path}"
            METRICS.increment("lala_edit_requests_total", channel="slack", status="completed")
            audit_event(
                "edit_request_completed",
                request_id=request_id,
                channel="slack",
                tools=[step.tool for step in report.steps],
                engine_versions=[step.engine_version for step in report.steps],
                output_sha256=report.final_sha256,
                latency_ms=round((time.monotonic() - started) * 1000, 2),
                evidence=[
                    {"skill_id": evidence.skill_id, "version": evidence.version}
                    for step in plan.steps
                    for evidence in step.evidence
                ],
            )
            return SlackResponse(request_id, plan, message, report.final_path)

        METRICS.increment(
            "lala_edit_requests_total", channel="slack", status="failed", error=error_code
        )
        audit_event(
            "edit_request_failed",
            request_id=request_id,
            channel="slack",
            error_code=error_code,
            retryable=retryable,
            latency_ms=round((time.monotonic() - started) * 1000, 2),
        )
        message = format_slack_plan(plan, library=self.validator.library)
        message += (
            "\n\n실행 결과\n"
            f"편집 실행에 실패했습니다: {error_message}\n"
            f"재시도 가능: {'예' if retryable else '아니요'}\n"
            f"요청 ID: {request_id}"
        )
        return SlackResponse(request_id, plan, message, None, error_message)


def format_slack_plan(plan: EditPlan, *, library: TechnicalLibraryRepository | None = None) -> str:
    tool_names = {"lut": "LUT", "generate_ai": "Generate AI"}
    lines = [f"추천 도구: {' → '.join(tool_names[step.tool] for step in plan.steps)}", "", "설정"]
    for step in plan.steps:
        lines.append(f"{step.order}. {tool_names[step.tool]}")
        if isinstance(step, LutStep):
            lines.extend(
                [
                    f"- LUT: {step.parameters.preset}",
                    f"- 강도: {step.parameters.lut_intensity:.2f}",
                    f"- 피부 보호: {'예' if step.parameters.skin_protection else '아니요'}",
                    f"- 그레인: {step.parameters.grain_amount:.2f}",
                    f"- 할레이션: {step.parameters.halation:.2f}",
                ]
            )
        elif isinstance(step, GenerateAIStep):
            lines.extend(
                [
                    f"- 작업: {step.parameters.use_case}",
                    f"- 실행: {step.parameters.execution_mode}",
                    f"- 요청: {step.parameters.prompt}",
                ]
            )
    lines.extend(["", "추천 이유", plan.overall_reason_ko, "", "참고한 technical-library"])
    evidence = {(item.skill_id, item.version) for step in plan.steps for item in step.evidence}
    if evidence:
        for technical_id, version in sorted(evidence):
            reference = f"- technical-library/{technical_id} v{version}"
            if library is not None:
                reference += f": {library.get_note(technical_id).title_ko}"
            lines.append(reference)
    else:
        lines.append("- 현재 요청에 적용 가능한 active technical-library 문서 없음")
    if plan.warnings_ko:
        lines.extend(["", "주의", *[f"- {warning}" for warning in plan.warnings_ko]])
    return "\n".join(lines)
