# Vibe Editing Tool API 연동 가이드

lala API는 OpenAPI 3 문서를 직접 제공한다. 서버 실행 후 다음 화면에서 요청·응답 모델, 인증 방식, 예제와 오류 코드를 확인하고 바로 호출할 수 있다.

- Swagger UI: `GET /docs`
- ReDoc: `GET /redoc`
- OpenAPI JSON: `GET /openapi.json`
- 런타임 지원 계약: `GET /v1/capabilities`

Vibe 브라우저에서 lala를 직접 호출하지 않는다. Vercel Route Handler 또는 Server Function에서만 `LALA_API_KEY`를 읽고 `Authorization: Bearer ...` 헤더를 붙인다. 업로드용 서명 PUT URL에는 Bearer 키를 붙이지 않는다.

## 전체 흐름

| 순서 | 요청 | 성공 결과 |
|---:|---|---|
| 1 | `GET /v1/capabilities` | 지원 버전과 문서 URL |
| 2 | `POST /v1/assets/upload-requests` | `asset_id`, 짧은 수명의 `upload_url` |
| 3 | `PUT <upload_url>` | 업로드 완료 |
| 4 | `POST /v1/edit-requests` | HTTP 202, `request_id`, `status_url` |
| 5 | `GET <status_url>` | `queued`, `analyzing`, `completed`, `failed` |

## 1. 지원 계약 확인

배포 시점에 `/v1/capabilities`를 한 번 조회해 Vibe의 EditPlan·Remaster·LUT 계약과 맞는지 확인한다. 현재 추천 판단기는 항상 `hermes-llm`이며 Generate AI 실행 모드는 `openai-image-api`다. renderer는 `gpt-image-2`, `low`, PNG로 고정되며 입력 종횡비에 가장 가까운 지원 1K 크기(`1024x1024`, `1536x1024`, `1024x1536`)를 선택한다.

## 2. 업로드 URL 발급

`POST /v1/assets/upload-requests`에 파일명, MIME, 정확한 byte size와 선택적 SHA-256을 보낸다. 응답의 `upload_url`에 원본 bytes를 그대로 PUT하고 발급 요청과 같은 `Content-Type`을 사용한다. 기본 URL 수명은 15분이며 한 번만 사용할 수 있다.

## 3. 편집 요청

```json
{
  "schema_version": "1.0",
  "client_request_id": "550e8400-e29b-41d4-a716-446655440000",
  "asset_id": "asset_0123456789abcdef0123456789abcdef",
  "prompt": "노을 분위기는 유지하고 얼굴만 자연스럽게 밝게 해줘",
  "locale": "ko-KR",
  "client_capabilities": {
    "edit_plan_version": "1.0",
    "remaster_engine_version": "1.0",
    "lut_catalog_version": "2026-08-02"
  }
}
```

`POST /v1/edit-requests`는 HTTP 202를 즉시 반환한다. Hermes LLM은 이미지와 자연어 요청의 전체 의미를 판단하며, Vibe는 `status_url`을 polling한다. 네트워크 재시도에는 같은 `client_request_id`와 완전히 같은 본문을 사용한다. 같은 ID에 다른 본문을 보내면 `IDEMPOTENCY_CONFLICT`가 반환된다.

## 4. 상태 polling

`queued`와 `analyzing` 동안 지수 backoff와 jitter를 적용해 조회한다. `completed`이면 `data.plan`이 `schemas/edit-plan.schema.json`을 만족한다. `failed`이면 `error.code`, 한국어 메시지, `retryable`을 사용하고 내부 Agent 출력은 사용자에게 노출하지 않는다.

```ts
const headers = {
  Authorization: `Bearer ${process.env.LALA_API_KEY}`,
  "Content-Type": "application/json",
};

const accepted = await fetch(`${process.env.LALA_API_URL}/v1/edit-requests`, {
  method: "POST",
  headers,
  body: JSON.stringify(requestBody),
}).then((response) => response.json());

for (let attempt = 0; attempt < 20; attempt += 1) {
  const result = await fetch(accepted.data.status_url, { headers }).then((response) =>
    response.json(),
  );
  if (result.data.status === "completed") return result.data.plan;
  if (result.data.status === "failed") throw new Error(result.error.code);
  await new Promise((resolve) => setTimeout(resolve, Math.min(500 * 2 ** attempt, 5000)));
}
throw new Error("LALA_POLL_TIMEOUT");
```

## 안정된 오류 코드

주요 오류는 `INVALID_REQUEST`, `INVALID_IMAGE`, `UNSUPPORTED_FORMAT`, `ASSET_NOT_READY`, `IDEMPOTENCY_CONFLICT`, `PLAN_VALIDATION_FAILED`, `AGENT_TIMEOUT`, `RATE_LIMITED`, `INTERNAL_ERROR`다. HTTP status와 함께 `error.retryable`을 확인한다.

TypeScript 참고 타입은 `docs/api/edit-plan.ts`, 생성된 기준 계약은 `schemas/openapi.json`과 `schemas/edit-plan.schema.json`이다.
