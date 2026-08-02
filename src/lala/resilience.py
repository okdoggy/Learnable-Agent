from __future__ import annotations

import threading
import time
from collections import deque

from lala.domain.errors import LalaError


class CircuitBreaker:
    def __init__(self, *, failure_threshold: int, recovery_seconds: float) -> None:
        self.failure_threshold = max(1, failure_threshold)
        self.recovery_seconds = max(0.1, recovery_seconds)
        self._failures = 0
        self._open_until = 0.0
        self._lock = threading.Lock()

    def require_available(self) -> None:
        with self._lock:
            now = time.monotonic()
            if self._open_until > now:
                raise LalaError(
                    "AGENT_UNAVAILABLE",
                    "추천 Agent가 일시적으로 불안정합니다. 잠시 후 다시 시도해 주세요.",
                    True,
                )
            if self._open_until:
                self._open_until = 0.0
                self._failures = 0

    def success(self) -> None:
        with self._lock:
            self._failures = 0
            self._open_until = 0.0

    def failure(self) -> None:
        with self._lock:
            self._failures += 1
            if self._failures >= self.failure_threshold:
                self._open_until = time.monotonic() + self.recovery_seconds


class SlidingWindowLimit:
    def __init__(self, *, limit: int, window_seconds: float, code: str, message_ko: str) -> None:
        self.limit = max(1, limit)
        self.window_seconds = window_seconds
        self.code = code
        self.message_ko = message_ko
        self._events: dict[str, deque[float]] = {}
        self._lock = threading.Lock()

    def consume(self, key: str) -> None:
        now = time.monotonic()
        with self._lock:
            events = self._events.setdefault(key, deque())
            cutoff = now - self.window_seconds
            while events and events[0] <= cutoff:
                events.popleft()
            if len(events) >= self.limit:
                raise LalaError(self.code, self.message_ko, True)
            events.append(now)
