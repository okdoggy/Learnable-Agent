from __future__ import annotations

import hashlib
import time
import urllib.parse
from dataclasses import replace

from fastapi.testclient import TestClient

from lala.api.app import create_app
from lala.config import Settings
from lala.storage.database import Database
from tests.fakes import StaticRemasterPlanner

AUTH = {"Authorization": "Bearer local-development-key"}


def _client(settings: Settings) -> TestClient:
    return TestClient(create_app(settings, planner=StaticRemasterPlanner()))


def _upload(client: TestClient, payload: bytes) -> str:
    response = client.post(
        "/v1/assets/upload-requests",
        headers=AUTH,
        json={
            "filename": "input.png",
            "mime": "image/png",
            "byte_size": len(payload),
        },
    )
    assert response.status_code == 200
    data = response.json()["data"]
    upload_url = urllib.parse.urlsplit(data["upload_url"])
    uploaded = client.put(
        f"{upload_url.path}?{upload_url.query}",
        headers={"Content-Type": "image/png"},
        content=payload,
    )
    assert uploaded.status_code == 200
    return data["asset_id"]


def _request(asset_id: str, client_request_id: str = "client-request-123") -> dict[str, object]:
    return {
        "schema_version": "1.0",
        "client_request_id": client_request_id,
        "asset_id": asset_id,
        "prompt": "얼굴을 자연스럽게 밝게 해줘",
        "locale": "ko-KR",
        "client_capabilities": {
            "edit_plan_version": "1.0",
            "remaster_engine_version": "1.0",
            "lut_catalog_version": "2026-08-12",
        },
    }


def test_api_requires_bearer_auth(settings: Settings) -> None:
    client = _client(settings)
    response = client.post(
        "/v1/assets/upload-requests",
        json={"filename": "x.png", "mime": "image/png", "byte_size": 10},
    )
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "UNAUTHORIZED"


def test_vibe_interactive_documentation_and_capabilities(settings: Settings) -> None:
    client = _client(settings)

    assert client.get("/docs").status_code == 200
    assert client.get("/redoc").status_code == 200
    openapi = client.get("/openapi.json").json()
    assert openapi["info"]["title"] == "lala API"
    assert openapi["paths"]["/v1/edit-requests"]["post"]["operationId"] == ("createEditRequest")
    response = client.get("/v1/capabilities", headers=AUTH)
    assert response.status_code == 200
    assert response.json()["data"]["planner"] == "hermes-llm"
    assert response.json()["data"]["imagegen_execution_modes"] == ["openai-image-api"]


def test_async_edit_contract_completes_with_valid_plan(
    settings: Settings, png_bytes: bytes
) -> None:
    client = _client(settings)
    asset_id = _upload(client, png_bytes)

    accepted = client.post("/v1/edit-requests", headers=AUTH, json=_request(asset_id))

    assert accepted.status_code == 202
    request_id = accepted.json()["data"]["request_id"]
    status_response = client.get(f"/v1/edit-requests/{request_id}", headers=AUTH)
    assert status_response.status_code == 200
    body = status_response.json()
    assert body["data"]["status"] == "completed"
    assert body["data"]["plan"]["request_id"] == request_id
    assert body["data"]["plan"]["steps"][0]["tool"] == "lut"
    assert body["error"] is None


def test_idempotency_replays_same_request_and_rejects_changed_payload(
    settings: Settings, png_bytes: bytes
) -> None:
    client = _client(settings)
    asset_id = _upload(client, png_bytes)
    payload = _request(asset_id)
    first = client.post("/v1/edit-requests", headers=AUTH, json=payload)
    second = client.post("/v1/edit-requests", headers=AUTH, json=payload)
    changed = dict(payload)
    changed["prompt"] = "완전히 어둡게 해줘"
    conflict = client.post("/v1/edit-requests", headers=AUTH, json=changed)

    assert first.json()["data"]["request_id"] == second.json()["data"]["request_id"]
    assert conflict.status_code == 409
    assert conflict.json()["error"]["code"] == "IDEMPOTENCY_CONFLICT"


def test_upload_rejects_non_image_bytes(settings: Settings) -> None:
    client = _client(settings)
    payload = b"not an image"
    response = client.post(
        "/v1/assets/upload-requests",
        headers=AUTH,
        json={"filename": "input.png", "mime": "image/png", "byte_size": len(payload)},
    )
    upload_url = urllib.parse.urlsplit(response.json()["data"]["upload_url"])
    uploaded = client.put(
        f"{upload_url.path}?{upload_url.query}",
        headers={"Content-Type": "image/png"},
        content=payload,
    )
    assert uploaded.status_code == 400
    assert uploaded.json()["error"]["code"] == "INVALID_IMAGE"


def test_api_rate_limit_uses_stable_error_contract(settings: Settings) -> None:
    configured = replace(settings, rate_limit_per_minute=1)
    client = _client(configured)
    body = {"filename": "x.png", "mime": "image/png", "byte_size": 10}

    first = client.post("/v1/assets/upload-requests", headers=AUTH, json=body)
    limited = client.post("/v1/assets/upload-requests", headers=AUTH, json=body)

    assert first.status_code == 200
    assert limited.status_code == 429
    assert limited.json()["error"] == {
        "code": "RATE_LIMITED",
        "message_ko": "API 요청 한도에 도달했습니다. 잠시 후 다시 시도해 주세요.",
        "retryable": True,
    }


def test_api_rejects_unsupported_client_contract_version(settings: Settings) -> None:
    client = _client(settings)
    body = {
        "schema_version": "1.0",
        "client_request_id": "unsupported-client",
        "asset_id": "asset_0123456789abcdef0123456789abcdef",
        "prompt": "밝게 해줘",
        "locale": "ko-KR",
        "client_capabilities": {
            "edit_plan_version": "0.9",
            "remaster_engine_version": "1.0",
            "lut_catalog_version": "2026-08-12",
        },
    }

    response = client.post("/v1/edit-requests", headers=AUTH, json=body)

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "INVALID_REQUEST"


def test_startup_requeues_an_interrupted_request(settings: Settings, png_bytes: bytes) -> None:
    database = Database(settings.database_path)
    asset_id = "asset_0123456789abcdef0123456789abcdef"
    request_id = "req_recovered"
    asset_path = settings.var_dir / "assets" / asset_id / "original.png"
    asset_path.parent.mkdir(parents=True)
    asset_path.write_bytes(png_bytes)
    digest = hashlib.sha256(png_bytes).hexdigest()
    database.create_asset(
        asset_id=asset_id,
        filename="input.png",
        declared_mime="image/png",
        byte_size=len(png_bytes),
        expected_sha256=digest,
        ttl_seconds=3600,
    )
    database.mark_asset_uploaded(
        asset_id,
        path=asset_path,
        actual_sha256=digest,
        detected_mime="image/png",
    )
    database.create_or_get_edit_request(
        request_id=request_id,
        client_request_id="recovery-client-request",
        asset_id=asset_id,
        prompt="자연스럽게 밝게 해줘",
        locale="ko-KR",
        client_capabilities={
            "edit_plan_version": "1.0",
            "remaster_engine_version": "1.0",
            "lut_catalog_version": "2026-08-12",
        },
        ttl_seconds=3600,
    )
    assert database.transition_request(request_id, expected="queued", target="analyzing")

    with _client(settings) as client:
        for _ in range(100):
            response = client.get(f"/v1/edit-requests/{request_id}", headers=AUTH)
            if response.json()["data"]["status"] == "completed":
                break
            time.sleep(0.01)

    assert response.json()["data"]["status"] == "completed"
    assert response.json()["data"]["plan"]["request_id"] == request_id
