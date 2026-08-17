from __future__ import annotations

from pathlib import Path

import pytest

from lala.domain.errors import PlanValidationError
from lala.domain.models import EditPlan, LutParameters, LutStep, RemasterParameters, RemasterStep
from lala.domain.validation import LutCalibrationPolicy
from lala.knowledge.technical import TechnicalLibraryRepository

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _plan(parameters: RemasterParameters) -> EditPlan:
    return EditPlan(
        request_id="req_pre_lut_tonal_safety",
        summary_ko="창의 LUT 전에 필요한 기술 보정을 제한합니다.",
        steps=[
            RemasterStep(
                order=1,
                tool="remaster",
                parameters=parameters,
                reason_ko="필요한 전역 기술 보정을 최소 범위에서 적용합니다.",
                evidence=[],
            ),
            LutStep(
                order=2,
                tool="lut",
                parameters=LutParameters(preset="documentary"),
                reason_ko="승인된 LUT로 의도한 전역 그레이드를 적용합니다.",
                evidence=[],
            ),
        ],
        overall_reason_ko="LUT보다 앞선 보정의 톤 누적을 피합니다.",
        confidence=0.7,
    )


def _policy() -> LutCalibrationPolicy:
    return LutCalibrationPolicy(PROJECT_ROOT / "config" / "parameter-registry.yaml")


def test_pre_lut_remaster_rejects_exposure_shadow_highlight_stack(tmp_path: Path) -> None:
    plan = _plan(RemasterParameters(brightness=8, shadows=18, highlights=-10))

    with pytest.raises(PlanValidationError, match="pre-LUT"):
        _policy().validate(plan, TechnicalLibraryRepository(tmp_path / "technical-library"))


def test_pre_lut_remaster_allows_nonstacked_llm_tonal_correction(tmp_path: Path) -> None:
    plan = _plan(RemasterParameters(brightness=12, contrast=4))

    _policy().validate(plan, TechnicalLibraryRepository(tmp_path / "technical-library"))
