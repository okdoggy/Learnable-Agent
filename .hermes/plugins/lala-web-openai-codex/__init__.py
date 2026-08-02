from __future__ import annotations

from .provider import OpenAICodexWebSearchProvider


def register(ctx) -> None:
    ctx.register_web_search_provider(OpenAICodexWebSearchProvider())
