from __future__ import annotations

from datetime import datetime
from typing import Annotated, Generic, Literal, TypeVar

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from lala.domain.models import EditPlan


class ApiModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class UploadRequestBody(ApiModel):
    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "filename": "portrait.png",
                    "mime": "image/png",
                    "byte_size": 245760,
                    "sha256": None,
                }
            ]
        },
    )

    filename: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=255)
    ] = Field(description="사용자가 업로드하는 원본 파일명")
    mime: Literal["image/jpeg", "image/png", "image/webp"] = Field(description="허용된 이미지 MIME")
    byte_size: int = Field(gt=0, description="업로드할 정확한 바이트 크기")
    sha256: Annotated[str, StringConstraints(pattern=r"^[0-9a-fA-F]{64}$")] | None = Field(
        default=None, description="선택적 원본 SHA-256"
    )


class UploadRequestData(ApiModel):
    asset_id: str
    upload_url: str
    upload_method: Literal["PUT"] = "PUT"
    expires_at: datetime


class UploadStatusData(ApiModel):
    asset_id: str
    status: Literal["uploaded"]


class ClientCapabilitiesBody(ApiModel):
    edit_plan_version: Literal["1.0"]
    remaster_engine_version: Literal["1.0"]
    lut_catalog_version: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=64)
    ]


class EditRequestBody(ApiModel):
    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "schema_version": "1.0",
                    "client_request_id": "550e8400-e29b-41d4-a716-446655440000",
                    "asset_id": "asset_0123456789abcdef0123456789abcdef",
                    "prompt": "노을 분위기는 유지하고 얼굴만 자연스럽게 밝게 해줘",
                    "locale": "ko-KR",
                    "client_capabilities": {
                        "edit_plan_version": "1.0",
                        "remaster_engine_version": "1.0",
                        "lut_catalog_version": "2026-08-02",
                    },
                }
            ]
        },
    )

    schema_version: Literal["1.0"] = "1.0"
    client_request_id: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=8,
            max_length=128,
            pattern=r"^[a-zA-Z0-9._-]+$",
        ),
    ]
    asset_id: Annotated[str, StringConstraints(pattern=r"^asset_[0-9a-f]{32}$")]
    prompt: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1, max_length=8000)
    ] = Field(description="Hermes LLM이 이미지 전체 맥락과 함께 해석할 자연어 편집 요청")
    locale: Literal["ko-KR"] = "ko-KR"
    client_capabilities: ClientCapabilitiesBody


class EditAcceptedData(ApiModel):
    request_id: str
    status: Literal["queued", "analyzing", "completed", "failed"]
    status_url: str


class EditStatusData(ApiModel):
    request_id: str
    status: Literal["queued", "analyzing", "completed", "failed"]
    plan: EditPlan | None = None


class ServiceCapabilitiesData(ApiModel):
    planner: Literal["hermes-llm"] = "hermes-llm"
    edit_plan_versions: tuple[Literal["1.0"], ...] = ("1.0",)
    remaster_engine_versions: tuple[Literal["1.0"], ...] = ("1.0",)
    imagegen_execution_modes: tuple[Literal["codex-imagegen-builtin"], ...] = (
        "codex-imagegen-builtin",
    )
    upload_mime_types: tuple[Literal["image/jpeg", "image/png", "image/webp"], ...] = (
        "image/jpeg",
        "image/png",
        "image/webp",
    )
    swagger_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"


class ApiError(ApiModel):
    code: str
    message_ko: str
    retryable: bool


class ApiMeta(ApiModel):
    created_at: datetime
    expires_at: datetime | None = None


DataT = TypeVar("DataT")


class Envelope(ApiModel, Generic[DataT]):
    data: DataT | None
    error: ApiError | None
    meta: ApiMeta
