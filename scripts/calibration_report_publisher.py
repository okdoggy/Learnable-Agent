from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT_MARKER = "lala-calibration-project-root.txt"


def _project_root() -> Path:
    root_value = os.environ.get("LALA_PROJECT_ROOT")
    if root_value:
        return Path(root_value).expanduser().resolve()
    marker = Path(__file__).resolve().with_name(PROJECT_ROOT_MARKER)
    if not marker.is_file():
        raise RuntimeError(f"프로젝트 루트 marker가 없습니다: {marker}")
    return Path(marker.read_text(encoding="utf-8").strip()).expanduser().resolve()


def main() -> None:
    staging_dir = Path(
        os.environ.get(
            "LALA_CALIBRATION_STAGING_DIR",
            str(Path.home() / "calibration-staging"),
        )
    ).expanduser().resolve()
    if not staging_dir.is_dir():
        return

    destination = _project_root() / "calibration" / "reports"
    destination.mkdir(parents=True, exist_ok=True)
    published = 0
    for source in sorted(staging_dir.glob("*.md")):
        content = source.read_text(encoding="utf-8")
        if "\ufffd" in content:
            raise ValueError(f"대체 문자가 포함된 보고서는 발행할 수 없습니다: {source.name}")
        target = destination / source.name
        if target.exists():
            if target.read_text(encoding="utf-8") != content:
                raise ValueError(f"같은 이름의 다른 보고서가 이미 존재합니다: {target}")
            continue
        temporary = target.with_suffix(".md.tmp")
        temporary.write_text(content, encoding="utf-8", newline="\n")
        temporary.replace(target)
        published += 1

    if published:
        print(f"캘리브레이션 보고서 {published}개를 프로젝트에 발행했습니다.")


if __name__ == "__main__":
    main()
