from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_hermes_collection_is_pinned_to_project_raw_directory() -> None:
    registration_script = (ROOT / "scripts/register-hermes-cron.sh").read_text(
        encoding="utf-8"
    )
    example_config = (ROOT / "config/hermes/config.example.yaml").read_text(
        encoding="utf-8"
    )
    collector_skill = (ROOT / "skills/knowledge-collector/SKILL.md").read_text(
        encoding="utf-8"
    )

    assert 'lala_raw_dir="${LALA_PROJECT_ROOT}/raw"' in registration_script
    assert (
        "hermes config set mcp_servers.lala-tools.env.LALA_RAW_DIR "
        '"${lala_raw_dir}"'
    ) in registration_script
    assert 'LALA_RAW_DIR: "${LALA_PROJECT_ROOT}/raw"' in example_config
    assert "현재 프로젝트의 `raw/`" in collector_skill
