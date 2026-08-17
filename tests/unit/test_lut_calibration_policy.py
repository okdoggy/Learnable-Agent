from __future__ import annotations

from pathlib import Path

import pytest

from lala.domain.errors import PlanValidationError
from lala.domain.models import EditPlan, LutParameters, LutStep, SkillEvidence
from lala.domain.validation import LutCalibrationPolicy
from lala.knowledge.markdown import render_markdown
from lala.knowledge.technical import TechnicalLibraryRepository

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _plan(*, grain_amount: float, halation: float, evidence: list[SkillEvidence]) -> EditPlan:
    return EditPlan(
        request_id="req_lut_policy",
        summary_ko="대기 효과를 검토한 LUT 보정입니다.",
        steps=[
            LutStep(
                order=1,
                tool="lut",
                parameters=LutParameters(
                    preset="documentary",
                    grain_amount=grain_amount,
                    halation=halation,
                ),
                reason_ko="원본의 핵심 가독성을 유지하며 전역 보정을 적용합니다.",
                evidence=evidence,
            )
        ],
        overall_reason_ko="active technical 근거와 calibration 정책을 따릅니다.",
        confidence=0.7,
    )


def _write_atmosphere_note(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "008-restrained-atmospheric-softness.md").write_text(
        render_markdown(
            {
                "schema_version": "1.0",
                "number": 8,
                "technical_id": "restrained-atmospheric-softness",
                "title_ko": "절제된 대기감",
                "summary_ko": "가독성을 지키며 약한 대기 효과를 적용합니다.",
                "version": "1.0.0",
                "status": "active",
                "supported_tools": ["lut"],
                "confidence": 0.9,
                "raw_scenario_ids": ["raw-20260817-atmospherea", "raw-20260817-atmosphereb"],
                "source_urls": ["https://example.com/a", "https://example.com/b"],
                "reviewed_at": "2026-08-17",
                "created_by": "hermes-llm",
            },
            "# 절제된 대기감\n",
        ),
        encoding="utf-8",
    )


def _policy() -> LutCalibrationPolicy:
    return LutCalibrationPolicy(PROJECT_ROOT / "config" / "parameter-registry.yaml")


def test_lut_defaults_start_without_atmospheric_effects() -> None:
    parameters = LutParameters(preset="documentary")

    assert parameters.lut_intensity == 0.65
    assert parameters.grain_amount == 0
    assert parameters.halation == 0


def test_atmospheric_effect_requires_active_technical_evidence(tmp_path: Path) -> None:
    library_root = tmp_path / "technical-library"
    _write_atmosphere_note(library_root)
    policy = _policy()

    with pytest.raises(PlanValidationError, match="restrained-atmospheric-softness"):
        policy.validate(
            _plan(grain_amount=0.1, halation=0, evidence=[]),
            TechnicalLibraryRepository(library_root),
        )


def test_atmospheric_effect_rejects_values_above_calibrated_start_cap(tmp_path: Path) -> None:
    library_root = tmp_path / "technical-library"
    _write_atmosphere_note(library_root)
    policy = _policy()
    evidence = [SkillEvidence(skill_id="restrained-atmospheric-softness", version="1.0.0")]

    with pytest.raises(PlanValidationError, match="calibration 시작 상한"):
        policy.validate(
            _plan(grain_amount=0.2, halation=0, evidence=evidence),
            TechnicalLibraryRepository(library_root),
        )


def test_atmospheric_effect_accepts_evidence_and_calibrated_start_range(tmp_path: Path) -> None:
    library_root = tmp_path / "technical-library"
    _write_atmosphere_note(library_root)
    policy = _policy()
    evidence = [SkillEvidence(skill_id="restrained-atmospheric-softness", version="1.0.0")]

    policy.validate(
        _plan(grain_amount=0.1, halation=0.1, evidence=evidence),
        TechnicalLibraryRepository(library_root),
    )
