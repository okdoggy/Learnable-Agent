from __future__ import annotations

import base64
import hashlib
import hmac
import os
import re
import tempfile
import time
import uuid
from dataclasses import dataclass
from pathlib import Path

from lala.config import Settings
from lala.domain.errors import LalaError
from lala.renderers.image_io import SUPPORTED_MIME, ImageAssetValidator
from lala.storage.database import AssetRecord, Database
from lala.storage.workspace import ensure_within

SHA256_PATTERN = re.compile(r"^[0-9a-fA-F]{64}$")


@dataclass(frozen=True, slots=True)
class UploadRequest:
    asset_id: str
    upload_url: str
    expires_at_epoch: int
    method: str = "PUT"


class AssetService:
    def __init__(self, settings: Settings, database: Database) -> None:
        self.settings = settings
        self.database = database
        self.asset_root = (settings.var_dir / "assets").resolve()
        self.asset_root.mkdir(parents=True, exist_ok=True)
        self.validator = ImageAssetValidator(
            max_bytes=settings.max_asset_bytes, max_pixels=settings.max_image_pixels
        )

    def create_upload_request(
        self,
        *,
        filename: str,
        mime: str,
        byte_size: int,
        sha256: str | None,
    ) -> UploadRequest:
        mime = mime.lower().strip()
        if mime not in SUPPORTED_MIME:
            raise LalaError("UNSUPPORTED_FORMAT", "지원하지 않는 이미지 MIME 형식입니다.", False)
        if byte_size <= 0 or byte_size > self.settings.max_asset_bytes:
            raise LalaError("INVALID_IMAGE", "이미지 파일 크기가 허용 범위를 벗어났습니다.", False)
        if sha256 is not None and not SHA256_PATTERN.fullmatch(sha256):
            raise LalaError("INVALID_REQUEST", "SHA-256 형식이 올바르지 않습니다.", False)
        safe_filename = Path(filename).name.strip()
        if not safe_filename or len(safe_filename) > 255:
            raise LalaError("INVALID_REQUEST", "파일명이 올바르지 않습니다.", False)
        asset_id = f"asset_{uuid.uuid4().hex}"
        self.database.create_asset(
            asset_id=asset_id,
            filename=safe_filename,
            declared_mime=mime,
            byte_size=byte_size,
            expected_sha256=sha256.lower() if sha256 else None,
            ttl_seconds=self.settings.asset_ttl_seconds,
        )
        expires = int(time.time()) + self.settings.upload_url_ttl_seconds
        token = self._sign(asset_id, expires)
        return UploadRequest(
            asset_id=asset_id,
            upload_url=(
                f"{self.settings.public_base_url}/v1/assets/{asset_id}/content"
                f"?expires={expires}&token={token}"
            ),
            expires_at_epoch=expires,
        )

    def store_upload(
        self,
        *,
        asset_id: str,
        expires: int,
        token: str,
        content: bytes,
        content_type: str,
    ) -> AssetRecord:
        if not self.settings.enable_local_uploads:
            raise LalaError("LOCAL_UPLOAD_DISABLED", "로컬 업로드가 비활성화되어 있습니다.", False)
        self._verify(asset_id, expires, token)
        record = self.database.get_asset(asset_id)
        if record.status != "awaiting_upload":
            raise LalaError("ASSET_STATE_CONFLICT", "이미 업로드된 자산입니다.", False)
        if len(content) > self.settings.max_asset_bytes:
            raise LalaError("INVALID_IMAGE", "이미지 파일이 너무 큽니다.", False)
        if content_type.split(";", 1)[0].strip().lower() != record.declared_mime:
            raise LalaError("INVALID_IMAGE", "업로드 Content-Type이 요청과 다릅니다.", False)
        asset_dir = ensure_within(self.asset_root / asset_id, self.asset_root)
        asset_dir.mkdir(parents=True, exist_ok=True)
        descriptor, temporary_name = tempfile.mkstemp(
            prefix="upload-", suffix=".tmp", dir=asset_dir
        )
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            validated = self.validator.validate(
                temporary,
                declared_mime=record.declared_mime,
                expected_sha256=record.expected_sha256,
                expected_bytes=record.byte_size,
            )
            extension = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}[
                validated.mime
            ]
            destination = ensure_within(asset_dir / f"original{extension}", asset_dir)
            os.replace(temporary, destination)
            return self.database.mark_asset_uploaded(
                asset_id,
                path=destination,
                actual_sha256=validated.sha256,
                detected_mime=validated.mime,
            )
        finally:
            temporary.unlink(missing_ok=True)

    def _sign(self, asset_id: str, expires: int) -> str:
        payload = f"{asset_id}:{expires}".encode()
        digest = hmac.new(self.settings.signing_secret.encode(), payload, hashlib.sha256).digest()
        return base64.urlsafe_b64encode(digest).rstrip(b"=").decode()

    def _verify(self, asset_id: str, expires: int, token: str) -> None:
        if expires < int(time.time()):
            raise LalaError("UPLOAD_URL_EXPIRED", "업로드 URL이 만료되었습니다.", False)
        if expires > int(time.time()) + self.settings.upload_url_ttl_seconds + 60:
            raise LalaError("INVALID_UPLOAD_TOKEN", "업로드 서명이 올바르지 않습니다.", False)
        expected = self._sign(asset_id, expires)
        if not hmac.compare_digest(expected, token):
            raise LalaError("INVALID_UPLOAD_TOKEN", "업로드 서명이 올바르지 않습니다.", False)
