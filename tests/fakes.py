from __future__ import annotations

from pathlib import Path

from lala.domain.models import (
    EditPlan,
    GenerateAIParameters,
    GenerateAIStep,
    LutParameters,
    LutStep,
)
from lala.renderers.inspection import ImageInspection


class StaticLutPlanner:
    """A fixed LLM response stand-in; it performs no prompt interpretation."""

    def plan(
        self,
        *,
        request_id: str,
        prompt: str,
        image_path: Path,
        inspection: ImageInspection,
    ) -> EditPlan:
        del prompt, image_path, inspection
        return EditPlan(
            request_id=request_id,
            summary_ko="원본 구도를 유지하며 어두운 영역을 자연스럽게 보정합니다.",
            steps=[
                LutStep(
                    order=1,
                    tool="lut",
                    parameters=LutParameters(
                        preset="documentary", lut_intensity=0.65, grain_amount=0, halation=0
                    ),
                    reason_ko="새 픽셀 생성 없이 전역 톤과 색감을 보수적으로 정리합니다.",
                    evidence=[],
                )
            ],
            overall_reason_ko="결정론적 LUT 보정으로 요청을 충족할 수 있습니다.",
            confidence=0.6,
            warnings_ko=["근거 technical 문서 없음"],
        )


StaticRemasterPlanner = StaticLutPlanner


class StaticGeneratePlanner:
    """A fixed Generate AI LLM response stand-in for execution tests."""

    def plan(
        self,
        *,
        request_id: str,
        prompt: str,
        image_path: Path,
        inspection: ImageInspection,
    ) -> EditPlan:
        del image_path, inspection
        return EditPlan(
            request_id=request_id,
            summary_ko="요청한 생성적 변경만 적용하고 나머지는 유지합니다.",
            steps=[
                GenerateAIStep(
                    order=1,
                    tool="generate_ai",
                    parameters=GenerateAIParameters(
                        use_case="precise-object-edit",
                        prompt=prompt,
                        constraints=["피사체와 구도를 유지"],
                        avoid=["요청하지 않은 객체", "텍스트", "워터마크"],
                    ),
                    reason_ko="요청을 충족하려면 지정 영역에 새 픽셀 생성이 필요합니다.",
                    evidence=[],
                )
            ],
            overall_reason_ko="결정론적 보정만으로는 생성적 변경을 만들 수 없습니다.",
            confidence=0.7,
            warnings_ko=["근거 technical 문서 없음"],
        )
