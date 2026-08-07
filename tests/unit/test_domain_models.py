from __future__ import annotations

import pytest
from pydantic import ValidationError

from lala.domain.models import EditPlan, GenerateAIParameters, RemasterParameters


def _remaster_step(order: int = 1) -> dict[str, object]:
    return {
        "order": order,
        "tool": "remaster",
        "parameters": RemasterParameters().model_dump(),
        "reason_ko": "원본을 보존하는 기본 보정입니다.",
        "evidence": [],
    }


def _generate_step(order: int = 1) -> dict[str, object]:
    return {
        "order": order,
        "tool": "generate_ai",
        "parameters": {
            "operation": "edit",
            "use_case": "lighting-weather",
            "execution_mode": "openai-image-api",
            "prompt": "맑은 날을 비 오는 날로 바꿔줘",
            "constraints": ["인물 유지"],
            "avoid": ["워터마크"],
            "output_format": "png",
        },
        "reason_ko": "생성적 날씨 변경이 필요합니다.",
        "evidence": [],
    }


def _plan(steps: list[dict[str, object]]) -> dict[str, object]:
    return {
        "schema_version": "1.0",
        "request_id": "req_123",
        "summary_ko": "이미지를 자연스럽게 편집합니다.",
        "steps": steps,
        "overall_reason_ko": "사용자 의도에 맞는 도구를 골랐습니다.",
        "confidence": 0.7,
        "warnings_ko": [],
    }


def test_remaster_parameter_range_is_strict() -> None:
    with pytest.raises(ValidationError):
        RemasterParameters(brightness=101)
    with pytest.raises(ValidationError):
        RemasterParameters.model_validate({"brightness": 1.5}, strict=True)


def test_generate_ai_cannot_be_mixed_with_deterministic_steps() -> None:
    with pytest.raises(ValidationError, match="only v1 step"):
        EditPlan.model_validate(_plan([_generate_step(1), _remaster_step(2)]))


def test_steps_must_be_contiguous() -> None:
    with pytest.raises(ValidationError, match="contiguously"):
        EditPlan.model_validate(_plan([_remaster_step(2)]))


def test_edit_plan_explanations_require_korean() -> None:
    payload = _plan([_remaster_step()])
    payload["overall_reason_ko"] = "English only"
    with pytest.raises(ValidationError):
        EditPlan.model_validate(payload)


@pytest.mark.parametrize("legacy_field", ["model", "quality", "size"])
def test_generate_contract_rejects_renderer_owned_fields(legacy_field: str) -> None:
    with pytest.raises(ValidationError):
        GenerateAIParameters.model_validate(
            {
                "use_case": "lighting-weather",
                "prompt": "날씨 변경",
                legacy_field: "legacy-api-value",
            }
        )


def test_generate_contract_uses_openai_image_api_mode() -> None:
    parameters = GenerateAIParameters(
        use_case="lighting-weather",
        prompt="날씨 변경",
    )
    assert parameters.execution_mode == "openai-image-api"
