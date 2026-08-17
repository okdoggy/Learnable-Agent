from __future__ import annotations

from dataclasses import dataclass

from lala.domain.errors import LalaError
from lala.domain.models import EditPlan, LutStep, validate_edit_plan
from lala.knowledge.technical import TechnicalLibraryRepository
from lala.renderers.lut import LutCatalog


@dataclass(frozen=True, slots=True)
class ClientCapabilities:
    edit_plan_version: str
    remaster_engine_version: str
    lut_catalog_version: str


class PlanRuntimeValidator:
    def __init__(self, catalog: LutCatalog, library: TechnicalLibraryRepository) -> None:
        self.catalog = catalog
        self.library = library

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
