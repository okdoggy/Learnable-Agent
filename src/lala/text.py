from __future__ import annotations

from pathlib import Path


class TextEncodingError(ValueError):
    """Raised when project text cannot be represented as clean UTF-8/LF."""


def normalize_utf8_lf(text: str) -> str:
    """Validate Unicode text and normalize every line ending to LF."""
    if "\ufffd" in text:
        raise TextEncodingError("대체 문자(U+FFFD)가 포함된 텍스트는 허용되지 않습니다.")
    try:
        text.encode("utf-8", errors="strict")
    except UnicodeEncodeError as exc:
        raise TextEncodingError("텍스트를 UTF-8로 인코딩할 수 없습니다.") from exc
    return text.replace("\r\n", "\n").replace("\r", "\n")


def read_utf8_lf(path: Path) -> str:
    """Read strict UTF-8 and present normalized LF text to callers."""
    try:
        decoded = path.read_bytes().decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise TextEncodingError("파일을 UTF-8로 디코딩할 수 없습니다.") from exc
    return normalize_utf8_lf(decoded)


def write_utf8_lf(path: Path, text: str) -> None:
    """Write UTF-8 without BOM and with LF line endings."""
    normalized = normalize_utf8_lf(text)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", errors="strict", newline="\n") as stream:
        stream.write(normalized)
