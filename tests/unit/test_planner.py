from __future__ import annotations

import base64
import json
import os
from dataclasses import replace
from pathlib import Path

import httpx
from PIL import Image

from lala.config import Settings
from lala.hermes.planner import HermesResponsesPlanner
from lala.knowledge.markdown import render_markdown
from lala.knowledge.technical import TechnicalLibraryRepository
from lala.renderers.inspection import inspect_image
from lala.text import write_utf8_lf


def _hermes_response(request_id: str) -> dict[str, object]:
    plan = {
        "schema_version": "1.0",
        "request_id": request_id,
        "summary_ko": "원본을 자연스럽게 밝힙니다.",
        "steps": [
            {
                "order": 1,
                "tool": "remaster",
                "parameters": {"brightness": 8},
                "reason_ko": "새 픽셀을 만들지 않고 어두운 영역을 회복합니다.",
                "evidence": [],
            }
        ],
        "overall_reason_ko": "결정론적 기본 보정으로 요청을 충족할 수 있습니다.",
        "confidence": 0.6,
        "warnings_ko": ["근거 스킬 없음"],
    }
    return {
        "id": "resp_valid",
        "output": [
            {
                "type": "message",
                "content": [{"type": "output_text", "text": json.dumps(plan)}],
            }
        ],
    }


def test_hermes_planner_performs_one_schema_correction(
    settings: Settings, sample_image: Path
) -> None:
    write_utf8_lf(
        settings.planner_prompt_path,
        (
            "모든 이미지 보정·편집 계획은 실제로 제공되어 읽은 active 문서의 ID와 version을 "
            "evidence에 기록한다.\n"
        ),
    )
    write_utf8_lf(
        settings.technical_library_dir / "001-shadow-recovery.md",
        render_markdown(
            {
                "schema_version": "1.0",
                "number": 1,
                "technical_id": "shadow-recovery",
                "title_ko": "그림자 세부 회복",
                "summary_ko": "밝은 영역을 보존하며 어두운 부분의 세부를 회복한다.",
                "version": "1.0.0",
                "status": "active",
                "supported_tools": ["remaster"],
                "confidence": 0.8,
                "raw_scenario_ids": ["raw-20260802-abc123", "raw-20260802-def456"],
                "source_urls": ["https://example.com/a", "https://another.example/b"],
                "reviewed_at": "2026-08-02",
                "created_by": "hermes-llm",
            },
            "# 그림자 세부 회복\n\n## 기술 절차\n\n1. 고유한 전문 내용을 먼저 읽는다.\n",
        ),
    )
    payloads: list[dict[str, object]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        payloads.append(json.loads(request.content))
        if len(payloads) == 1:
            return httpx.Response(
                200,
                json={
                    "id": "resp_invalid",
                    "output": [
                        {
                            "type": "message",
                            "content": [{"type": "output_text", "text": "not json"}],
                        }
                    ],
                },
            )
        return httpx.Response(200, json=_hermes_response("req_hermes"))

    client = httpx.Client(transport=httpx.MockTransport(handler))
    planner = HermesResponsesPlanner(
        replace(settings, hermes_api_key="test-only"),
        TechnicalLibraryRepository(settings.technical_library_dir),
        client,
    )

    plan = planner.plan(
        request_id="req_hermes",
        prompt="자연스럽게 밝게 해줘",
        image_path=sample_image,
        inspection=inspect_image(sample_image),
    )

    assert plan.request_id == "req_hermes"
    assert len(payloads) == 2
    assert payloads[1]["previous_response_id"] == "resp_invalid"
    first_input = payloads[0]["input"][0]["content"][0]["text"]
    assert "전체 문맥을 의미적으로 해석" in first_input
    assert "단어 포함 여부" in first_input
    assert "실제로 읽을 수 있도록 제공된 active technical library 문서 전문" in first_input
    required_evidence_instruction = (
        "모든 이미지 보정·편집 계획은 실제로 제공되어 읽은 active 문서의 ID와 version을 "
        "evidence에 기록"
    )
    assert required_evidence_instruction in payloads[0]["instructions"]
    assert "고유한 전문 내용을 먼저 읽는다" in first_input
    assert "renderer capability 및 parameter calibration registry" in first_input
    assert "semantic-local-masks" in first_input
    assert "global shadow lift also raises background shadows" in first_input


def test_hermes_planner_retries_transient_rate_limit(
    settings: Settings, sample_image: Path, monkeypatch
) -> None:
    calls = 0

    def handler(_: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if calls == 1:
            return httpx.Response(429, json={"error": "slow down"})
        return httpx.Response(200, json=_hermes_response("req_retry"))

    monkeypatch.setattr("lala.hermes.planner.time.sleep", lambda _: None)
    client = httpx.Client(transport=httpx.MockTransport(handler))
    planner = HermesResponsesPlanner(
        replace(settings, hermes_api_key="test-only", hermes_max_attempts=2),
        TechnicalLibraryRepository(settings.technical_library_dir),
        client,
    )

    planner.plan(
        request_id="req_retry",
        prompt="자연스럽게 밝게 해줘",
        image_path=sample_image,
        inspection=inspect_image(sample_image),
    )

    assert calls == 2


def test_hermes_planner_keeps_original_large_image_bytes_within_configured_cap(
    settings: Settings, tmp_path: Path
) -> None:
    source = tmp_path / "large-source.png"
    Image.frombytes("RGB", (2000, 2000), os.urandom(2000 * 2000 * 3)).save(source, format="PNG")
    payload_sizes: list[int] = []
    image_urls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        payload_sizes.append(len(request.content))
        payload = json.loads(request.content)
        image_urls.append(payload["input"][0]["content"][1]["image_url"])
        return httpx.Response(200, json=_hermes_response("req_large_preview"))

    client = httpx.Client(transport=httpx.MockTransport(handler))
    planner = HermesResponsesPlanner(
        replace(settings, hermes_api_key="test-only"),
        TechnicalLibraryRepository(settings.technical_library_dir),
        client,
    )

    planner.plan(
        request_id="req_large_preview",
        prompt="자연스럽게 보정해줘",
        image_path=source,
        inspection=inspect_image(source),
    )

    assert 10 * 1024 * 1024 < payload_sizes[0] <= 40 * 1024 * 1024
    assert image_urls[0].startswith("data:image/png;base64,")
    assert base64.b64decode(image_urls[0].split(",", 1)[1]) == source.read_bytes()
