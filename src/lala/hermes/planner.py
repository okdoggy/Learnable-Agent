from __future__ import annotations

import base64
import hashlib
import json
import re
import time
from pathlib import Path
from typing import Protocol

import httpx
from pydantic import ValidationError

from lala.config import Settings
from lala.domain.errors import AgentTimeoutError, LalaError, PlanValidationError
from lala.domain.models import EditPlan
from lala.knowledge.technical import TechnicalLibraryRepository
from lala.observability.audit import audit_event
from lala.renderers.inspection import ImageInspection
from lala.resilience import CircuitBreaker
from lala.text import TextEncodingError, read_utf8_lf


class Planner(Protocol):
    def plan(
        self,
        *,
        request_id: str,
        prompt: str,
        image_path: Path,
        inspection: ImageInspection,
    ) -> EditPlan: ...


class HermesResponsesPlanner:
    """Delegate every semantic editing decision to the Hermes LLM."""

    def __init__(
        self,
        settings: Settings,
        library: TechnicalLibraryRepository,
        client: httpx.Client | None = None,
    ) -> None:
        self.settings = settings
        self.library = library
        self.client = client or httpx.Client(timeout=settings.hermes_timeout_seconds)
        self.circuit_breaker = CircuitBreaker(
            failure_threshold=settings.hermes_circuit_failures,
            recovery_seconds=settings.hermes_circuit_recovery_seconds,
        )

    def plan(
        self,
        *,
        request_id: str,
        prompt: str,
        image_path: Path,
        inspection: ImageInspection,
    ) -> EditPlan:
        prompt_template = _read_utf8_prompt(self.settings.planner_prompt_path)
        prompt_sha256 = hashlib.sha256(prompt_template.encode("utf-8")).hexdigest()
        audit_event(
            "planner_prompt_loaded",
            request_id=request_id,
            planner_prompt_sha256=prompt_sha256,
        )
        image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")
        schema = EditPlan.model_json_schema()
        instructions = (
            prompt_template
            + "\n\n## 출력 계약\n"
            + "최종 응답은 설명이나 Markdown fence 없이 다음 JSON Schema를 만족하는 객체 하나다.\n"
            + json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
        )
        active_notes = [
            {
                "technical_id": note.technical_id,
                "version": note.version,
                "title_ko": note.title_ko,
                "summary_ko": note.summary_ko,
                "supported_tools": list(note.supported_tools),
                "content_ko": note.content,
            }
            for note in self.library.list_notes(status="active")
        ]
        input_text = "\n".join(
            [
                f"request_id={request_id}",
                f"planner_prompt_sha256={prompt_sha256}",
                f"사용자 요청: {prompt}",
                f"이미지 정량 분석: {inspection.model_dump_json()}",
                "실제로 읽을 수 있도록 제공된 active technical library 문서 전문:",
                json.dumps(active_notes, ensure_ascii=False, separators=(",", ":")),
                (
                    "이미지와 전체 문맥을 의미적으로 해석하라. 단어 포함 여부, 정규식, "
                    "동의어 표 또는 점수 규칙으로 도구나 파라미터를 고르지 마라. 위에 전문이 "
                    "제공된 active 문서만 근거로 선택하고 ID와 version을 정확히 기록하라."
                ),
            ]
        )
        payload: dict[str, object] = {
            "model": self.settings.hermes_model,
            "instructions": instructions,
            "input": [
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": input_text},
                        {
                            "type": "input_image",
                            "image_url": f"data:image/png;base64,{image_data}",
                        },
                    ],
                }
            ],
            "store": True,
        }
        headers = {"Authorization": f"Bearer {self.settings.hermes_api_key}"}
        previous_response_id: str | None = None
        last_error = ""
        for attempt in range(2):
            if attempt:
                payload = {
                    "model": self.settings.hermes_model,
                    "instructions": instructions,
                    "input": (
                        "이전 출력의 의미 판단은 유지하고 다음 계약 오류만 교정하라. "
                        "JSON 객체만 다시 출력하라: " + last_error[:2000]
                    ),
                    "store": False,
                    "previous_response_id": previous_response_id,
                }
            response = self._post(payload, headers)
            data = response.json()
            previous_response_id = str(data.get("id", "")) or None
            try:
                text = _response_output_text(data)
                candidate = _extract_json(text)
                plan = EditPlan.model_validate_json(candidate, strict=True)
                if plan.request_id != request_id:
                    raise ValueError("request_id mismatch")
                self.library.validate_plan_evidence(plan)
                return plan
            except (ValidationError, ValueError, PlanValidationError) as exc:
                last_error = str(exc)
        raise PlanValidationError(
            "Hermes 출력이 1회 교정 후에도 EditPlan 계약을 만족하지 못했습니다."
        )

    def _post(self, payload: dict[str, object], headers: dict[str, str]) -> httpx.Response:
        self.circuit_breaker.require_available()
        last_error: LalaError | None = None
        attempts = min(max(1, self.settings.hermes_max_attempts), 5)
        for attempt in range(attempts):
            try:
                response = self.client.post(
                    f"{self.settings.hermes_base_url}/v1/responses",
                    headers=headers,
                    json=payload,
                )
                if response.status_code == 429:
                    last_error = LalaError(
                        "RATE_LIMITED", "추천 Agent 요청 한도에 도달했습니다.", True
                    )
                elif response.status_code >= 500:
                    last_error = LalaError(
                        "AGENT_ERROR", "추천 Agent가 일시적인 오류를 반환했습니다.", True
                    )
                else:
                    response.raise_for_status()
                    self.circuit_breaker.success()
                    return response
            except httpx.TimeoutException:
                last_error = AgentTimeoutError()
            except httpx.HTTPStatusError as exc:
                self.circuit_breaker.failure()
                raise LalaError(
                    "AGENT_ERROR",
                    "추천 Agent가 요청을 거부했습니다.",
                    False,
                    str(exc),
                ) from exc
            except httpx.HTTPError as exc:
                last_error = LalaError(
                    "AGENT_ERROR", "추천 Agent 호출에 실패했습니다.", True, str(exc)
                )
            if attempt + 1 < attempts:
                time.sleep(min(0.25 * (2**attempt), 1.0))
        self.circuit_breaker.failure()
        if last_error is None:  # pragma: no cover - defensive guard
            last_error = LalaError("AGENT_ERROR", "추천 Agent 호출에 실패했습니다.", True)
        raise last_error


def build_planner(settings: Settings) -> Planner:
    if not settings.hermes_api_key:
        raise LalaError("CONFIG_ERROR", "HERMES_API_KEY가 설정되지 않았습니다.", False)
    library = TechnicalLibraryRepository(settings.technical_library_dir)
    return HermesResponsesPlanner(settings, library)


def _read_utf8_prompt(path: Path) -> str:
    try:
        content = read_utf8_lf(path)
    except (OSError, TextEncodingError) as exc:
        raise LalaError(
            "PROMPT_LOAD_FAILED", "Hermes planner 프롬프트를 UTF-8로 읽을 수 없습니다.", False
        ) from exc
    if not content.strip() or "\ufffd" in content:
        raise LalaError("PROMPT_LOAD_FAILED", "Hermes planner 프롬프트가 비어 있습니다.", False)
    return content.strip()


def _response_output_text(data: dict[str, object]) -> str:
    texts: list[str] = []
    output = data.get("output")
    if isinstance(output, list):
        for item in output:
            if not isinstance(item, dict) or item.get("type") != "message":
                continue
            content = item.get("content")
            if not isinstance(content, list):
                continue
            for part in content:
                if isinstance(part, dict) and part.get("type") == "output_text":
                    texts.append(str(part.get("text", "")))
    if not texts:
        raise ValueError("Hermes response has no output_text")
    return "\n".join(texts)


def _extract_json(text: str) -> str:
    stripped = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.IGNORECASE)
    start, end = stripped.find("{"), stripped.rfind("}")
    if start < 0 or end <= start:
        raise ValueError("response does not contain a JSON object")
    return stripped[start : end + 1]
