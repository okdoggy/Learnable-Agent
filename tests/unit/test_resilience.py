from __future__ import annotations

import pytest

from lala.domain.errors import LalaError
from lala.resilience import CircuitBreaker, SlidingWindowLimit


def test_circuit_breaker_opens_and_recovers(monkeypatch) -> None:
    clock = 100.0
    monkeypatch.setattr("lala.resilience.time.monotonic", lambda: clock)
    breaker = CircuitBreaker(failure_threshold=2, recovery_seconds=10)

    breaker.failure()
    breaker.require_available()
    breaker.failure()
    with pytest.raises(LalaError) as captured:
        breaker.require_available()
    assert captured.value.code == "AGENT_UNAVAILABLE"

    clock = 111.0
    breaker.require_available()


def test_sliding_window_limit_releases_old_events(monkeypatch) -> None:
    clock = 100.0
    monkeypatch.setattr("lala.resilience.time.monotonic", lambda: clock)
    limiter = SlidingWindowLimit(
        limit=2,
        window_seconds=60,
        code="RATE_LIMITED",
        message_ko="호출 한도 초과",
    )

    limiter.consume("client")
    limiter.consume("client")
    with pytest.raises(LalaError) as captured:
        limiter.consume("client")
    assert captured.value.code == "RATE_LIMITED"

    clock = 161.0
    limiter.consume("client")
