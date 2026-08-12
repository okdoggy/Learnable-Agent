# Learnable Agent (lala)

`lala`는 Hermes Agent를 기반으로 Vibe Editing Tool과 Slack에 동일한 이미지 편집 계획을
제공하는 서비스입니다. Vibe에는 검증된 `EditPlan 1.0`을 반환하고, Slack에서는 같은 계획을
Vibe Editing 호환 LUT/Generate AI 렌더러로 실행해 결과 파일까지 전달합니다.

## 빠른 시작

Python 3.11 이상과 `uv`가 필요합니다.

```bash
uv sync --extra dev
cp .env.example .env
# .env의 replace-me, HERMES_BASE_URL, HERMES_API_KEY를 실제 값으로 교체합니다.
# Generate AI를 사용하려면 같은 파일의 LALA_IMAGEGEN_OPENAI_API_KEY도 입력하고 Hermes/MCP를 재시작합니다.
uv run lala-api
```

API 문서는 실행 후 `http://127.0.0.1:8000/docs`에서 확인할 수 있습니다. 기본 개발용 Bearer
키는 `local-development-key`이며 운영에서는 반드시 `LALA_API_KEY`와
`LALA_SIGNING_SECRET`을 별도 비밀로 설정해야 합니다.

### Generate AI 전용 key

Generate AI를 사용할 서버의 `/workspace/Learnable-Agent/.env`에 다음 한 줄을 입력합니다.

```dotenv
LALA_IMAGEGEN_OPENAI_API_KEY=실제_OpenAI_API_key
```

`.env`는 Git에서 제외되며 실제 key를 `.env.example`, YAML, 코드 또는 로그에 넣지 않습니다.
설정 후 Hermes gateway와 `lala-tools` MCP 프로세스를 재시작해야 합니다. 이 변수는 `Settings`가 로드한 뒤
`src/lala/renderers/imagegen.py`만 소비하며 Hermes planner, LUT와 cron에는 전달하지 않습니다.

Swagger UI는 `/docs`, ReDoc은 `/redoc`, OpenAPI JSON은 `/openapi.json`, Vibe 런타임 계약은
`/v1/capabilities`에서 제공합니다.

### Slack 이미지 fast path

Slack 이미지 요청은 `process_slack_image` MCP 호출 한 번으로 첨부 등록, PNG 정규화, 이미지 검사,
Hermes 계획, EditPlan 검증과 선택적 렌더링을 수행합니다. 편집 방법 문의는 `mode=recommend`, 실제
결과 요청은 `mode=edit`를 사용합니다. Slack 플랫폼에는 `skills`와 `lala-slack` toolset만 노출하며
`lala-slack`은 composite 도구 하나만 제공합니다. 따라서 운영 요청에서 저장소 탐색, terminal/Python,
임시 스크립트, source/skill 수정과 저수준 renderer 수동 조립을 할 수 없습니다.

Hermes의 Slack 첨부 cache 위치는 `LALA_SLACK_CACHE_DIR`로 지정합니다. 기본 운영 예시는
`/opt/data/cache/images`이며 Agent는 이 디렉터리의 basename만 composite 도구에 전달합니다.

3000×4000 등의 원본은 planner와 renderer 모두에서 축소하지 않습니다. 기본 asset 상한 25 MiB를
원본 PNG base64로 planner에 전달하려면 Hermes gateway 환경의 `API_SERVER_MAX_REQUEST_BYTES`를
40 MiB(`41943040`)로 설정합니다. 이 값은 1~100 MiB의 유한 범위로 검증되며, 무제한 body 허용이 아닙니다.

```bash
uv run pytest
uv run ruff check .
```

## LLM 실행 원칙

- 모든 도구 선택과 파라미터 선택은 `HERMES_BASE_URL`의 `/v1/responses`를 호출한 Hermes LLM이
  이미지 전체와 사용자 요청을 보고 판단합니다. production keyword/heuristic fallback은 없습니다.
- raw 수집은 Hermes가 web 도구로 전문가 자료를 직접 탐색하고, technical library는 Hermes가 raw의
  반복 의미를 판단해 `001-xxxx.md` 파일로 발행합니다. Python은 검증과 안전한 저장만 담당합니다.
- 지식 산출물은 Hermes 세션의 임시 작업공간에 두지 않습니다. raw는 항상 프로젝트의 `raw/`,
  중요도와 필수 기술화 여부를 판단해 발행한 문서는 항상 프로젝트의 `technical-library/`에 둡니다.
- 네 workflow skill과 reference는 실제 프롬프트 원본입니다. 실시간 요청은 versioned capability·parameter calibration registry를 읽되 전후 vision 품질 비교로 지연시키지 않습니다.
- 매일 21:00 Asia/Seoul 개발 cron은 최근 Slack 이미지 편집 세션을 오프라인 검토해 비식별 calibration 후보 보고서를 staging에 만들며 production을 즉시 자동 수정하지 않습니다. 21:10 deterministic publisher가 검증된 UTF-8 보고서만 프로젝트 `calibration/reports/`로 원자적으로 복사합니다.
- Generate AI는 이미지 생성 전용 `LALA_IMAGEGEN_OPENAI_API_KEY`로 OpenAI Image API를 호출합니다. 모델은
  `gpt-image-2`, 품질은 `low`, 출력은 PNG로 고정합니다. Slack에서 Generate AI를 선택하면 입력 종횡비에 가장 가까운
  지원 1K 해상도(`1024x1024`, `1536x1024`, `1024x1536`)를 renderer가 선택하며 Codex `$imagegen`으로 자동 fallback하지 않습니다.

Hermes 설정 예시는 `config/hermes/config.example.yaml`, Agent 말투는
`config/hermes/SOUL.md`, API 연동 절차는 `docs/api/vibe.md`에 있습니다.

## 주요 경계

- `raw/` 자료는 비신뢰 수집 데이터이며 사용자 응답의 직접 근거로 사용하지 않습니다.
- `technical-library/`의 번호형 문서에서 `status: active`인 기술만 추천 근거가 될 수 있습니다.
- 입력/중간/출력 이미지는 기본 24시간 TTL을 가지며 `lala-cleanup`으로 제거합니다.
- LUT는 `luts/manifest.yaml`에 `approved`로 등록된 ID만 실행합니다.
- 사용자 프롬프트와 보존·회피 조건은 multipart Image API 요청으로만 전달하며 API key는 로그나 결과 계약에 기록하지 않습니다.
- Markdown, YAML, JSON은 strict UTF-8로 검증하며 CI에서 깨진 문자와 U+FFFD를 거부합니다.

전체 설계와 완료 기준은 `docs/design-and-implementation-plan.md`를 참고하세요.
