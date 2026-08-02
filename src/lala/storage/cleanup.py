from __future__ import annotations

import shutil
from datetime import UTC, datetime, timedelta
from pathlib import Path

from lala.config import Settings
from lala.storage.database import Database
from lala.storage.workspace import ensure_within


def cleanup_expired(settings: Settings, *, now: datetime | None = None) -> dict[str, int]:
    settings.ensure_directories()
    database = Database(settings.database_path)
    cutoff = now or datetime.now(UTC)
    asset_paths, request_ids = database.expired_paths(cutoff)
    removed_assets = 0
    removed_jobs = 0
    removed_imagegen = 0
    asset_root = (settings.var_dir / "assets").resolve()
    jobs_root = (settings.var_dir / "jobs").resolve()
    for asset_path in asset_paths:
        safe_file = ensure_within(asset_path, asset_root)
        asset_dir = ensure_within(safe_file.parent, asset_root)
        if asset_dir != asset_root and asset_dir.is_dir():
            shutil.rmtree(asset_dir)
            removed_assets += 1
    for request_id in request_ids:
        job_dir = ensure_within(jobs_root / request_id.name, jobs_root)
        if job_dir != jobs_root and job_dir.is_dir():
            shutil.rmtree(job_dir)
            removed_jobs += 1
        imagegen_dir = ensure_within(
            settings.output_dir / "imagegen" / request_id.name, settings.output_dir
        )
        if imagegen_dir.is_dir():
            shutil.rmtree(imagegen_dir)
            removed_imagegen += 1
    orphan_cutoff = cutoff - timedelta(seconds=settings.asset_ttl_seconds)
    removed_assets += _remove_old_directories(asset_root, orphan_cutoff)
    removed_jobs += _remove_old_directories(jobs_root, orphan_cutoff)
    removed_imagegen += _remove_old_directories(
        (settings.output_dir / "imagegen").resolve(), orphan_cutoff
    )
    database.mark_expired(cutoff)
    return {
        "assets": removed_assets,
        "jobs": removed_jobs,
        "imagegen": removed_imagegen,
    }


def _remove_old_directories(root: Path, cutoff: datetime) -> int:
    if not root.is_dir():
        return 0
    removed = 0
    for candidate in root.iterdir():
        if not candidate.is_dir() or candidate.is_symlink():
            continue
        safe = ensure_within(candidate, root)
        modified = datetime.fromtimestamp(safe.stat().st_mtime, UTC)
        if modified <= cutoff:
            shutil.rmtree(safe)
            removed += 1
    return removed


def main() -> None:
    result = cleanup_expired(Settings.from_env())
    print(f"removed assets={result['assets']} jobs={result['jobs']} imagegen={result['imagegen']}")
