from __future__ import annotations

import asyncio
import secrets
from contextlib import asynccontextmanager
from datetime import UTC, datetime
from typing import Annotated

import uvicorn
from fastapi import BackgroundTasks, Depends, FastAPI, Header, Query, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse, RedirectResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from lala.api.models import (
    ApiError,
    ApiMeta,
    EditAcceptedData,
    EditRequestBody,
    EditStatusData,
    Envelope,
    ServiceCapabilitiesData,
    UploadRequestBody,
    UploadRequestData,
    UploadStatusData,
)
from lala.api.service import EditRequestService
from lala.config import Settings
from lala.domain.errors import LalaError
from lala.domain.validation import LutCalibrationPolicy, PlanRuntimeValidator
from lala.hermes.planner import Planner, build_planner
from lala.knowledge.technical import TechnicalLibraryRepository
from lala.observability.metrics import METRICS
from lala.renderers.lut import LutCatalog
from lala.resilience import SlidingWindowLimit
from lala.storage.assets import AssetService
from lala.storage.database import Database
from lala.storage.workspace import WorkspaceManager


def _now() -> datetime:
    return datetime.now(UTC)


def create_app(settings: Settings | None = None, *, planner: Planner | None = None) -> FastAPI:
    config = settings or Settings.from_env()
    config.ensure_directories()
    database = Database(config.database_path)
    database.initialize()
    assets = AssetService(config, database)
    catalog = LutCatalog(config.lut_manifest_path)
    technical_library = TechnicalLibraryRepository(config.technical_library_dir)
    runtime_validator = PlanRuntimeValidator(
        catalog,
        technical_library,
        LutCalibrationPolicy(config.parameter_registry_path),
    )
    selected_planner = planner or build_planner(config)
    workspaces = WorkspaceManager(config.var_dir / "jobs")
    requests = EditRequestService(
        settings=config,
        database=database,
        planner=selected_planner,
        validator=runtime_validator,
        workspaces=workspaces,
    )
    rate_limiter = SlidingWindowLimit(
        limit=config.rate_limit_per_minute,
        window_seconds=60,
        code="RATE_LIMITED",
        message_ko="API 요청 한도에 도달했습니다. 잠시 후 다시 시도해 주세요.",
    )
    bearer_scheme = HTTPBearer(auto_error=False)

    @asynccontextmanager
    async def lifespan(lifespan_app: FastAPI):
        recovery_tasks = {
            asyncio.create_task(asyncio.to_thread(requests.process, request_id))
            for request_id in database.requeue_incomplete_requests()
        }
        lifespan_app.state.recovery_tasks = recovery_tasks
        try:
            yield
        finally:
            if recovery_tasks:
                await asyncio.gather(*recovery_tasks, return_exceptions=True)

    app = FastAPI(
        title="lala API",
        version="1.0.0",
        description=(
            "Vibe Editing Tool 서버가 이미지 업로드와 Hermes LLM 기반 EditPlan 생성을 "
            "연동하기 위한 비동기 API입니다. 브라우저가 아니라 Vibe 서버에서 Bearer 인증으로 "
            "호출하세요. `upload request → signed PUT → edit request → status polling` 순서입니다."
        ),
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        swagger_ui_parameters={
            "displayRequestDuration": True,
            "filter": True,
            "persistAuthorization": True,
        },
        openapi_tags=[
            {"name": "Capabilities", "description": "지원 계약과 문서 URL 조회"},
            {"name": "Assets", "description": "서명된 이미지 업로드"},
            {"name": "Edit requests", "description": "비동기 LLM 편집 계획 생성과 조회"},
            {"name": "Operations", "description": "서비스 상태와 관측성"},
        ],
        lifespan=lifespan,
    )
    app.state.settings = config
    app.state.database = database
    app.state.assets = assets
    app.state.edit_requests = requests

    async def require_auth(
        request: Request,
        credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    ) -> None:
        if credentials is None or credentials.scheme.casefold() != "bearer":
            raise LalaError("UNAUTHORIZED", "인증이 필요합니다.", False)
        if not secrets.compare_digest(credentials.credentials, config.api_key):
            raise LalaError("UNAUTHORIZED", "인증 정보가 올바르지 않습니다.", False)
        client_host = request.client.host if request.client else "unknown"
        rate_limiter.consume(client_host)

    @app.exception_handler(LalaError)
    async def lala_error_handler(_: Request, exc: LalaError) -> JSONResponse:
        status_code = _status_for_error(exc.code)
        return JSONResponse(
            status_code=status_code,
            content=Envelope[None](
                data=None,
                error=ApiError(
                    code=exc.code,
                    message_ko=exc.user_message_ko,
                    retryable=exc.retryable,
                ),
                meta=ApiMeta(created_at=_now()),
            ).model_dump(mode="json"),
            headers={"WWW-Authenticate": "Bearer"} if status_code == 401 else None,
        )

    @app.exception_handler(RequestValidationError)
    async def validation_error_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
        del exc
        return JSONResponse(
            status_code=422,
            content=Envelope[None](
                data=None,
                error=ApiError(
                    code="INVALID_REQUEST",
                    message_ko="요청 본문 또는 파라미터 형식이 올바르지 않습니다.",
                    retryable=False,
                ),
                meta=ApiMeta(created_at=_now()),
            ).model_dump(mode="json"),
        )

    @app.get("/", include_in_schema=False)
    async def documentation_root() -> RedirectResponse:
        return RedirectResponse(url="/docs")

    @app.get("/health", include_in_schema=False, tags=["Operations"])
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get(
        "/metrics",
        include_in_schema=False,
        dependencies=[Depends(require_auth)],
        response_class=PlainTextResponse,
        tags=["Operations"],
    )
    async def metrics() -> str:
        return METRICS.render_prometheus()

    @app.post(
        "/v1/assets/upload-requests",
        response_model=Envelope[UploadRequestData],
        dependencies=[Depends(require_auth)],
        tags=["Assets"],
        summary="서명된 이미지 업로드 URL 발급",
        operation_id="createUploadRequest",
        description=(
            "파일 메타데이터를 먼저 등록합니다. 응답의 `upload_url`에 정확한 바이트와 "
            "Content-Type으로 PUT한 뒤 편집 요청을 생성하세요."
        ),
    )
    async def create_upload(body: UploadRequestBody) -> Envelope[UploadRequestData]:
        result = assets.create_upload_request(
            filename=body.filename,
            mime=body.mime,
            byte_size=body.byte_size,
            sha256=body.sha256,
        )
        expires = datetime.fromtimestamp(result.expires_at_epoch, UTC)
        return Envelope[UploadRequestData](
            data=UploadRequestData(
                asset_id=result.asset_id,
                upload_url=result.upload_url,
                expires_at=expires,
            ),
            error=None,
            meta=ApiMeta(created_at=_now(), expires_at=expires),
        )

    @app.put(
        "/v1/assets/{asset_id}/content",
        response_model=Envelope[UploadStatusData],
        tags=["Assets"],
        summary="서명 URL로 이미지 업로드",
        operation_id="uploadAssetContent",
        description="발급된 짧은 수명의 서명 URL 전용 엔드포인트입니다.",
    )
    async def upload_content(
        asset_id: str,
        request: Request,
        expires: Annotated[int, Query(gt=0)],
        token: Annotated[str, Query(min_length=16, max_length=256)],
        content_type: Annotated[str | None, Header()] = None,
    ) -> Envelope[UploadStatusData]:
        if not content_type:
            raise LalaError("INVALID_IMAGE", "Content-Type이 필요합니다.", False)
        chunks: list[bytes] = []
        total = 0
        async for chunk in request.stream():
            total += len(chunk)
            if total > config.max_asset_bytes:
                raise LalaError("INVALID_IMAGE", "이미지 파일이 너무 큽니다.", False)
            chunks.append(chunk)
        record = assets.store_upload(
            asset_id=asset_id,
            expires=expires,
            token=token,
            content=b"".join(chunks),
            content_type=content_type,
        )
        return Envelope[UploadStatusData](
            data=UploadStatusData(asset_id=record.asset_id, status="uploaded"),
            error=None,
            meta=ApiMeta(created_at=_now(), expires_at=record.expires_at),
        )

    @app.post(
        "/v1/edit-requests",
        status_code=status.HTTP_202_ACCEPTED,
        response_model=Envelope[EditAcceptedData],
        dependencies=[Depends(require_auth)],
        tags=["Edit requests"],
        summary="Hermes LLM 편집 계획 생성 요청",
        operation_id="createEditRequest",
        description=(
            "업로드 완료된 asset과 자연어 요청을 제출합니다. 즉시 202를 반환하며 "
            "`status_url`을 완료 또는 실패까지 polling합니다."
        ),
    )
    async def create_edit(
        body: EditRequestBody, background: BackgroundTasks
    ) -> Envelope[EditAcceptedData]:
        record, _ = requests.submit(
            client_request_id=body.client_request_id,
            asset_id=body.asset_id,
            prompt=body.prompt,
            locale=body.locale,
            client_capabilities=body.client_capabilities.model_dump(),
        )
        if record.status == "queued":
            background.add_task(requests.process, record.request_id)
        status_url = f"{config.public_base_url}/v1/edit-requests/{record.request_id}"
        return Envelope[EditAcceptedData](
            data=EditAcceptedData(
                request_id=record.request_id,
                status=record.status,
                status_url=status_url,
            ),
            error=None,
            meta=ApiMeta(created_at=record.created_at, expires_at=record.expires_at),
        )

    @app.get(
        "/v1/edit-requests/{request_id}",
        response_model=Envelope[EditStatusData],
        dependencies=[Depends(require_auth)],
        tags=["Edit requests"],
        summary="편집 계획 상태 조회",
        operation_id="getEditRequest",
        description="완료 시 실행 가능한 EditPlan 1.0과 한국어 판단 근거를 반환합니다.",
    )
    async def get_edit(request_id: str) -> Envelope[EditStatusData]:
        record = database.get_edit_request(request_id)
        error = None
        if record.status == "failed":
            error = ApiError(
                code=record.error_code or "INTERNAL_ERROR",
                message_ko=record.error_message_ko or "요청 처리에 실패했습니다.",
                retryable=bool(record.retryable),
            )
        return Envelope[EditStatusData](
            data=EditStatusData(
                request_id=record.request_id,
                status=record.status,
                plan=record.plan,
            ),
            error=error,
            meta=ApiMeta(created_at=record.created_at, expires_at=record.expires_at),
        )

    @app.get(
        "/v1/capabilities",
        response_model=Envelope[ServiceCapabilitiesData],
        dependencies=[Depends(require_auth)],
        tags=["Capabilities"],
        summary="클라이언트 연동 계약 조회",
        operation_id="getCapabilities",
    )
    async def get_capabilities() -> Envelope[ServiceCapabilitiesData]:
        return Envelope[ServiceCapabilitiesData](
            data=ServiceCapabilitiesData(),
            error=None,
            meta=ApiMeta(created_at=_now()),
        )

    return app


def _status_for_error(code: str) -> int:
    if code == "UNAUTHORIZED":
        return 401
    if code in {"NOT_FOUND"}:
        return 404
    if code in {"IDEMPOTENCY_CONFLICT", "ASSET_STATE_CONFLICT", "REQUEST_STATE_CONFLICT"}:
        return 409
    if code in {"RATE_LIMITED"}:
        return 429
    if code in {"INTERNAL_ERROR"}:
        return 500
    return 400


def main() -> None:
    uvicorn.run("lala.api.app:create_app", factory=True, host="0.0.0.0", port=8000)
