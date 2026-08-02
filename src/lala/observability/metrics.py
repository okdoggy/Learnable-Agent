from __future__ import annotations

import threading
from collections import defaultdict


class MetricsRegistry:
    def __init__(self) -> None:
        self._counters: dict[tuple[str, tuple[tuple[str, str], ...]], float] = defaultdict(float)
        self._lock = threading.Lock()

    def increment(self, name: str, **labels: str) -> None:
        key = (name, tuple(sorted(labels.items())))
        with self._lock:
            self._counters[key] += 1

    def render_prometheus(self) -> str:
        with self._lock:
            rows = sorted(self._counters.items())
        lines = ["# lala in-process counters"]
        for (name, labels), value in rows:
            label_text = ""
            if labels:
                encoded = ",".join(f'{key}="{_escape_label(label)}"' for key, label in labels)
                label_text = "{" + encoded + "}"
            lines.append(f"{name}{label_text} {value:g}")
        return "\n".join(lines) + "\n"


def _escape_label(value: str) -> str:
    return value.replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')


METRICS = MetricsRegistry()
