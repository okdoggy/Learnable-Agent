from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

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
    policy = _parameter_policy(project_root / "config" / "parameter-registry.yaml")
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
        "parameter_calibration_policy": policy,
    }
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))


def _parameter_policy(registry_path: Path) -> dict[str, object] | None:
    """Expose only offline review requirements, never user assets or prompts."""
    if not registry_path.is_file():
        return None
    data = yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError("parameter registry 형식이 올바르지 않습니다.")
    calibration = data.get("calibration")
    if not isinstance(calibration, dict):
        raise ValueError("parameter registry calibration 형식이 올바르지 않습니다.")
    selection = calibration.get("lut_parameter_selection")
    if not isinstance(selection, dict):
        return None
    promotion_requirements = selection.get("promotion_requirements")
    if not isinstance(promotion_requirements, list) or not all(
        isinstance(requirement, str) for requirement in promotion_requirements
    ):
        raise ValueError("promotion_requirements 형식이 올바르지 않습니다.")
    return {
        "calibration_version": data.get("calibration_version"),
        "base_correction_before_creative_grade": selection.get(
            "base_correction_before_creative_grade"
        ),
        "atmospheric_effects": selection.get("atmospheric_effects"),
        "tonal_separation": selection.get("tonal_separation"),
        "promotion_requirements": promotion_requirements,
    }


if __name__ == "__main__":
    main()
