from __future__ import annotations

import re
import threading
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from pydantic import ValidationError

from lala.domain.errors import LalaError, PlanValidationError
from lala.domain.models import EditPlan, SkillEvidence
from lala.knowledge.markdown import read_frontmatter, render_markdown
from lala.knowledge.models import TechnicalNoteFrontmatter, TechnicalNoteSubmission
from lala.knowledge.raw_store import RawScenarioStore, _atomic_write
from lala.storage.workspace import ensure_within

NUMBERED_NOTE = re.compile(r"^(?P<number>\d{3})-(?P<slug>[a-z0-9][a-z0-9-]*)\.md$")


@dataclass(frozen=True, slots=True)
class TechnicalNote:
    number: int
    technical_id: str
    title_ko: str
    summary_ko: str
    version: str
    status: str
    supported_tools: tuple[str, ...]
    confidence: float
    raw_scenario_ids: tuple[str, ...]
    path: Path
    content: str

    def as_evidence(self) -> SkillEvidence:
        return SkillEvidence(skill_id=self.technical_id, version=self.version)


@dataclass(frozen=True, slots=True)
class TechnicalPublishResult:
    technical_id: str
    number: int
    version: str
    status: str
    path: Path
    changed: bool


class TechnicalLibraryRepository:
    """Validate and persist LLM-authored notes without making semantic decisions."""

    def __init__(self, root: Path, raw_store: RawScenarioStore | None = None) -> None:
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.raw_store = raw_store
        self._write_lock = threading.Lock()

    def list_notes(self, *, status: str | None = None) -> list[TechnicalNote]:
        notes: list[TechnicalNote] = []
        for path in sorted(self.root.glob("[0-9][0-9][0-9]-*.md")):
            try:
                metadata, body = read_frontmatter(path)
                frontmatter = TechnicalNoteFrontmatter.model_validate(metadata)
            except (LalaError, ValidationError, OSError, ValueError):
                continue
            match = NUMBERED_NOTE.fullmatch(path.name)
            if match is None or int(match.group("number")) != frontmatter.number:
                continue
            if match.group("slug") != frontmatter.technical_id:
                continue
            if status is not None and frontmatter.status != status:
                continue
            notes.append(
                TechnicalNote(
                    number=frontmatter.number,
                    technical_id=frontmatter.technical_id,
                    title_ko=frontmatter.title_ko,
                    summary_ko=frontmatter.summary_ko,
                    version=frontmatter.version,
                    status=frontmatter.status,
                    supported_tools=tuple(frontmatter.supported_tools),
                    confidence=frontmatter.confidence,
                    raw_scenario_ids=tuple(frontmatter.raw_scenario_ids),
                    path=path.resolve(),
                    content=body,
                )
            )
        return notes

    def get_note(self, technical_id: str) -> TechnicalNote:
        for note in self.list_notes():
            if note.technical_id == technical_id:
                return note
        raise LalaError(
            "TECHNICAL_NOTE_NOT_FOUND", "technical library 문서를 찾을 수 없습니다.", False
        )

    def publish(
        self, submission: TechnicalNoteSubmission | dict[str, object]
    ) -> TechnicalPublishResult:
        if self.raw_store is None:
            raise LalaError(
                "TECHNICAL_LIBRARY_READ_ONLY",
                "이 프로세스에서는 technical library를 쓸 수 없습니다.",
                False,
            )
        try:
            parsed = (
                submission
                if isinstance(submission, TechnicalNoteSubmission)
                else TechnicalNoteSubmission.model_validate(submission)
            )
        except ValidationError as exc:
            raise LalaError(
                "INVALID_TECHNICAL_NOTE",
                "technical library 문서 스키마가 올바르지 않습니다.",
                False,
            ) from exc
        self._validate_korean(parsed)
        raw_documents = [
            self.raw_store.get_document(scenario_id) for scenario_id in parsed.raw_scenario_ids
        ]
        source_urls = sorted({str(scenario.source.url) for _, scenario, _ in raw_documents})
        if parsed.status == "active" and len(source_urls) < 2:
            raise LalaError(
                "INSUFFICIENT_REPEATED_EVIDENCE",
                "active 기술에는 서로 다른 raw 출처가 두 개 이상 필요합니다.",
                False,
            )
        body = _render_note_body(parsed)
        with self._write_lock:
            existing = next(
                (note for note in self.list_notes() if note.technical_id == parsed.technical_id),
                None,
            )
            if existing and _is_unchanged(existing, parsed, body):
                return TechnicalPublishResult(
                    technical_id=existing.technical_id,
                    number=existing.number,
                    version=existing.version,
                    status=existing.status,
                    path=existing.path,
                    changed=False,
                )
            number = existing.number if existing else self._next_number()
            version = _next_version(existing.version if existing else None, parsed.status)
            frontmatter = TechnicalNoteFrontmatter(
                number=number,
                technical_id=parsed.technical_id,
                title_ko=parsed.title_ko,
                summary_ko=parsed.summary_ko,
                version=version,
                status=parsed.status,
                supported_tools=parsed.supported_tools,
                confidence=parsed.confidence,
                raw_scenario_ids=sorted(set(parsed.raw_scenario_ids)),
                source_urls=source_urls,
                reviewed_at=datetime.now(ZoneInfo("Asia/Seoul")).date(),
            )
            path = (
                existing.path
                if existing
                else ensure_within(self.root / f"{number:03d}-{parsed.technical_id}.md", self.root)
            )
            _atomic_write(path, render_markdown(frontmatter.model_dump(mode="json"), body))
            return TechnicalPublishResult(
                technical_id=parsed.technical_id,
                number=number,
                version=version,
                status=parsed.status,
                path=path,
                changed=True,
            )

    def validate_plan_evidence(self, plan: EditPlan) -> None:
        active = {
            (note.technical_id, note.version): note for note in self.list_notes(status="active")
        }
        for step in plan.steps:
            for evidence in step.evidence:
                note = active.get((evidence.skill_id, evidence.version))
                if note is None or step.tool not in note.supported_tools:
                    raise PlanValidationError(
                        "활성 technical library 문서가 아닌 근거가 포함되었습니다: "
                        f"{evidence.skill_id} v{evidence.version}"
                    )

    def _next_number(self) -> int:
        numbers = [note.number for note in self.list_notes()]
        number = max(numbers, default=0) + 1
        if number > 999:
            raise LalaError(
                "TECHNICAL_LIBRARY_FULL", "technical library 번호 공간이 가득 찼습니다.", False
            )
        return number

    @staticmethod
    def _validate_korean(submission: TechnicalNoteSubmission) -> None:
        values = [
            submission.title_ko,
            submission.summary_ko,
            *submission.applicability_ko,
            *submission.procedure_ko,
            *submission.parameter_guidance_ko,
            *submission.rationale_ko,
            *submission.cautions_ko,
            *submission.conflicts_ko,
        ]
        if any(not re.search(r"[가-힣]", value) for value in values):
            raise LalaError(
                "TECHNICAL_KOREAN_REQUIRED",
                "technical library의 설명 필드는 한국어로 작성해야 합니다.",
                False,
            )


def _render_note_body(submission: TechnicalNoteSubmission) -> str:
    return "\n".join(
        [
            f"# {submission.title_ko}",
            "",
            submission.summary_ko,
            "",
            "## 적용 조건",
            "",
            *[f"- {item}" for item in submission.applicability_ko],
            "",
            "## 기술 절차",
            "",
            *[f"{index}. {item}" for index, item in enumerate(submission.procedure_ko, 1)],
            "",
            "## 파라미터 가이드",
            "",
            *[f"- {item}" for item in submission.parameter_guidance_ko],
            "",
            "## 판단 근거",
            "",
            *[f"- {item}" for item in submission.rationale_ko],
            "",
            "## 주의사항",
            "",
            *[f"- {item}" for item in submission.cautions_ko],
            "",
            "## 충돌 및 예외",
            "",
            *(
                [f"- {item}" for item in submission.conflicts_ko]
                if submission.conflicts_ko
                else ["- 확인된 충돌 없음"]
            ),
            "",
            "## raw 근거",
            "",
            *[f"- {scenario_id}" for scenario_id in submission.raw_scenario_ids],
        ]
    )


def _is_unchanged(existing: TechnicalNote, submission: TechnicalNoteSubmission, body: str) -> bool:
    return (
        existing.title_ko == submission.title_ko
        and existing.summary_ko == submission.summary_ko
        and existing.status == submission.status
        and existing.supported_tools == tuple(submission.supported_tools)
        and existing.confidence == submission.confidence
        and set(existing.raw_scenario_ids) == set(submission.raw_scenario_ids)
        and existing.content.strip() == body.strip()
    )


def _next_version(previous: str | None, status: str) -> str:
    if previous is None:
        return "1.0.0" if status == "active" else "0.1.0"
    major, minor, patch = (int(value) for value in previous.split("."))
    if status == "active" and major == 0:
        return "1.0.0"
    return f"{major}.{minor}.{patch + 1}"
