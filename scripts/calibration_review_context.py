from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

PROJECT_ROOT_MARKER = "lala-calibration-project-root.txt"


def _project_root() -> Path:
    root_value = os.environ.get("LALA_PROJECT_ROOT")
    if root_value:
        return Path(root_value).expanduser().resolve()
    marker = Path(__file__).resolve().with_name(PROJECT_ROOT_MARKER)
    if marker.is_file():
        return Path(marker.read_text(encoding="utf-8").strip()).expanduser().resolve()
    return Path.cwd().resolve()


def main() -> None:
    project_root = _project_root()
    report_dir = project_root / "calibration" / "reports"
    staging_dir = Path(
        os.environ.get(
            "LALA_CALIBRATION_STAGING_DIR",
            str(Path.home() / "calibration-staging"),
        )
    ).expanduser().resolve()
    existing = sorted(report_dir.glob("*.md")) if report_dir.is_dir() else []
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    payload = {
        "timezone": "Asia/Seoul",
        "project_root": str(project_root),
        "review_started_at": now.isoformat(),
        "report_directory": "calibration/reports",
        "staging_report_directory": str(staging_dir),
        "report_filename": str(staging_dir / f"{now:%Y%m%d-%H%M%S}.md"),
        "latest_report": str(existing[-1].relative_to(project_root)) if existing else None,
        "max_sessions_per_run": 5,
    }
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
