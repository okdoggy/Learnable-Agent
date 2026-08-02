from __future__ import annotations

import hashlib
import json
import sqlite3
import threading
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from lala.domain.errors import LalaError, NotFoundError
from lala.domain.models import EditPlan

DATABASE_SCHEMA_VERSION = 2


def utc_now() -> datetime:
    return datetime.now(UTC)


def isoformat(value: datetime) -> str:
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


@dataclass(frozen=True, slots=True)
class AssetRecord:
    asset_id: str
    filename: str
    declared_mime: str
    byte_size: int
    expected_sha256: str | None
    actual_sha256: str | None
    detected_mime: str | None
    path: Path | None
    status: str
    created_at: datetime
    expires_at: datetime


@dataclass(frozen=True, slots=True)
class EditRequestRecord:
    request_id: str
    client_request_id: str
    asset_id: str
    prompt: str
    locale: str
    client_capabilities: dict[str, Any]
    status: str
    plan: EditPlan | None
    error_code: str | None
    error_message_ko: str | None
    retryable: bool | None
    created_at: datetime
    updated_at: datetime
    expires_at: datetime


class Database:
    def __init__(self, path: Path) -> None:
        self.path = path.resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_lock = threading.Lock()
        self._initialized = False

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        connection = sqlite3.connect(self.path, timeout=30)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA busy_timeout = 30000")
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def initialize(self) -> None:
        if self._initialized:
            return
        with self._init_lock:
            if self._initialized:
                return
            with self.connect() as connection:
                current_version = int(connection.execute("PRAGMA user_version").fetchone()[0])
                if current_version > DATABASE_SCHEMA_VERSION:
                    raise LalaError(
                        "DATABASE_VERSION_UNSUPPORTED",
                        "현재 애플리케이션보다 새로운 상태 DB입니다.",
                        False,
                    )
                connection.executescript(
                    """
                    PRAGMA journal_mode = WAL;
                    CREATE TABLE IF NOT EXISTS assets (
                        asset_id TEXT PRIMARY KEY,
                        filename TEXT NOT NULL,
                        declared_mime TEXT NOT NULL,
                        byte_size INTEGER NOT NULL,
                        expected_sha256 TEXT,
                        actual_sha256 TEXT,
                        detected_mime TEXT,
                        path TEXT,
                        status TEXT NOT NULL,
                        created_at TEXT NOT NULL,
                        expires_at TEXT NOT NULL
                    );
                    CREATE TABLE IF NOT EXISTS edit_requests (
                        request_id TEXT PRIMARY KEY,
                        client_request_id TEXT NOT NULL UNIQUE,
                        request_fingerprint TEXT NOT NULL,
                        asset_id TEXT NOT NULL REFERENCES assets(asset_id),
                        prompt TEXT NOT NULL,
                        locale TEXT NOT NULL,
                        capabilities_json TEXT NOT NULL,
                        status TEXT NOT NULL,
                        plan_json TEXT,
                        error_code TEXT,
                        error_message_ko TEXT,
                        retryable INTEGER,
                        created_at TEXT NOT NULL,
                        updated_at TEXT NOT NULL,
                        expires_at TEXT NOT NULL
                    );
                    CREATE INDEX IF NOT EXISTS edit_requests_status_idx
                    ON edit_requests(status, created_at);
                    CREATE TABLE IF NOT EXISTS raw_scenarios (
                        scenario_id TEXT PRIMARY KEY,
                        canonical_url TEXT NOT NULL,
                        url_hash TEXT NOT NULL,
                        content_hash TEXT NOT NULL,
                        fingerprint TEXT NOT NULL,
                        path TEXT NOT NULL UNIQUE,
                        created_at TEXT NOT NULL,
                        UNIQUE(content_hash),
                        UNIQUE(canonical_url, fingerprint)
                    );
                    """
                )
                if current_version < 2:
                    connection.execute("DROP TABLE IF EXISTS curator_processed")
                connection.execute(f"PRAGMA user_version = {DATABASE_SCHEMA_VERSION}")
            self._initialized = True

    def create_asset(
        self,
        *,
        asset_id: str,
        filename: str,
        declared_mime: str,
        byte_size: int,
        expected_sha256: str | None,
        ttl_seconds: int,
    ) -> AssetRecord:
        self.initialize()
        now = utc_now()
        expires = now + timedelta(seconds=ttl_seconds)
        with self.connect() as connection:
            connection.execute(
                """
                INSERT INTO assets(
                    asset_id, filename, declared_mime, byte_size, expected_sha256,
                    status, created_at, expires_at
                ) VALUES (?, ?, ?, ?, ?, 'awaiting_upload', ?, ?)
                """,
                (
                    asset_id,
                    filename,
                    declared_mime,
                    byte_size,
                    expected_sha256,
                    isoformat(now),
                    isoformat(expires),
                ),
            )
        return self.get_asset(asset_id)

    def get_asset(self, asset_id: str) -> AssetRecord:
        self.initialize()
        with self.connect() as connection:
            row = connection.execute(
                "SELECT * FROM assets WHERE asset_id = ?", (asset_id,)
            ).fetchone()
        if row is None:
            raise NotFoundError("업로드 자산을 찾을 수 없습니다.")
        return _asset_from_row(row)

    def mark_asset_uploaded(
        self, asset_id: str, *, path: Path, actual_sha256: str, detected_mime: str
    ) -> AssetRecord:
        self.initialize()
        with self.connect() as connection:
            cursor = connection.execute(
                """
                UPDATE assets
                SET path = ?, actual_sha256 = ?, detected_mime = ?, status = 'uploaded'
                WHERE asset_id = ? AND status = 'awaiting_upload'
                """,
                (str(path.resolve()), actual_sha256, detected_mime, asset_id),
            )
            if cursor.rowcount != 1:
                row = connection.execute(
                    "SELECT status FROM assets WHERE asset_id = ?", (asset_id,)
                ).fetchone()
                if row is None:
                    raise NotFoundError("업로드 자산을 찾을 수 없습니다.")
                raise LalaError("ASSET_STATE_CONFLICT", "이미 업로드된 자산입니다.", False)
        return self.get_asset(asset_id)

    def create_or_get_edit_request(
        self,
        *,
        request_id: str,
        client_request_id: str,
        asset_id: str,
        prompt: str,
        locale: str,
        client_capabilities: dict[str, Any],
        ttl_seconds: int,
    ) -> tuple[EditRequestRecord, bool]:
        self.initialize()
        payload = {
            "asset_id": asset_id,
            "prompt": prompt,
            "locale": locale,
            "client_capabilities": client_capabilities,
        }
        fingerprint = hashlib.sha256(
            json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        now = utc_now()
        expires = now + timedelta(seconds=ttl_seconds)
        capabilities_json = json.dumps(client_capabilities, ensure_ascii=False, sort_keys=True)
        with self.connect() as connection:
            try:
                connection.execute(
                    """
                    INSERT INTO edit_requests(
                        request_id, client_request_id, request_fingerprint, asset_id,
                        prompt, locale, capabilities_json, status, created_at, updated_at,
                        expires_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, 'queued', ?, ?, ?)
                    """,
                    (
                        request_id,
                        client_request_id,
                        fingerprint,
                        asset_id,
                        prompt,
                        locale,
                        capabilities_json,
                        isoformat(now),
                        isoformat(now),
                        isoformat(expires),
                    ),
                )
                created = True
            except sqlite3.IntegrityError:
                row = connection.execute(
                    """
                    SELECT request_id, request_fingerprint
                    FROM edit_requests WHERE client_request_id = ?
                    """,
                    (client_request_id,),
                ).fetchone()
                if row is None or row["request_fingerprint"] != fingerprint:
                    raise LalaError(
                        "IDEMPOTENCY_CONFLICT",
                        "같은 client_request_id에 다른 요청 내용이 사용되었습니다.",
                        False,
                    ) from None
                request_id = row["request_id"]
                created = False
        return self.get_edit_request(request_id), created

    def get_edit_request(self, request_id: str) -> EditRequestRecord:
        self.initialize()
        with self.connect() as connection:
            row = connection.execute(
                "SELECT * FROM edit_requests WHERE request_id = ?", (request_id,)
            ).fetchone()
        if row is None:
            raise NotFoundError("편집 요청을 찾을 수 없습니다.")
        return _edit_request_from_row(row)

    def requeue_incomplete_requests(self) -> list[str]:
        self.initialize()
        now = isoformat(utc_now())
        with self.connect() as connection:
            connection.execute(
                """
                UPDATE edit_requests SET status = 'queued', updated_at = ?
                WHERE status = 'analyzing' AND expires_at > ?
                """,
                (now, now),
            )
            rows = connection.execute(
                """
                SELECT request_id FROM edit_requests
                WHERE status = 'queued' AND expires_at > ?
                ORDER BY created_at
                """,
                (now,),
            ).fetchall()
        return [str(row["request_id"]) for row in rows]

    def transition_request(self, request_id: str, *, expected: str, target: str) -> bool:
        now = isoformat(utc_now())
        with self.connect() as connection:
            cursor = connection.execute(
                """
                UPDATE edit_requests SET status = ?, updated_at = ?
                WHERE request_id = ? AND status = ?
                """,
                (target, now, request_id, expected),
            )
        return cursor.rowcount == 1

    def complete_request(self, request_id: str, plan: EditPlan) -> None:
        now = isoformat(utc_now())
        with self.connect() as connection:
            cursor = connection.execute(
                """
                UPDATE edit_requests
                SET status = 'completed', plan_json = ?, error_code = NULL,
                    error_message_ko = NULL, retryable = NULL, updated_at = ?
                WHERE request_id = ? AND status = 'analyzing'
                """,
                (plan.model_dump_json(), now, request_id),
            )
            if cursor.rowcount != 1:
                raise LalaError("REQUEST_STATE_CONFLICT", "요청 상태가 변경되었습니다.", True)

    def fail_request(self, request_id: str, *, code: str, message_ko: str, retryable: bool) -> None:
        now = isoformat(utc_now())
        with self.connect() as connection:
            connection.execute(
                """
                UPDATE edit_requests
                SET status = 'failed', error_code = ?, error_message_ko = ?,
                    retryable = ?, updated_at = ?
                WHERE request_id = ? AND status IN ('queued', 'analyzing')
                """,
                (code, message_ko, int(retryable), now, request_id),
            )

    def expired_paths(self, before: datetime) -> tuple[list[Path], list[Path]]:
        self.initialize()
        cutoff = isoformat(before)
        with self.connect() as connection:
            asset_rows = connection.execute(
                "SELECT path FROM assets WHERE expires_at <= ? AND path IS NOT NULL", (cutoff,)
            ).fetchall()
            request_rows = connection.execute(
                "SELECT request_id FROM edit_requests WHERE expires_at <= ?", (cutoff,)
            ).fetchall()
        assets = [Path(row["path"]) for row in asset_rows]
        jobs = [Path(row["request_id"]) for row in request_rows]
        return assets, jobs

    def mark_expired(self, before: datetime) -> None:
        self.initialize()
        cutoff = isoformat(before)
        with self.connect() as connection:
            connection.execute(
                """
                UPDATE assets
                SET status = 'expired', path = NULL, filename = ''
                WHERE expires_at <= ?
                """,
                (cutoff,),
            )
            connection.execute(
                """
                UPDATE edit_requests
                SET status = 'failed',
                    prompt = '',
                    plan_json = NULL,
                    error_code = 'EXPIRED',
                    error_message_ko = '요청이 만료되었습니다.',
                    retryable = 0
                WHERE expires_at <= ?
                """,
                (cutoff,),
            )


def _parse_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _asset_from_row(row: sqlite3.Row) -> AssetRecord:
    return AssetRecord(
        asset_id=row["asset_id"],
        filename=row["filename"],
        declared_mime=row["declared_mime"],
        byte_size=row["byte_size"],
        expected_sha256=row["expected_sha256"],
        actual_sha256=row["actual_sha256"],
        detected_mime=row["detected_mime"],
        path=Path(row["path"]) if row["path"] else None,
        status=row["status"],
        created_at=_parse_datetime(row["created_at"]),
        expires_at=_parse_datetime(row["expires_at"]),
    )


def _edit_request_from_row(row: sqlite3.Row) -> EditRequestRecord:
    plan = EditPlan.model_validate_json(row["plan_json"], strict=True) if row["plan_json"] else None
    return EditRequestRecord(
        request_id=row["request_id"],
        client_request_id=row["client_request_id"],
        asset_id=row["asset_id"],
        prompt=row["prompt"],
        locale=row["locale"],
        client_capabilities=json.loads(row["capabilities_json"]),
        status=row["status"],
        plan=plan,
        error_code=row["error_code"],
        error_message_ko=row["error_message_ko"],
        retryable=bool(row["retryable"]) if row["retryable"] is not None else None,
        created_at=_parse_datetime(row["created_at"]),
        updated_at=_parse_datetime(row["updated_at"]),
        expires_at=_parse_datetime(row["expires_at"]),
    )
