from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def test_slack_skill_requires_one_composite_runtime_call() -> None:
    skill = (ROOT / "skills" / "lala-coordinator" / "SKILL.md").read_text(encoding="utf-8")

    assert "process_slack_image(cache_filename, prompt, mode)" in skill
    assert "정확히 한 번 호출" in skill
    assert "운영 요청을 디버깅이나 개발 작업으로 전환하지 않는다" in skill
    assert "terminal, Python 실행" in skill


def test_hermes_example_isolates_slack_from_development_tools() -> None:
    config = yaml.safe_load((ROOT / "config" / "hermes" / "config.example.yaml").read_text())

    assert config["platform_toolsets"]["slack"] == ["skills", "lala-slack"]
    assert config["platform_toolsets"]["api_server"] == ["no_mcp"]
    slack_server = config["mcp_servers"]["lala-slack"]
    assert slack_server["tools"]["include"] == ["process_slack_image"]
    assert slack_server["env"]["LALA_SLACK_CACHE_DIR"] == "${LALA_SLACK_CACHE_DIR}"
