from __future__ import annotations

from pathlib import Path

from lala.config import Settings


def test_knowledge_directories_are_always_bound_to_project_root(
    tmp_path: Path, monkeypatch
) -> None:
    project_root = tmp_path / "project"
    hermes_temp = tmp_path / "hermes-session"
    monkeypatch.setenv("LALA_RAW_DIR", str(hermes_temp / "raw"))
    monkeypatch.setenv(
        "LALA_TECHNICAL_LIBRARY_DIR", str(hermes_temp / "technical-library")
    )

    settings = Settings.from_env(project_root)
    settings.ensure_directories()

    assert settings.raw_dir == (project_root / "raw").resolve()
    assert settings.technical_library_dir == (project_root / "technical-library").resolve()
    assert settings.raw_dir.is_dir()
    assert settings.technical_library_dir.is_dir()
    assert not hermes_temp.exists()


def test_settings_load_image_api_configuration(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "must-not-be-used-by-imagegen")
    monkeypatch.setenv("LALA_IMAGEGEN_OPENAI_API_KEY", "test-image-api-key")

    configured = Settings.from_env(tmp_path)

    assert configured.imagegen_openai_api_key == "test-image-api-key"
    assert configured.imagegen_model == "gpt-image-2"
    assert configured.imagegen_quality == "low"
    assert configured.imagegen_size == "1024x1024"
