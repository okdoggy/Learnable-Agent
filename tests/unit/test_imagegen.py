from __future__ import annotations

import subprocess
from dataclasses import replace
from pathlib import Path

import pytest
from PIL import Image, ImageStat, PngImagePlugin

from lala.config import Settings
from lala.domain.errors import ExecutionError
from lala.domain.models import GenerateAIParameters
from lala.renderers.imagegen import CodexImagegenRunner


def test_committed_builtin_imagegen_edit_fixture_is_valid() -> None:
    fixture_root = Path(__file__).resolve().parents[1] / "fixtures" / "imagegen"
    with Image.open(fixture_root / "backlit-still-life-source.png") as source:
        source.load()
        source_size = source.size
        source_luminance = ImageStat.Stat(source.convert("L")).mean[0]
        assert source.info == {}
        assert len(source.getexif()) == 0
    with Image.open(fixture_root / "backlit-still-life-edited.png") as edited:
        edited.load()
        edited_size = edited.size
        edited_luminance = ImageStat.Stat(edited.convert("L")).mean[0]
        assert edited.info == {}
        assert len(edited.getexif()) == 0

    assert source_size == edited_size == (1536, 1024)
    assert edited_luminance > source_luminance


def _configured(settings: Settings, tmp_path: Path, *, attempts: int = 3) -> Settings:
    executable = tmp_path / "codex"
    executable.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
    executable.chmod(0o755)
    return replace(
        settings,
        codex_executable=str(executable),
        imagegen_max_attempts=attempts,
    )


def _source_and_destination(settings: Settings, request_id: str) -> tuple[Path, Path]:
    source = settings.var_dir / "jobs" / request_id / "input" / "source.png"
    source.parent.mkdir(parents=True)
    Image.new("RGB", (16, 16), (1, 2, 3)).save(source)
    destination = settings.output_dir / "imagegen" / request_id / "result.png"
    return source, destination


def test_imagegen_invokes_codex_builtin_skill_without_api_key(
    settings: Settings, tmp_path: Path, monkeypatch
) -> None:
    configured = _configured(settings, tmp_path)
    source, destination = _source_and_destination(settings, "req_imagegen")
    captured: dict[str, object] = {}

    def fake_run(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        captured["command"] = command
        captured["kwargs"] = kwargs
        prompt = str(kwargs["input"])
        assert "$imagegen" in prompt
        assert "default built-in image generation tool" in prompt
        assert "fallback Image API CLI" in prompt
        assert "인물의 얼굴을 유지" in prompt
        assert str(destination.resolve()) in prompt
        destination.parent.mkdir(parents=True, exist_ok=True)
        metadata = PngImagePlugin.PngInfo()
        metadata.add_text("private", "must be removed")
        Image.new("RGB", (16, 16), (4, 5, 6)).save(destination, pnginfo=metadata)
        return subprocess.CompletedProcess(command, 0, "ok", "")

    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("SLACK_BOT_TOKEN", "must-not-leak")
    monkeypatch.setenv("HERMES_API_KEY", "must-not-leak")
    monkeypatch.setattr(subprocess, "run", fake_run)
    parameters = GenerateAIParameters(
        use_case="lighting-weather",
        prompt="배경 날씨만 비 오는 날로 변경",
        constraints=["인물의 얼굴을 유지"],
    )

    result = CodexImagegenRunner(configured).edit(source, destination, parameters)

    command = captured["command"]
    assert isinstance(command, list)
    assert command[1:3] == ["exec", "--ephemeral"]
    assert command[command.index("--cd") + 1] == str(destination.parent)
    assert "--skip-git-repo-check" in command
    assert "--image" in command
    assert command[-1] == "-"
    environment = captured["kwargs"]["env"]
    assert "OPENAI_API_KEY" not in environment
    assert "SLACK_BOT_TOKEN" not in environment
    assert "HERMES_API_KEY" not in environment
    assert captured["kwargs"]["encoding"] == "utf-8"
    assert result.path == destination.resolve()
    assert result.execution_mode == "codex-imagegen-builtin"
    with Image.open(result.path) as generated:
        assert generated.info == {}
        assert len(generated.getexif()) == 0


def test_imagegen_retries_only_transient_codex_failures(
    settings: Settings, tmp_path: Path, monkeypatch
) -> None:
    configured = _configured(settings, tmp_path, attempts=2)
    source, destination = _source_and_destination(settings, "req_retry")
    calls = 0

    def fake_run(command: list[str], **_: object) -> subprocess.CompletedProcess[str]:
        nonlocal calls
        calls += 1
        if calls == 1:
            return subprocess.CompletedProcess(command, 1, "", "HTTP 429 rate limit")
        destination.parent.mkdir(parents=True, exist_ok=True)
        Image.new("RGB", (16, 16), (4, 5, 6)).save(destination)
        return subprocess.CompletedProcess(command, 0, "ok", "")

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr("lala.renderers.imagegen.time.sleep", lambda _: None)

    CodexImagegenRunner(configured).edit(
        source,
        destination,
        GenerateAIParameters(use_case="lighting-weather", prompt="날씨만 변경"),
    )

    assert calls == 2


def test_imagegen_does_not_retry_policy_or_user_errors(
    settings: Settings, tmp_path: Path, monkeypatch
) -> None:
    configured = _configured(settings, tmp_path, attempts=3)
    source, destination = _source_and_destination(settings, "req_policy")
    calls = 0

    def fake_run(command: list[str], **_: object) -> subprocess.CompletedProcess[str]:
        nonlocal calls
        calls += 1
        return subprocess.CompletedProcess(command, 1, "", "policy blocked")

    monkeypatch.setattr(subprocess, "run", fake_run)

    with pytest.raises(ExecutionError) as captured:
        CodexImagegenRunner(configured).edit(
            source,
            destination,
            GenerateAIParameters(use_case="lighting-weather", prompt="날씨만 변경"),
        )

    assert captured.value.retryable is False
    assert calls == 1


def test_imagegen_rejects_output_symlink_escape(
    settings: Settings, tmp_path: Path, monkeypatch
) -> None:
    configured = _configured(settings, tmp_path, attempts=1)
    source, destination = _source_and_destination(settings, "req_symlink")
    outside = tmp_path / "outside.png"
    Image.new("RGB", (16, 16), (4, 5, 6)).save(outside)

    def fake_run(command: list[str], **_: object) -> subprocess.CompletedProcess[str]:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.symlink_to(outside)
        return subprocess.CompletedProcess(command, 0, "ok", "")

    monkeypatch.setattr(subprocess, "run", fake_run)

    with pytest.raises(ExecutionError, match="output 디렉터리"):
        CodexImagegenRunner(configured).edit(
            source,
            destination,
            GenerateAIParameters(use_case="lighting-weather", prompt="날씨만 변경"),
        )
