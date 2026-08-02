from __future__ import annotations

import uuid
from dataclasses import dataclass

from lala.config import Settings
from lala.domain.errors import LalaError
from lala.domain.validation import ClientCapabilities, PlanRuntimeValidator
from lala.hermes.planner import Planner
from lala.observability.audit import audit_event
from lala.observability.metrics import METRICS
from lala.renderers.image_io import ImageAssetValidator
from lala.renderers.inspection import inspect_image
from lala.storage.database import Database, EditRequestRecord
from lala.storage.workspace import WorkspaceManager


@dataclass(slots=True)
class EditRequestService:
    settings: Settings
    database: Database
    planner: Planner
    validator: PlanRuntimeValidator
    workspaces: WorkspaceManager

    def submit(
        self,
        *,
        client_request_id: str,
        asset_id: str,
        prompt: str,
        locale: str,
        client_capabilities: dict[str, str],
    ) -> tuple[EditRequestRecord, bool]:
        asset = self.database.get_asset(asset_id)
        if asset.status != "uploaded" or asset.path is None:
            raise LalaError("ASSET_NOT_READY", "이미지 업로드가 완료되지 않았습니다.", True)
        request_id = f"req_{uuid.uuid4().hex}"
        record, created = self.database.create_or_get_edit_request(
            request_id=request_id,
            client_request_id=client_request_id,
            asset_id=asset_id,
            prompt=prompt,
            locale=locale,
            client_capabilities=client_capabilities,
            ttl_seconds=self.settings.asset_ttl_seconds,
        )
        audit_event(
            "edit_request_submitted",
            request_id=record.request_id,
            channel="vibe",
            asset_id=asset_id,
            idempotent_replay=not created,
        )
        METRICS.increment("lala_edit_requests_total", channel="vibe", status="submitted")
        return record, created

    def process(self, request_id: str) -> None:
        if not self.database.transition_request(request_id, expected="queued", target="analyzing"):
            return
        try:
            request = self.database.get_edit_request(request_id)
            asset = self.database.get_asset(request.asset_id)
            if asset.status != "uploaded" or asset.path is None or not asset.path.is_file():
                raise LalaError("ASSET_NOT_READY", "업로드 이미지를 찾을 수 없습니다.", True)
            workspace = self.workspaces.create(request_id)
            image_validator = ImageAssetValidator(
                max_bytes=self.settings.max_asset_bytes,
                max_pixels=self.settings.max_image_pixels,
            )
            normalized = image_validator.normalize(asset.path, workspace.input_image)
            inspection = inspect_image(workspace.input_image)
            plan = self.planner.plan(
                request_id=request_id,
                prompt=request.prompt,
                image_path=workspace.input_image,
                inspection=inspection,
            )
            capabilities = ClientCapabilities(**request.client_capabilities)
            plan = self.validator.validate(plan, capabilities)
            self.database.complete_request(request_id, plan)
            METRICS.increment("lala_edit_requests_total", channel="vibe", status="completed")
            for step in plan.steps:
                METRICS.increment("lala_tool_selection_total", channel="vibe", tool=step.tool)
            audit_event(
                "edit_request_completed",
                request_id=request_id,
                channel="vibe",
                input_mime=normalized.mime,
                input_bytes=normalized.byte_size,
                input_width=normalized.width,
                input_height=normalized.height,
                input_sha256=normalized.sha256,
                tools=[step.tool for step in plan.steps],
                evidence=[
                    {"skill_id": evidence.skill_id, "version": evidence.version}
                    for step in plan.steps
                    for evidence in step.evidence
                ],
            )
        except LalaError as exc:
            self.database.fail_request(
                request_id,
                code=exc.code,
                message_ko=exc.user_message_ko,
                retryable=exc.retryable,
            )
            METRICS.increment(
                "lala_edit_requests_total", channel="vibe", status="failed", error=exc.code
            )
            audit_event(
                "edit_request_failed",
                request_id=request_id,
                channel="vibe",
                error_code=exc.code,
                retryable=exc.retryable,
            )
        except Exception as exc:  # keep stable API errors; details only go to server logs
            self.database.fail_request(
                request_id,
                code="INTERNAL_ERROR",
                message_ko="요청 처리 중 내부 오류가 발생했습니다.",
                retryable=True,
            )
            METRICS.increment(
                "lala_edit_requests_total",
                channel="vibe",
                status="failed",
                error="INTERNAL_ERROR",
            )
            audit_event(
                "edit_request_failed",
                request_id=request_id,
                channel="vibe",
                error_code="INTERNAL_ERROR",
                retryable=True,
                exception_type=type(exc).__name__,
            )
