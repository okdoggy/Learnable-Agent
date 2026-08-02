from __future__ import annotations

import math
from datetime import date
from typing import Annotated, Literal
from zoneinfo import ZoneInfo

from pydantic import (
    AnyHttpUrl,
    AwareDatetime,
    BaseModel,
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
    StringConstraints,
    model_validator,
)

NonEmpty = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=1000)]
Slug = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True, min_length=1, max_length=128, pattern=r"^[a-z0-9][a-z0-9-]*$"
    ),
]


class KnowledgeModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class RawSource(KnowledgeModel):
    type: Literal["official", "magazine", "youtube", "social", "community", "other"]
    publisher: NonEmpty
    author: NonEmpty = "unknown"
    url: AnyHttpUrl
    published_at: date | None = None
    accessed_at: AwareDatetime
    original_language: Annotated[str, StringConstraints(pattern=r"^[a-z]{2,3}(-[A-Za-z0-9]+)*$")]


class RawDevice(KnowledgeModel):
    capture_device: NonEmpty | None = None
    editing_device: NonEmpty | None = None
    software: NonEmpty


class RawScenarioTaxonomy(KnowledgeModel):
    subject: Slug
    condition: list[Slug] = Field(min_length=1, max_length=32)
    intent: list[Slug] = Field(min_length=1, max_length=32)


class RawMethodStep(KnowledgeModel):
    tool: NonEmpty
    parameter: NonEmpty
    value: StrictInt | StrictFloat | NonEmpty | None = None
    unit: NonEmpty | None = None
    reported_as: Literal["exact", "qualitative"]

    @model_validator(mode="after")
    def qualitative_values_are_not_invented(self) -> RawMethodStep:
        if isinstance(self.value, bool) or (
            isinstance(self.value, float) and not math.isfinite(self.value)
        ):
            raise ValueError("method values must be finite numbers or text")
        if self.reported_as == "qualitative" and self.value is not None:
            raise ValueError("qualitative steps must use value=null")
        if self.reported_as == "exact" and self.value is None:
            raise ValueError("exact steps require a value")
        return self


class RawMethod(KnowledgeModel):
    steps: list[RawMethodStep] = Field(min_length=1, max_length=64)


class RawCollection(KnowledgeModel):
    collector_version: Annotated[str, StringConstraints(pattern=r"^\d+\.\d+\.\d+$")]
    content_sha256: Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{64}$")] | None = None
    collected_at: AwareDatetime


class RawScenario(KnowledgeModel):
    schema_version: Literal["1.0"] = "1.0"
    scenario_id: Annotated[
        str,
        StringConstraints(pattern=r"^raw-[0-9]{8}-[a-z0-9]{6,32}$"),
    ]
    title_ko: NonEmpty
    status: Literal["validated"] = "validated"
    source: RawSource
    device: RawDevice
    scenario: RawScenarioTaxonomy
    method: RawMethod
    rationale_ko: list[NonEmpty] = Field(min_length=1, max_length=32)
    collection: RawCollection

    @model_validator(mode="after")
    def validate_timeline(self) -> RawScenario:
        if self.source.accessed_at > self.collection.collected_at:
            raise ValueError("source access must not be later than collection")
        if (
            self.source.published_at is not None
            and self.source.published_at > self.source.accessed_at.date()
        ):
            raise ValueError("source publication must not be later than access")
        scenario_date = self.scenario_id.split("-", 2)[1]
        collected_date = self.collection.collected_at.astimezone(ZoneInfo("Asia/Seoul")).strftime(
            "%Y%m%d"
        )
        if scenario_date != collected_date:
            raise ValueError("scenario ID date must match the Asia/Seoul collection date")
        return self


class RawScenarioSubmission(KnowledgeModel):
    scenario: RawScenario
    situation_ko: NonEmpty
    workflow_ko: list[NonEmpty] = Field(min_length=1, max_length=64)
    editing_routine_ko: list[NonEmpty] = Field(min_length=1, max_length=64)
    cautions_ko: list[NonEmpty] = Field(min_length=1, max_length=32)
    certainty_ko: NonEmpty


class TechnicalNoteFrontmatter(KnowledgeModel):
    schema_version: Literal["1.0"] = "1.0"
    number: int = Field(ge=1, le=999)
    technical_id: Slug
    title_ko: NonEmpty
    summary_ko: NonEmpty
    version: Annotated[str, StringConstraints(pattern=r"^\d+\.\d+\.\d+$")]
    status: Literal["active", "candidate", "deprecated"]
    supported_tools: list[Literal["remaster", "lut", "generate_ai"]] = Field(
        min_length=1, max_length=3
    )
    confidence: float = Field(ge=0, le=1)
    raw_scenario_ids: list[
        Annotated[str, StringConstraints(pattern=r"^raw-[0-9]{8}-[a-z0-9]{6,32}$")]
    ] = Field(min_length=1, max_length=128)
    source_urls: list[AnyHttpUrl] = Field(min_length=1, max_length=128)
    reviewed_at: date
    created_by: Literal["hermes-llm"] = "hermes-llm"

    @model_validator(mode="after")
    def active_notes_need_repeated_evidence(self) -> TechnicalNoteFrontmatter:
        if self.status == "active" and len(set(self.raw_scenario_ids)) < 2:
            raise ValueError("active technical notes require at least two raw scenarios")
        if self.status == "active" and len({str(url) for url in self.source_urls}) < 2:
            raise ValueError("active technical notes require at least two source URLs")
        return self


class TechnicalNoteSubmission(KnowledgeModel):
    technical_id: Slug
    title_ko: NonEmpty
    summary_ko: NonEmpty
    status: Literal["active", "candidate", "deprecated"]
    supported_tools: list[Literal["remaster", "lut", "generate_ai"]] = Field(
        min_length=1, max_length=3
    )
    confidence: float = Field(ge=0, le=1)
    raw_scenario_ids: list[
        Annotated[str, StringConstraints(pattern=r"^raw-[0-9]{8}-[a-z0-9]{6,32}$")]
    ] = Field(min_length=1, max_length=128)
    applicability_ko: list[NonEmpty] = Field(min_length=1, max_length=64)
    procedure_ko: list[NonEmpty] = Field(min_length=1, max_length=64)
    parameter_guidance_ko: list[NonEmpty] = Field(min_length=1, max_length=64)
    rationale_ko: list[NonEmpty] = Field(min_length=1, max_length=64)
    cautions_ko: list[NonEmpty] = Field(min_length=1, max_length=64)
    conflicts_ko: list[NonEmpty] = Field(default_factory=list, max_length=64)
