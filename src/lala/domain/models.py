from __future__ import annotations

from typing import Annotated, Literal, TypeAlias

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, TypeAdapter, model_validator

StrictId = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True, min_length=3, max_length=128, pattern=r"^[a-zA-Z0-9._-]+$"
    ),
]
KoreanText = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=4000,
        pattern=r"[가-힣]",
    ),
]


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class SkillEvidence(StrictModel):
    skill_id: StrictId
    version: Annotated[
        str,
        StringConstraints(pattern=r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$"),
    ]


class RemasterParameters(StrictModel):
    brightness: int = Field(default=0, ge=-100, le=100)
    contrast: int = Field(default=0, ge=-100, le=100)
    highlights: int = Field(default=0, ge=-100, le=100)
    shadows: int = Field(default=0, ge=-100, le=100)
    saturation: int = Field(default=0, ge=-100, le=100)
    temperature: int = Field(default=0, ge=-100, le=100)
    tint: int = Field(default=0, ge=-100, le=100)
    sharpness: int = Field(default=0, ge=0, le=100)
    denoise: int = Field(default=0, ge=0, le=100)
    vignette: int = Field(default=0, ge=-100, le=100)


class LutParameters(StrictModel):
    preset: StrictId
    lut_intensity: float = Field(default=0.65, ge=0.0, le=1.0)
    skin_protection: bool = True
    grain_amount: float = Field(default=0.0, ge=0.0, le=1.0)
    halation: float = Field(default=0.0, ge=0.0, le=1.0)
    use_aces: bool = True


GenerateUseCase = Literal[
    "text-localization",
    "identity-preserve",
    "precise-object-edit",
    "lighting-weather",
    "background-extraction",
    "style-transfer",
    "compositing",
    "sketch-to-render",
]


class GenerateAIParameters(StrictModel):
    operation: Literal["edit"] = "edit"
    use_case: GenerateUseCase
    execution_mode: Literal["openai-image-api"] = "openai-image-api"
    prompt: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=16000)]
    constraints: list[
        Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=500)]
    ] = Field(default_factory=list, max_length=32)
    avoid: list[
        Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=500)]
    ] = Field(default_factory=list, max_length=32)
    output_format: Literal["png"] = "png"


class StepBase(StrictModel):
    order: int = Field(ge=1, le=16)
    reason_ko: KoreanText
    evidence: list[SkillEvidence] = Field(default_factory=list, max_length=32)


class RemasterStep(StepBase):
    tool: Literal["remaster"]
    parameters: RemasterParameters


class LutStep(StepBase):
    tool: Literal["lut"]
    parameters: LutParameters


class GenerateAIStep(StepBase):
    tool: Literal["generate_ai"]
    parameters: GenerateAIParameters


EditStep: TypeAlias = Annotated[LutStep | GenerateAIStep, Field(discriminator="tool")]


class EditPlan(StrictModel):
    schema_version: Literal["1.0"] = "1.0"
    request_id: StrictId
    summary_ko: KoreanText
    steps: list[EditStep] = Field(min_length=1, max_length=16)
    overall_reason_ko: KoreanText
    confidence: float = Field(ge=0, le=1)
    warnings_ko: list[
        Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=1000)]
    ] = Field(default_factory=list, max_length=32)

    @model_validator(mode="after")
    def validate_step_composition(self) -> EditPlan:
        orders = [step.order for step in self.steps]
        if orders != list(range(1, len(self.steps) + 1)):
            raise ValueError("steps must be ordered contiguously from 1")
        generate_steps = [step for step in self.steps if step.tool == "generate_ai"]
        if generate_steps and len(self.steps) != 1:
            raise ValueError("generate_ai must be the only v1 step")
        return self


EDIT_PLAN_ADAPTER = TypeAdapter(EditPlan)


def validate_edit_plan(value: EditPlan | dict[str, object]) -> EditPlan:
    if isinstance(value, EditPlan):
        return value
    return EDIT_PLAN_ADAPTER.validate_python(value, strict=True)
