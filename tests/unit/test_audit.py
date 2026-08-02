from __future__ import annotations

from lala.observability.audit import LOGGER, audit_event


def test_audit_log_drops_prompts_secrets_and_image_content(monkeypatch) -> None:
    messages: list[str] = []
    monkeypatch.setattr(LOGGER, "info", messages.append)

    audit_event(
        "test_event",
        request_id="req_safe",
        prompt="사용자 비밀 프롬프트",
        api_key="secret-key",
        image_content="raw-image-content",
        input_sha256="a" * 64,
    )

    assert len(messages) == 1
    assert "req_safe" in messages[0]
    assert "사용자 비밀 프롬프트" not in messages[0]
    assert "secret-key" not in messages[0]
    assert "raw-image-content" not in messages[0]
