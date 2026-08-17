from __future__ import annotations

import pytest

from lala.domain.errors import LalaError
from lala.domain.models import EditPlan, RemasterParameters, RemasterStep
from lala.domain.validation import ClientCapabilities, PlanRuntimeValidator
from lala.knowledge.technical import TechnicalLibraryRepository
from lala.renderers.lut import LutCatalog


def _plan() -> EditPlan:
    return EditPlan(
        request_id="req_remaster_contract",
        summary_ko="기본 보정과 에지 마무리를 적용합니다.",
        steps=[
            RemasterStep(
                order=1,
                tool="remaster",
                parameters=RemasterParameters(sharpen_amount=0.8),
                reason_ko="전역 에지를 절제해 정리합니다.",
                evidence=[],
            )
        ],
        overall_reason_ko="결정론적 기본 보정으로 충분합니다.",
        confidence=0.7,
    )


def test_remaster_plan_requires_client_remaster_engine_v11(settings) -> None:
    catalog = LutCatalog(settings.lut_manifest_path)
    validator = PlanRuntimeValidator(
        catalog, TechnicalLibraryRepository(settings.technical_library_dir)
    )
    legacy = ClientCapabilities(
        edit_plan_version="1.0",
        remaster_engine_version="1.0",
        lut_catalog_version=catalog.version,
    )

    with pytest.raises(LalaError, match="Remaster 엔진") as captured:
        validator.validate(_plan(), legacy)

    assert captured.value.code == "REMASTER_ENGINE_UNSUPPORTED"


def test_remaster_plan_accepts_client_remaster_engine_v11(settings) -> None:
    catalog = LutCatalog(settings.lut_manifest_path)
    validator = PlanRuntimeValidator(
        catalog, TechnicalLibraryRepository(settings.technical_library_dir)
    )
    capabilities = ClientCapabilities(
        edit_plan_version="1.0",
        remaster_engine_version="1.1",
        lut_catalog_version=catalog.version,
    )

    assert validator.validate(_plan(), capabilities).steps[0].tool == "remaster"
