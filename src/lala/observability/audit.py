from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from typing import Any

LOGGER = logging.getLogger("lala.audit")
if not LOGGER.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(message)s"))
    LOGGER.addHandler(_handler)
LOGGER.setLevel(logging.INFO)
LOGGER.propagate = False

ALLOWED_AUDIT_FIELDS = frozenset(
    {
        "request_id",
        "run_id",
        "channel",
        "asset_id",
        "idempotent_replay",
        "planner_prompt_sha256",
        "calibration_registry_sha256",
        "input_mime",
        "input_bytes",
        "input_width",
        "input_height",
        "input_sha256",
        "tools",
        "tool_versions",
        "engine_versions",
        "evidence",
        "output_sha256",
        "latency_ms",
        "error_code",
        "retryable",
        "exception_type",
    }
)


def audit_event(event: str, **fields: Any) -> None:
    safe_fields = {key: value for key, value in fields.items() if key in ALLOWED_AUDIT_FIELDS}
    payload = {
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "event": event,
        **safe_fields,
    }
    LOGGER.info(json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str))
