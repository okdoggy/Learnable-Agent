from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".json", ".md", ".py", ".sh", ".toml", ".ts", ".yaml", ".yml"}
IGNORED_PARTS = {".git", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".venv", "dist"}


def main() -> None:
    failures: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in IGNORED_PARTS for part in path.relative_to(ROOT).parts):
            continue
        data = path.read_bytes()
        try:
            content = data.decode("utf-8", errors="strict")
        except UnicodeError as exc:
            failures.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        if "\ufffd" in content:
            failures.append(f"{path.relative_to(ROOT)}: contains Unicode replacement character")
        if b"\r" in data:
            failures.append(f"{path.relative_to(ROOT)}: contains non-LF line endings")
    if failures:
        raise SystemExit("UTF-8 validation failed:\n" + "\n".join(failures))
    print("UTF-8 validation passed")


if __name__ == "__main__":
    main()
