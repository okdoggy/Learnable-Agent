from __future__ import annotations

from datetime import UTC, datetime

from lala.config import Settings
from lala.storage.cleanup import cleanup_expired
from lala.storage.database import Database


def test_cleanup_removes_expired_assets_jobs_and_generate_outputs(settings: Settings) -> None:
    database = Database(settings.database_path)
    asset_id = "asset_cleanup"
    request_id = "req_cleanup"
    asset_dir = settings.var_dir / "assets" / asset_id
    asset_dir.mkdir(parents=True)
    asset_path = asset_dir / "original.png"
    asset_path.write_bytes(b"expired")
    database.create_asset(
        asset_id=asset_id,
        filename="original.png",
        declared_mime="image/png",
        byte_size=7,
        expected_sha256=None,
        ttl_seconds=-1,
    )
    database.mark_asset_uploaded(
        asset_id,
        path=asset_path,
        actual_sha256="0" * 64,
        detected_mime="image/png",
    )
    database.create_or_get_edit_request(
        request_id=request_id,
        client_request_id="cleanup-client-request",
        asset_id=asset_id,
        prompt="만료 테스트",
        locale="ko-KR",
        client_capabilities={
            "edit_plan_version": "1.0",
            "remaster_engine_version": "1.0",
            "lut_catalog_version": "2026-08-02",
        },
        ttl_seconds=-1,
    )
    job_dir = settings.var_dir / "jobs" / request_id
    imagegen_dir = settings.output_dir / "imagegen" / request_id
    job_dir.mkdir(parents=True)
    imagegen_dir.mkdir(parents=True)
    (job_dir / "input.png").write_bytes(b"expired")
    (imagegen_dir / "result.png").write_bytes(b"expired")

    result = cleanup_expired(settings, now=datetime.now(UTC))

    assert result == {"assets": 1, "jobs": 1, "imagegen": 1}
    assert not asset_dir.exists()
    assert not job_dir.exists()
    assert not imagegen_dir.exists()
    asset = database.get_asset(asset_id)
    assert asset.status == "expired"
    assert asset.filename == ""
    request = database.get_edit_request(request_id)
    assert request.status == "failed"
    assert request.error_code == "EXPIRED"
    assert request.retryable is False
    assert request.prompt == ""


def test_cleanup_initializes_a_fresh_database(settings: Settings) -> None:
    settings.database_path.unlink(missing_ok=True)

    result = cleanup_expired(settings)

    assert result == {"assets": 0, "jobs": 0, "imagegen": 0}
