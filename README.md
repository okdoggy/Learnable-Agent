# Learnable Agent (lala)

`lala`는 Hermes Agent를 기반으로 Vibe Editing Tool과 Slack에 동일한 이미지 편집 계획을
제공하는 서비스입니다. Vibe에는 검증된 `EditPlan 1.0`을 반환하고, Slack에서는 같은 계획을
Remaster/LUT/Generate AI 렌더러로 실행해 결과 파일까지 전달합니다.

## 빠른 시작

Python 3.11 이상과 `uv`가 필요합니다.

```bash
uv sync --extra dev
cp .env.example .env
# .env의 replace-me, HERMES_BASE_URL, HERMES_API_KEY를 실제 값으로 교체하고 Hermes를 시작합니다.
uv run lala-api
```

API 문서는 실행 후 `http://127.0.0.1:8000/docs`에서 확인할 수 있습니다. 기본 개발용 Bearer
키는 `local-development-key`이며 운영에서는 반드시 `LALA_API_KEY`와
`LALA_SIGNING_SECRET`을 별도 비밀로 설정해야 합니다.

Swagger UI는 `/docs`, ReDoc은 `/redoc`, OpenAPI JSON은 `/openapi.json`, Vibe 런타임 계약은
`/v1/capabilities`에서 제공합니다.

```bash
uv run pytest
uv run ruff check .
```

## LLM 실행 원칙

- 모든 도구 선택과 파라미터 선택은 `HERMES_BASE_URL`의 `/v1/responses`를 호출한 Hermes LLM이
  이미지 전체와 사용자 요청을 보고 판단합니다. production keyword/heuristic fallback은 없습니다.
- raw 수집은 Hermes가 web 도구로 전문가 자료를 직접 탐색하고, technical library는 Hermes가 raw의
  반복 의미를 판단해 `001-xxxx.md` 파일로 발행합니다. Python은 검증과 안전한 저장만 담당합니다.
- 세 Hermes skill과 planner reference는 실제 프롬프트 원본입니다. 반복된 오판이 확인되면 Hermes의
  `skill_manage` self-improvement가 작은 수정으로 발전시킬 수 있습니다.
- Generate AI는 로그인된 Codex CLI의 `$imagegen` 내장 도구를 사용합니다. 별도
  `OPENAI_API_KEY`나 Image API CLI가 필요하지 않으며 해당 경로로 자동 fallback하지 않습니다.

Hermes 설정 예시는 `config/hermes/config.example.yaml`, Agent 말투는
`config/hermes/SOUL.md`, API 연동 절차는 `docs/api/vibe.md`에 있습니다.

## 주요 경계

- `raw/` 자료는 비신뢰 수집 데이터이며 사용자 응답의 직접 근거로 사용하지 않습니다.
- `technical-library/`의 번호형 문서에서 `status: active`인 기술만 추천 근거가 될 수 있습니다.
- 입력/중간/출력 이미지는 기본 24시간 TTL을 가지며 `lala-cleanup`으로 제거합니다.
- LUT는 `luts/manifest.yaml`에 `approved`로 등록된 ID만 실행합니다.
- 사용자 프롬프트는 셸 문자열로 보간하지 않으며 Codex에는 UTF-8 stdin으로 전달합니다.
- Markdown, YAML, JSON은 strict UTF-8로 검증하며 CI에서 깨진 문자와 U+FFFD를 거부합니다.

전체 설계와 완료 기준은 `docs/design-and-implementation-plan.md`를 참고하세요.
