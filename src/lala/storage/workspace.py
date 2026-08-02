from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from lala.domain.errors import LalaError, NotFoundError

SAFE_ID = re.compile(r"^[a-zA-Z0-9_-]{3,128}$")


def ensure_within(path: Path, root: Path) -> Path:
    resolved = path.resolve()
    root_resolved = root.resolve()
    if resolved != root_resolved and root_resolved not in resolved.parents:
        raise LalaError("UNSAFE_PATH", "허용되지 않은 파일 경로입니다.", False)
    return resolved


@dataclass(frozen=True, slots=True)
class JobWorkspace:
    request_id: str
    root: Path
    input_dir: Path
    intermediate_dir: Path
    output_dir: Path

    @property
    def input_image(self) -> Path:
        return self.input_dir / "source.png"

    def intermediate(self, order: int, suffix: str = ".png") -> Path:
        if order < 1 or not re.fullmatch(r"\.[a-zA-Z0-9]{2,5}", suffix):
            raise LalaError("UNSAFE_PATH", "허용되지 않은 중간 파일 경로입니다.", False)
        return ensure_within(self.intermediate_dir / f"step-{order:02d}{suffix}", self.root)

    def output(self, filename: str = "result.png") -> Path:
        if Path(filename).name != filename or not re.fullmatch(r"[a-zA-Z0-9._-]{1,128}", filename):
            raise LalaError("UNSAFE_PATH", "허용되지 않은 출력 파일명입니다.", False)
        return ensure_within(self.output_dir / filename, self.root)


class WorkspaceManager:
    def __init__(self, jobs_root: Path) -> None:
        self.jobs_root = jobs_root.resolve()
        self.jobs_root.mkdir(parents=True, exist_ok=True)

    def create(self, request_id: str) -> JobWorkspace:
        workspace = self.get(request_id)
        for path in (
            workspace.root,
            workspace.input_dir,
            workspace.intermediate_dir,
            workspace.output_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)
        return workspace

    def get(self, request_id: str) -> JobWorkspace:
        if not SAFE_ID.fullmatch(request_id):
            raise LalaError("INVALID_REQUEST_ID", "유효하지 않은 요청 ID입니다.", False)
        root = ensure_within(self.jobs_root / request_id, self.jobs_root)
        return JobWorkspace(
            request_id=request_id,
            root=root,
            input_dir=root / "input",
            intermediate_dir=root / "intermediate",
            output_dir=root / "output",
        )

    def require_input(self, request_id: str) -> Path:
        path = self.get(request_id).input_image
        if not path.is_file():
            raise NotFoundError("요청의 입력 이미지를 찾을 수 없습니다.")
        return path.resolve()
