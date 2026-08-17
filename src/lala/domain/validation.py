from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from lala.domain.errors import LalaError, PlanValidationError
from lala.domain.models import EditPlan, LutStep, validate_edit_plan
from lala.knowledge.technical import TechnicalLibraryRepository
from lala.renderers.lut import LutCatalog
from lala.text import TextEncodingError, read_utf8_lf


@dataclass(frozen=True, slots=True)
class ClientCapabilities:
    edit_plan_version: str
    remaster_engine_version: str
    lut_catalog_version: str


class LutCalibrationPolicy:
    """Validate explicit LUT atmosphere effects against active calibration evidence.

    This policy deliberately does not infer photographic intent. Hermes selects the
    LUT and values from the complete image/request context; the policy only rejects
    effects that lack the active technical evidence required by the registry.
    """

    def __init__(self, registry_path: Path) -> None:
        self.registry_path = registry_path
        self._atmospheric_evidence_id: str | None = None
        self._max_grain_amount: float | None = None
        self._max_halation: float | None = None
        self._load()

    def validate(self, plan: EditPlan, library: TechnicalLibraryRepository) -> None:
        if self._atmospheric_evidence_id is None:
            return
        active_ids = {note.technical_id for note in library.list_notes(status="active")}
        for step in plan.steps:
            if not isinstance(step, LutStep):
                continue
            parameters = step.parameters
            if parameters.grain_amount <= 0 and parameters.halation <= 0:
                continue
            evidence_ids = {evidence.skill_id for evidence in step.evidence}
            if (
                self._atmospheric_evidence_id not in evidence_ids
                or self._atmospheric_evidence_id not in active_ids
            ):
                raise PlanValidationError(
                    "grain 또는 halation은 active technical evidence "
                    f"{self._atmospheric_evidence_id}가 필요합니다."
                )
            if (
                self._max_grain_amount is not None
                and parameters.grain_amount > self._max_grain_amount
            ):
                raise PlanValidationError("grain_amount가 calibration 시작 상한을 초과했습니다.")
            if self._max_halation is not None and parameters.halation > self._max_halation:
                raise PlanValidationError("halation이 calibration 시작 상한을 초과했습니다.")

    def _load(self) -> None:
        try:
            data = yaml.safe_load(read_utf8_lf(self.registry_path)) or {}
        except (OSError, TextEncodingError, yaml.YAMLError) as exc:
            raise LalaError(
                "CALIBRATION_REGISTRY_INVALID",
                "parameter calibration registry를 읽을 수 없습니다.",
                False,
            ) from exc
        if not isinstance(data, dict):
            raise LalaError(
                "CALIBRATION_REGISTRY_INVALID",
                "parameter calibration registry 형식이 올바르지 않습니다.",
                False,
            )
        calibration = data.get("calibration")
        if not isinstance(calibration, dict):
            raise LalaError(
                "CALIBRATION_REGISTRY_INVALID",
                "calibration 형식이 올바르지 않습니다.",
                False,
            )
        policy = calibration.get("lut_parameter_selection")
        if policy is None:
            return
        if not isinstance(policy, dict):
            raise LalaError(
                "CALIBRATION_REGISTRY_INVALID",
                "lut_parameter_selection 형식이 올바르지 않습니다.",
                False,
            )
        atmosphere = policy.get("atmospheric_effects")
        if not isinstance(atmosphere, dict):
            raise LalaError(
                "CALIBRATION_REGISTRY_INVALID",
                "atmospheric_effects 형식이 올바르지 않습니다.",
                False,
            )
        evidence_id = atmosphere.get("required_technical_id")
        if not isinstance(evidence_id, str) or not evidence_id:
            raise LalaError(
                "CALIBRATION_REGISTRY_INVALID",
                "atmospheric_effects required_technical_id가 필요합니다.",
                False,
            )
        self._atmospheric_evidence_id = evidence_id
        self._max_grain_amount = _bounded_fraction(atmosphere, "max_grain_amount")
        self._max_halation = _bounded_fraction(atmosphere, "max_halation")


def _bounded_fraction(policy: dict[object, object], key: str) -> float:
    value = policy.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 1:
        raise LalaError(
            "CALIBRATION_REGISTRY_INVALID",
            f"atmospheric_effects {key}는 0부터 1 사이 숫자여야 합니다.",
            False,
        )
    return float(value)


class PlanRuntimeValidator:
    def __init__(
        self,
        catalog: LutCatalog,
        library: TechnicalLibraryRepository,
        calibration_policy: LutCalibrationPolicy | None = None,
    ) -> None:
        self.catalog = catalog
        self.library = library
        self.calibration_policy = calibration_policy

    def validate(
        self,
        value: EditPlan | dict[str, object],
        capabilities: ClientCapabilities | None = None,
    ) -> EditPlan:
        plan = validate_edit_plan(value)
        self.library.validate_plan_evidence(plan)
        for step in plan.steps:
            if isinstance(step, LutStep):
                self.catalog.resolve(step.parameters.preset)
        if self.calibration_policy is not None:
            self.calibration_policy.validate(plan, self.library)
        if capabilities:
            if capabilities.edit_plan_version != plan.schema_version:
                raise LalaError(
                    "PLAN_VERSION_UNSUPPORTED",
                    "클라이언트가 EditPlan 1.0을 지원하지 않습니다.",
                    False,
                )

            if (
                any(isinstance(step, LutStep) for step in plan.steps)
                and capabilities.lut_catalog_version != self.catalog.version
            ):
                raise LalaError(
                    "LUT_CATALOG_MISMATCH",
                    "LUT 카탈로그 버전이 서로 다릅니다.",
                    False,
                )
        return plan
