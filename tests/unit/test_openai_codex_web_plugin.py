from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path
from typing import Any

PLUGIN_ROOT = (
    Path(__file__).resolve().parents[2]
    / ".hermes"
    / "plugins"
    / "lala-web-openai-codex"
)
PLUGIN_PATH = PLUGIN_ROOT / "provider.py"


def _load_provider_module() -> Any:
    agent_module = types.ModuleType("agent")
    provider_module: Any = types.ModuleType("agent.web_search_provider")

    class WebSearchProvider:
        pass

    provider_module.WebSearchProvider = WebSearchProvider
    sys.modules["agent"] = agent_module
    sys.modules["agent.web_search_provider"] = provider_module
    spec = importlib.util.spec_from_file_location("lala_openai_codex_web_provider", PLUGIN_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_search_uses_gpt_response_and_keeps_https_results() -> None:
    module = _load_provider_module()
    captured: dict[str, object] = {}

    def requester(prompt: str, allowed_domains: list[str]) -> str:
        captured["prompt"] = prompt
        captured["allowed_domains"] = allowed_domains
        return (
            '{"results": ['
            '{"title": "Adobe guide", "url": "https://www.adobe.com/guide", '
            '"description": "전문가 편집 가이드"}, '
            '{"title": "Unsafe", "url": "http://example.com", "description": "drop"}'
            "]}"
        )

    provider = module.OpenAICodexWebSearchProvider(
        requester=requester,
        allowed_domains=["adobe.com"],
    )

    result = provider.search("인물 사진 색보정", limit=5)

    assert result == {
        "success": True,
        "data": {
            "web": [
                {
                    "title": "Adobe guide",
                    "url": "https://www.adobe.com/guide",
                    "description": "전문가 편집 가이드",
                    "position": 1,
                }
            ]
        },
    }
    assert captured["allowed_domains"] == ["adobe.com"]
    assert "web_search" in str(captured["prompt"])


def test_default_transport_calls_codex_responses_web_search(monkeypatch) -> None:
    module = _load_provider_module()
    captured: dict[str, object] = {}

    monkeypatch.setattr(module, "_read_codex_access_token", lambda: "oauth-token")

    def fake_stream(payload: dict[str, object], token: str) -> list[dict[str, object]]:
        captured["payload"] = payload
        captured["token"] = token
        return [
            {
                "type": "response.output_item.done",
                "item": {
                    "type": "message",
                    "content": [
                        {
                            "type": "output_text",
                            "text": (
                                '{"results":[{"title":"Adobe",'
                                '"url":"https://adobe.com/a","description":"guide"}]}'
                            ),
                        }
                    ],
                },
            }
        ]

    monkeypatch.setattr(module, "_stream_codex_response", fake_stream)
    provider = module.OpenAICodexWebSearchProvider(allowed_domains=["adobe.com"])

    result = provider.search("photo editing", limit=1)

    assert result["success"] is True
    assert captured["token"] == "oauth-token"
    payload = captured["payload"]
    assert isinstance(payload, dict)
    assert payload["tools"] == [
        {"type": "web_search", "filters": {"allowed_domains": ["adobe.com"]}}
    ]
    assert payload["stream"] is True
    assert "browser" not in str(payload).lower()


def test_extract_reads_allowed_https_pages_with_gpt() -> None:
    module = _load_provider_module()
    captured: dict[str, object] = {}

    def requester(prompt: str, allowed_domains: list[str]) -> str:
        captured["prompt"] = prompt
        captured["allowed_domains"] = allowed_domains
        return (
            '{"documents":[{"url":"https://www.adobe.com/guide",'
            '"title":"Adobe guide","content":"노출과 화이트 밸런스를 조정한다."}]}'
        )

    provider = module.OpenAICodexWebSearchProvider(
        requester=requester,
        allowed_domains=["adobe.com"],
    )

    result = provider.extract(
        ["https://www.adobe.com/guide", "https://example.com/rejected"],
        max_chars=4000,
    )

    assert result == [
        {
            "url": "https://www.adobe.com/guide",
            "title": "Adobe guide",
            "content": "노출과 화이트 밸런스를 조정한다.",
            "raw_content": "",
            "metadata": {"source": "openai-codex-web-search"},
        }
    ]
    assert captured["allowed_domains"] == ["adobe.com"]
    assert "https://www.adobe.com/guide" in str(captured["prompt"])
    assert "example.com" not in str(captured["prompt"])


def test_provider_loads_domain_allowlist_from_hermes_config(monkeypatch) -> None:
    module = _load_provider_module()
    hermes_cli_module = types.ModuleType("hermes_cli")
    config_module: Any = types.ModuleType("hermes_cli.config")
    config_module.load_config = lambda: {
        "web": {"openai_codex": {"allowed_domains": ["adobe.com"]}}
    }
    monkeypatch.setitem(sys.modules, "hermes_cli", hermes_cli_module)
    monkeypatch.setitem(sys.modules, "hermes_cli.config", config_module)

    provider = module.OpenAICodexWebSearchProvider(
        requester=lambda _prompt, _domains: (
            '{"results":[{"title":"bad","url":"https://example.com/a",'
            '"description":"drop"}]}'
        )
    )

    result = provider.search("photo editing")

    assert result == {"success": True, "data": {"web": []}}


def test_provider_accepts_cli_serialized_domain_allowlist(monkeypatch) -> None:
    module = _load_provider_module()
    hermes_cli_module = types.ModuleType("hermes_cli")
    config_module: Any = types.ModuleType("hermes_cli.config")
    config_module.load_config = lambda: {
        "web": {
            "openai_codex": {"allowed_domains": '["adobe.com","fstoppers.com"]'}
        }
    }
    monkeypatch.setitem(sys.modules, "hermes_cli", hermes_cli_module)
    monkeypatch.setitem(sys.modules, "hermes_cli.config", config_module)
    captured: dict[str, object] = {}

    def requester(_prompt: str, domains: list[str]) -> str:
        captured["domains"] = domains
        return '{"results":[]}'

    module.OpenAICodexWebSearchProvider(requester=requester).search("photo editing")

    assert captured["domains"] == ["adobe.com", "fstoppers.com"]


def test_search_reports_codex_transport_failure() -> None:
    module = _load_provider_module()

    def requester(_prompt: str, _domains: list[str]) -> str:
        raise RuntimeError("upstream unavailable")

    result = module.OpenAICodexWebSearchProvider(requester=requester).search("photo editing")

    assert result["success"] is False
    assert "GPT web search" in result["error"]


def test_plugin_registers_openai_codex_web_provider() -> None:
    agent_module = types.ModuleType("agent")
    provider_module: Any = types.ModuleType("agent.web_search_provider")

    class WebSearchProvider:
        pass

    provider_module.WebSearchProvider = WebSearchProvider
    sys.modules["agent"] = agent_module
    sys.modules["agent.web_search_provider"] = provider_module
    spec = importlib.util.spec_from_file_location(
        "lala_test_web_plugin",
        PLUGIN_ROOT / "__init__.py",
        submodule_search_locations=[str(PLUGIN_ROOT)],
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    captured: list[Any] = []
    context = types.SimpleNamespace(register_web_search_provider=captured.append)

    module.register(context)

    assert len(captured) == 1
    assert captured[0].name == "openai-codex"
