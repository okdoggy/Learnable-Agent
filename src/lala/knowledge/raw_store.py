from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import urllib.parse
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml
from pydantic import ValidationError

from lala.domain.errors import LalaError
from lala.knowledge.markdown import read_frontmatter, render_markdown
from lala.knowledge.models import RawCollection, RawMethodStep, RawScenario, RawScenarioSubmission
from lala.storage.database import Database, isoformat, utc_now
from lala.storage.workspace import ensure_within
from lala.text import TextEncodingError, normalize_utf8_lf, read_utf8_lf

TRACKING_QUERY_KEYS = {
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
    "ref",
    "source",
}


@dataclass(frozen=True, slots=True)
class RawPublishResult:
    scenario_id: str
    path: Path
    duplicate: bool
    content_sha256: str


class SourceAllowlist:
    def __init__(self, config_path: Path) -> None:
        self.config_path = config_path.resolve()

    def validate(self, source_type: str, url: str) -> str:
        canonical = canonicalize_url(url)
        parsed = urllib.parse.urlsplit(canonical)
        host = (parsed.hostname or "").lower()
        try:
            raw = yaml.safe_load(read_utf8_lf(self.config_path)) or {}
        except (OSError, TextEncodingError, yaml.YAMLError) as exc:
            raise LalaError(
                "SOURCE_POLICY_ERROR", "소스 allowlist를 읽을 수 없습니다.", False
            ) from exc
        entries = raw.get("sources", []) if isinstance(raw, dict) else []
        for entry in entries:
            if not isinstance(entry, dict) or not entry.get("enabled", False):
                continue
            types = entry.get("types", [])
            domains = [str(domain).lower() for domain in entry.get("domains", [])]
            if source_type not in types:
                continue
            if any(host == domain or host.endswith(f".{domain}") for domain in domains):
                return canonical
        raise LalaError("SOURCE_NOT_ALLOWED", "allowlist에 없는 지식 출처입니다.", False)


class RawScenarioStore:
    def __init__(
        self,
        *,
        root: Path,
        database: Database,
        sources: SourceAllowlist,
    ) -> None:
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.database = database
        self.sources = sources

    def publish(self, submission: RawScenarioSubmission | dict[str, object]) -> RawPublishResult:
        try:
            parsed = (
                submission
                if isinstance(submission, RawScenarioSubmission)
                else RawScenarioSubmission.model_validate(submission)
            )
        except ValidationError as exc:
            raise LalaError(
                "INVALID_RAW_SCENARIO", "raw 시나리오 스키마가 올바르지 않습니다.", False
            ) from exc
        self._validate_korean(parsed)
        scenario = parsed.scenario
        canonical_url = self.sources.validate(scenario.source.type, str(scenario.source.url))
        scenario_data = scenario.model_dump(mode="python")
        scenario_data["source"]["url"] = canonical_url
        scenario = RawScenario.model_validate(scenario_data)
        content_hash = _content_hash(scenario)
        scenario = scenario.model_copy(
            update={
                "collection": RawCollection(
                    collector_version=scenario.collection.collector_version,
                    content_sha256=content_hash,
                    collected_at=scenario.collection.collected_at,
                )
            }
        )
        fingerprint = _scenario_fingerprint(scenario)
        url_hash = hashlib.sha256(canonical_url.encode()).hexdigest()
        collected_kst = scenario.collection.collected_at.astimezone(ZoneInfo("Asia/Seoul"))
        directory = ensure_within(
            self.root
            / f"{collected_kst.year:04d}"
            / f"{collected_kst.month:02d}"
            / f"{collected_kst.day:02d}",
            self.root,
        )
        stem = "-".join(
            [
                _slug(scenario.source.type),
                _slug(scenario.scenario.subject),
                _slug(scenario.scenario.intent[0]),
                content_hash[:8],
            ]
        )
        path = ensure_within(directory / f"{stem}.md", self.root)
        body = _render_raw_body(parsed, canonical_url, scenario.source.accessed_at)
        document = render_markdown(scenario.model_dump(mode="json"), body)
        self.database.initialize()
        with self.database.connect() as connection:
            duplicate = connection.execute(
                """
                SELECT scenario_id, path, content_hash FROM raw_scenarios
                WHERE content_hash = ? OR (canonical_url = ? AND fingerprint = ?)
                LIMIT 1
                """,
                (content_hash, canonical_url, fingerprint),
            ).fetchone()
            if duplicate:
                return RawPublishResult(
                    scenario_id=duplicate["scenario_id"],
                    path=Path(duplicate["path"]),
                    duplicate=True,
                    content_sha256=duplicate["content_hash"],
                )
            if path.exists():
                path = ensure_within(
                    directory / f"{stem}-{scenario.scenario_id[-6:]}.md", self.root
                )
            connection.execute(
                """
                INSERT INTO raw_scenarios(
                    scenario_id, canonical_url, url_hash, content_hash,
                    fingerprint, path, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    scenario.scenario_id,
                    canonical_url,
                    url_hash,
                    content_hash,
                    fingerprint,
                    str(path),
                    isoformat(utc_now()),
                ),
            )
            try:
                _atomic_write(path, document)
            except Exception:
                raise
        return RawPublishResult(scenario.scenario_id, path, False, content_hash)

    def list_documents(self) -> list[tuple[Path, RawScenario]]:
        documents: list[tuple[Path, RawScenario]] = []
        for path in sorted(self.root.glob("*/*/*/*.md")):
            try:
                metadata, _ = read_frontmatter(path)
                scenario = RawScenario.model_validate(metadata)
            except (LalaError, ValidationError):
                continue
            if scenario.status == "validated":
                documents.append((path.resolve(), scenario))
        return documents

    def get_document(self, scenario_id: str) -> tuple[Path, RawScenario, str]:
        for path, scenario in self.list_documents():
            if scenario.scenario_id == scenario_id:
                _, body = read_frontmatter(path)
                return path, scenario, body
        raise LalaError("RAW_SCENARIO_NOT_FOUND", "raw 시나리오를 찾을 수 없습니다.", False)

    def _validate_korean(self, submission: RawScenarioSubmission) -> None:
        values = [
            submission.scenario.title_ko,
            *submission.scenario.rationale_ko,
            submission.situation_ko,
            *submission.workflow_ko,
            *submission.editing_routine_ko,
            *submission.cautions_ko,
            submission.certainty_ko,
        ]
        if any(not re.search(r"[가-힣]", value) for value in values):
            raise LalaError(
                "RAW_KOREAN_REQUIRED",
                "raw 시나리오의 한국어 필드에는 한글 설명이 필요합니다.",
                False,
            )


def canonicalize_url(url: str) -> str:
    try:
        parsed = urllib.parse.urlsplit(url.strip())
    except ValueError as exc:
        raise LalaError("INVALID_SOURCE_URL", "출처 URL이 올바르지 않습니다.", False) from exc
    if parsed.scheme.lower() != "https" or not parsed.hostname:
        raise LalaError("INVALID_SOURCE_URL", "출처 URL은 HTTPS여야 합니다.", False)
    try:
        port = parsed.port
    except ValueError as exc:
        raise LalaError(
            "INVALID_SOURCE_URL", "출처 URL의 포트가 올바르지 않습니다.", False
        ) from exc
    if parsed.username or parsed.password or port not in {None, 443}:
        raise LalaError(
            "INVALID_SOURCE_URL", "출처 URL에 허용되지 않은 인증 또는 포트가 있습니다.", False
        )
    try:
        host = parsed.hostname.encode("idna").decode("ascii").lower()
    except UnicodeError as exc:
        raise LalaError(
            "INVALID_SOURCE_URL", "출처 URL 호스트가 올바르지 않습니다.", False
        ) from exc
    path = urllib.parse.quote(urllib.parse.unquote(parsed.path or "/"), safe="/%:@-._~!$&'()*+,;=")
    query_items = []
    for key, value in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True):
        lowered = key.lower()
        if lowered.startswith("utm_") or lowered in TRACKING_QUERY_KEYS:
            continue
        query_items.append((key, value))
    query = urllib.parse.urlencode(sorted(query_items), doseq=True)
    return urllib.parse.urlunsplit(("https", host, path, query, ""))


def _content_hash(scenario: RawScenario) -> str:
    payload = {
        "title_ko": scenario.title_ko,
        "source": {
            "url": str(scenario.source.url),
            "publisher": scenario.source.publisher,
            "author": scenario.source.author,
            "published_at": scenario.source.published_at.isoformat()
            if scenario.source.published_at
            else None,
        },
        "device": scenario.device.model_dump(mode="json"),
        "scenario": scenario.scenario.model_dump(mode="json"),
        "method": scenario.method.model_dump(mode="json"),
        "rationale_ko": scenario.rationale_ko,
    }
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def _scenario_fingerprint(scenario: RawScenario) -> str:
    payload = {
        "subject": scenario.scenario.subject,
        "condition": sorted(scenario.scenario.condition),
        "intent": sorted(scenario.scenario.intent),
        "method": [
            {
                "tool": step.tool.casefold(),
                "parameter": step.parameter.casefold(),
                "value": step.value,
                "reported_as": step.reported_as,
            }
            for step in scenario.method.steps
        ],
    }
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def _render_raw_body(
    submission: RawScenarioSubmission, canonical_url: str, accessed_at: datetime
) -> str:
    scenario = submission.scenario
    rationale = "\n".join(f"- {item}" for item in scenario.rationale_ko)
    workflow = "\n".join(f"{index}. {item}" for index, item in enumerate(submission.workflow_ko, 1))
    starting_values = "\n".join(f"- {_render_method_step(step)}" for step in scenario.method.steps)
    editing_routine = "\n".join(f"- {item}" for item in submission.editing_routine_ko)
    cautions = "\n".join(f"- {item}" for item in submission.cautions_ko)
    return f"""# {scenario.title_ko}

이 문서는 하나의 촬영·보정 시나리오만 다룬다.

## 상황

{submission.situation_ko}

## 촬영/작업 순서

{workflow}

## 추천 시작값 / 조작값

{starting_values}

## 보정 루틴

{editing_routine}

## 주의할 점

{cautions}

## 확실성과 근거

{rationale}

{submission.certainty_ko}

## 출처

- 원문 URL: {canonical_url}
- 접근일: {accessed_at.astimezone(UTC).date().isoformat()}
"""


def _render_method_step(step: RawMethodStep) -> str:
    if step.reported_as == "qualitative":
        rendered_value = "원문 정성 표현(수치 추정 없음)"
    else:
        rendered_value = str(step.value)
        if step.unit:
            rendered_value += f" {step.unit}"
    return f"{step.tool} / {step.parameter}: {rendered_value}"


def _slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized[:48] or "source"


def _atomic_write(path: Path, content: str) -> None:
    try:
        content = normalize_utf8_lf(content)
    except TextEncodingError as exc:
        raise LalaError(
            "INVALID_TEXT_ENCODING",
            "문서에 올바르지 않은 UTF-8 텍스트가 포함되어 있습니다.",
            False,
        ) from exc
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        try:
            directory_descriptor = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(directory_descriptor)
            finally:
                os.close(directory_descriptor)
        except OSError:
            pass
    finally:
        temporary.unlink(missing_ok=True)
