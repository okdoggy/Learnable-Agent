from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from lala.domain.errors import LalaError
from lala.text import TextEncodingError, normalize_utf8_lf, read_utf8_lf


def parse_frontmatter_text(text: str) -> tuple[dict[str, Any], str]:
    try:
        text = normalize_utf8_lf(text)
    except TextEncodingError as exc:
        raise LalaError(
            "INVALID_MARKDOWN_ENCODING",
            "Markdown에 올바르지 않은 UTF-8 텍스트가 포함되어 있습니다.",
            False,
        ) from exc
    if not text.startswith("---\n"):
        raise LalaError("INVALID_MARKDOWN", "Markdown frontmatter가 없습니다.", False)
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise LalaError("INVALID_MARKDOWN", "Markdown frontmatter 경계가 올바르지 않습니다.", False)
    try:
        metadata = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        raise LalaError("INVALID_MARKDOWN", "Markdown YAML을 읽을 수 없습니다.", False) from exc
    if not isinstance(metadata, dict):
        raise LalaError("INVALID_MARKDOWN", "Markdown frontmatter는 객체여야 합니다.", False)
    return metadata, parts[2].lstrip("\n")


def read_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    try:
        return parse_frontmatter_text(read_utf8_lf(path))
    except (OSError, TextEncodingError) as exc:
        raise LalaError("INVALID_MARKDOWN", "Markdown 파일을 읽을 수 없습니다.", False) from exc


def render_markdown(metadata: dict[str, Any], body: str) -> str:
    yaml_text = yaml.safe_dump(
        metadata,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=100,
    ).rstrip()
    try:
        return normalize_utf8_lf(f"---\n{yaml_text}\n---\n\n{body.rstrip()}\n")
    except TextEncodingError as exc:
        raise LalaError(
            "INVALID_MARKDOWN_ENCODING",
            "Markdown에 올바르지 않은 UTF-8 텍스트가 포함되어 있습니다.",
            False,
        ) from exc
