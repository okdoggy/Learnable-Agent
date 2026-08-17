from __future__ import annotations

import base64
import io
from dataclasses import replace
from pathlib import Path

import httpx
import pytest
from PIL import Image, ImageStat, PngImagePlugin

from lala.config import Settings
from lala.domain.errors import ExecutionError
from lala.domain.models import GenerateAIParameters
from lala.renderers.imagegen import OpenAIImagegenRunner


def test_committed_imagegen_edit_fixture_is_valid() -> None:
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


def _configured(settings: Settings, *, attempts: int = 3) -> Settings:
    return replace(
        settings,
        imagegen_openai_api_key="image-api-secret",
        imagegen_max_attempts=attempts,
    )


def _source_and_destination(
    settings: Settings, request_id: str, *, size: tuple[int, int] = (16, 16)
) -> tuple[Path, Path]:
    source = settings.var_dir / "jobs" / request_id / "input" / "source.png"
    source.parent.mkdir(parents=True)
    Image.new("RGB", size, (1, 2, 3)).save(source)
    destination = settings.output_dir / "imagegen" / request_id / "result.png"
    return source, destination


def _encoded_png(*, size: tuple[int, int] = (1024, 1024), metadata: bool = False) -> str:
    generated = io.BytesIO()
    pnginfo = None
    if metadata:
        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("private", "must be removed")
    Image.new("RGB", size, (4, 5, 6)).save(generated, format="PNG", pnginfo=pnginfo)
    return base64.b64encode(generated.getvalue()).decode()


def _parameters() -> GenerateAIParameters:
    return GenerateAIParameters(
        execution_mode="openai-image-api",
        use_case="lighting-weather",
        prompt="only change the weather",
        constraints=["keep identity"],
        avoid=["avoid text"],
    )


def test_imagegen_calls_gpt_image_2_low_at_1k(settings: Settings) -> None:
    configured = _configured(settings)
    source, destination = _source_and_destination(settings, "req_openai_imagegen")

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url == "https://api.openai.com/v1/images/edits"
        assert request.headers["authorization"] == "Bearer image-api-secret"
        body = request.read()
        assert b'name="model"' in body and b"gpt-image-2" in body
        assert b'name="quality"' in body and b"low" in body
        assert b'name="size"' in body and b"1024x1024" in body
        assert b'name="output_format"' in body and b"png" in body
        assert b'name="image[]"' in body
        assert b"only change the weather" in body
        assert b"keep identity" in body
        assert b"avoid text" in body
        assert b"Preserve the input composition and aspect ratio" in body
        return httpx.Response(200, json={"data": [{"b64_json": _encoded_png(metadata=True)}]})

    client = httpx.Client(transport=httpx.MockTransport(handler))
    result = OpenAIImagegenRunner(configured, client=client).edit(
        source, destination, _parameters()
    )

    assert result.path == destination.resolve()
    assert result.execution_mode == "openai-image-api"
    assert result.model == "gpt-image-2"
    assert result.quality == "low"
    assert result.size == "1024x1024"
    with Image.open(result.path) as image:
        assert image.size == (1024, 1024)
        assert image.info == {}
        assert len(image.getexif()) == 0


@pytest.mark.parametrize(
    ("source_size", "expected_size"),
    [((3, 2), "1536x1024"), ((2, 3), "1024x1536")],
)
def test_imagegen_selects_1k_size_closest_to_input_aspect_ratio(
    settings: Settings, source_size: tuple[int, int], expected_size: str
) -> None:
    configured = _configured(settings)
    source, destination = _source_and_destination(
        settings, f"req_aspect_{source_size[0]}_{source_size[1]}", size=source_size
    )

    def handler(request: httpx.Request) -> httpx.Response:
        body = request.read()
        assert expected_size.encode() in body
        width, height = (int(value) for value in expected_size.split("x"))
        return httpx.Response(
            200, json={"data": [{"b64_json": _encoded_png(size=(width, height))}]}
        )

    client = httpx.Client(transport=httpx.MockTransport(handler))
    result = OpenAIImagegenRunner(configured, client=client).edit(
        source, destination, _parameters()
    )

    assert result.size == expected_size
    with Image.open(result.path) as image:
        assert image.size == tuple(int(value) for value in expected_size.split("x"))


def test_imagegen_requires_api_key_only_when_called(settings: Settings) -> None:
    source, destination = _source_and_destination(settings, "req_missing_key")
    called = False

    def handler(_: httpx.Request) -> httpx.Response:
        nonlocal called
        called = True
        return httpx.Response(500)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    with pytest.raises(ExecutionError, match="OPENAI_API_KEY") as captured:
        OpenAIImagegenRunner(replace(settings, imagegen_openai_api_key=""), client=client).edit(
            source, destination, _parameters()
        )

    assert captured.value.retryable is False
    assert called is False


def test_imagegen_retries_429(settings: Settings, monkeypatch) -> None:
    configured = _configured(settings, attempts=2)
    source, destination = _source_and_destination(settings, "req_retry")
    calls = 0

    def handler(_: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if calls == 1:
            return httpx.Response(429)
        return httpx.Response(200, json={"data": [{"b64_json": _encoded_png()}]})

    monkeypatch.setattr("lala.renderers.imagegen.time.sleep", lambda _: None)
    client = httpx.Client(transport=httpx.MockTransport(handler))
    OpenAIImagegenRunner(configured, client=client).edit(source, destination, _parameters())

    assert calls == 2


def test_imagegen_does_not_retry_auth_errors(settings: Settings) -> None:
    configured = _configured(settings, attempts=3)
    source, destination = _source_and_destination(settings, "req_auth")
    calls = 0

    def handler(_: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(401)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    with pytest.raises(ExecutionError) as captured:
        OpenAIImagegenRunner(configured, client=client).edit(source, destination, _parameters())

    assert captured.value.retryable is False
    assert calls == 1
    assert "image-api-secret" not in str(captured.value)


def test_imagegen_accepts_valid_response_with_different_dimensions(settings: Settings) -> None:
    configured = _configured(settings)
    source, destination = _source_and_destination(settings, "req_wrong_size")

    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={"data": [{"b64_json": _encoded_png(size=(512, 512))}]},
        )

    client = httpx.Client(transport=httpx.MockTransport(handler))
    result = OpenAIImagegenRunner(configured, client=client).edit(
        source, destination, _parameters()
    )

    assert result.size == "512x512"
    with Image.open(result.path) as image:
        assert image.size == (512, 512)
