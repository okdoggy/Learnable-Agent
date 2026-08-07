from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_calibration_review_context_reports_latest_cursor(tmp_path: Path) -> None:
    reports = tmp_path / "calibration" / "reports"
    reports.mkdir(parents=True)
    (reports / "20260806-210000.md").write_text("older\n", encoding="utf-8")
    (reports / "20260807-210000.md").write_text("latest\n", encoding="utf-8")
    env = {**os.environ, "LALA_PROJECT_ROOT": str(tmp_path)}

    completed = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "scripts" / "calibration_review_context.py")],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )

    context = json.loads(completed.stdout)
    assert context["timezone"] == "Asia/Seoul"
    assert context["latest_report"] == "calibration/reports/20260807-210000.md"
    assert context["report_directory"] == "calibration/reports"


def test_calibration_review_context_uses_workdir_without_environment(tmp_path: Path) -> None:
    env = dict(os.environ)
    env.pop("LALA_PROJECT_ROOT", None)

    completed = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "scripts" / "calibration_review_context.py")],
        check=True,
        capture_output=True,
        text=True,
        env=env,
        cwd=tmp_path,
    )

    context = json.loads(completed.stdout)
    assert context["project_root"] == str(tmp_path.resolve())


def test_calibration_review_context_reads_installed_project_root_marker(tmp_path: Path) -> None:
    script_dir = tmp_path / "scripts"
    script_dir.mkdir()
    installed = script_dir / "lala-calibration-review-context.py"
    installed.write_bytes((PROJECT_ROOT / "scripts" / "calibration_review_context.py").read_bytes())
    (script_dir / "lala-calibration-project-root.txt").write_text(
        f"{tmp_path / 'project'}\n", encoding="utf-8"
    )
    env = dict(os.environ)
    env.pop("LALA_PROJECT_ROOT", None)

    completed = subprocess.run(
        [sys.executable, str(installed)],
        check=True,
        capture_output=True,
        text=True,
        env=env,
        cwd=tmp_path,
    )

    context = json.loads(completed.stdout)
    assert context["project_root"] == str((tmp_path / "project").resolve())


def test_publisher_copies_staged_reports_once(tmp_path: Path) -> None:
    script_dir = tmp_path / "scripts"
    script_dir.mkdir()
    project_root = tmp_path / "project"
    staging = tmp_path / "staging"
    staging.mkdir()
    report = staging / "20260807-210000.md"
    report.write_text("# candidate review\n", encoding="utf-8")
    installed = script_dir / "lala-calibration-report-publisher.py"
    installed.write_bytes(
        (PROJECT_ROOT / "scripts" / "calibration_report_publisher.py").read_bytes()
    )
    (script_dir / "lala-calibration-project-root.txt").write_text(
        f"{project_root}\n", encoding="utf-8"
    )
    env = {
        **os.environ,
        "LALA_CALIBRATION_STAGING_DIR": str(staging),
    }

    first = subprocess.run(
        [sys.executable, str(installed)],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )
    second = subprocess.run(
        [sys.executable, str(installed)],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )

    assert (project_root / "calibration" / "reports" / report.name).read_text(
        encoding="utf-8"
    ) == "# candidate review\n"
    assert "1개" in first.stdout
    assert second.stdout == ""


def test_registers_nightly_calibration_review_at_21_kst(tmp_path: Path) -> None:
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    calls = tmp_path / "hermes-calls.txt"
    fake_hermes = fake_bin / "hermes"
    fake_hermes.write_text(
        "#!/usr/bin/env bash\n"
        "printf '%s\\n' \"$*\" >> \"$HERMES_CALLS\"\n"
        "if [[ \"$1 $2\" == \"config path\" ]]; then "
        "printf '%s\\n' \"$HERMES_FAKE_CONFIG\"; exit 0; fi\n"
        "if [[ \"$1 $2\" == \"cron list\" ]]; then exit 0; fi\n",
        encoding="utf-8",
    )
    fake_hermes.chmod(0o755)
    env = {
        **os.environ,
        "PATH": f"{fake_bin}:{os.environ['PATH']}",
        "HERMES_CALLS": str(calls),
        "HERMES_FAKE_CONFIG": str(tmp_path / "hermes" / "config.yaml"),
        "LALA_PROJECT_ROOT": str(PROJECT_ROOT),
    }

    subprocess.run(
        ["bash", str(PROJECT_ROOT / "scripts" / "register-hermes-cron.sh")],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )

    recorded = calls.read_text(encoding="utf-8")
    assert "cron create 0 12 * * *" in recorded
    assert "lala-calibration-reviewer" in recorded
    assert "--script lala-calibration-review-context.py" in recorded
    assert "cron create 10 12 * * *" in recorded
    assert "--script lala-calibration-report-publisher.py --no-agent" in recorded
    installed_script = tmp_path / "hermes" / "scripts" / "lala-calibration-review-context.py"
    assert installed_script.is_file()
    assert not installed_script.is_symlink()
    assert installed_script.read_bytes() == (
        PROJECT_ROOT / "scripts" / "calibration_review_context.py"
    ).read_bytes()
    installed_publisher = tmp_path / "hermes" / "scripts" / "lala-calibration-report-publisher.py"
    assert installed_publisher.read_bytes() == (
        PROJECT_ROOT / "scripts" / "calibration_report_publisher.py"
    ).read_bytes()
    marker = tmp_path / "hermes" / "scripts" / "lala-calibration-project-root.txt"
    assert marker.read_text(encoding="utf-8") == f"{PROJECT_ROOT}\n"
