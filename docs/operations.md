# 운영 가이드

## 배포 전

- `LALA_API_KEY`, `LALA_SIGNING_SECRET`, `HERMES_API_KEY`, `LALA_IMAGEGEN_OPENAI_API_KEY`, Slack 토큰을 secret store에서 주입한다. `LALA_IMAGEGEN_OPENAI_API_KEY`는 Generate AI에만 사용한다.
- `LALA_PROJECT_ROOT`를 저장소의 절대 경로로 지정하고 `LALA_SLACK_CACHE_DIR`를 Hermes가 첨부를
  저장하는 cache root(기본 운영값 `/opt/data/cache/images`)로 지정한다.
- `LALA_MAX_ASSET_BYTES=25 MiB` 정책을 유지하는 경우 Hermes gateway 환경에
  `API_SERVER_MAX_REQUEST_BYTES=41943040`(40 MiB)을 설정한다. planner는 원본 PNG를 base64로
  전달하므로 25 MiB 원본은 약 33.4 MiB로 늘어난다. 이 상한은 무제한이 아니며 1~100 MiB 범위만 허용한다.
  원본 해상도·바이트를 preview로 축소하지 않고, renderer와 planner 모두 정규화된 원본을 사용한다.
- 프로젝트의 `raw/`와
  `technical-library/`를 쓰기 가능한 영속 경로로 유지한다. 두 지식 경로는 Hermes 임시 폴더나
  별도 환경변수로 변경하지 않는다. `LALA_VAR_DIR`, `LALA_OUTPUT_DIR`만 필요에 따라 영속 볼륨으로
  지정한다.
- Hermes 호스트와 scheduler에 `TZ=Asia/Seoul`을 설정한다.
- Hermes 서비스의 `HERMES_MODEL` 또는 `model.default`를 무인 작업에 사용할 모델로 설정한다.
  per-job override가 필요하면 등록 후 Hermes의 `cronjob` update 도구나 dashboard에서 model/provider를
  지정한다. 현재 `hermes cron create` CLI에는 해당 override flag가 없다.
- `config/hermes/config.example.yaml`을 병합한다. Slack은 `platform_toolsets.slack=[skills,lala-slack]`로
  제한하고 `lala-slack` MCP에는 `process_slack_image`만 노출한다. 개발·Vibe·knowledge용
  `lala-tools`의 저수준 renderer/raw/technical 도구를 Slack에 노출하지 않는다. 내부 EditPlan
  planner가 사용하는 API server는 `platform_toolsets.api_server=[no_mcp]`로 제한해 skill/MCP 재호출 없이
  제공된 이미지·technical context에서 JSON 계획만 반환하게 한다.
- 등록 직후 Hermes의 `cronjob.update`로 수집 작업은
  `enabled_toolsets=["web","file","skills","mcp-lala-tools"]`, Curator 작업은
  `enabled_toolsets=["file","skills","mcp-lala-tools"]`, 21시 calibration reviewer는
  `enabled_toolsets=["file","skills","session_search","vision","mcp-lala-tools"]`로 고정한다. 21:10 report publisher는 `no_agent=true`로 실행한다. CLI로만 운영할 때는
  `hermes tools`의 `cron` 플랫폼을 최소 권한으로 설정하고 실행 이력에서 실제 도구 목록을 확인한다.
- `SLACK_ALLOWED_USERS`와 `slack.allowed_channels`를 실제 ID allowlist로 설정한다.
- 프로젝트 `.env` 또는 배포 secret store에 `LALA_IMAGEGEN_OPENAI_API_KEY`를 주입하고 Hermes/MCP 프로세스를
  재시작한다. key 값은 저장소, 로그, EditPlan과 감사 이벤트에 기록하지 않는다.
- `skills.write_approval=false`는 Hermes의 prompt self-improvement를 즉시 반영한다. 변경을 사전
  검토해야 하는 환경은 `true`로 바꾸고 `~/.hermes/pending/skills/` 승인 절차를 운영한다.
- `PYTHONUTF8=1`을 설정하고 `uv run python scripts/validate_utf8.py`를 실행한다.
- `scripts/register-hermes-cron.sh`를 실행한 뒤 네 작업을 `hermes cron run <name>`으로
  수동 검증한다. 반환된 raw 경로가 `<LALA_PROJECT_ROOT>/raw/`, technical 경로가
  `<LALA_PROJECT_ROOT>/technical-library/`, calibration 보고서가 `<LALA_PROJECT_ROOT>/calibration/reports/`
  아래인지 확인한다. 스크립트는 같은 이름이 이미 있으면 생성을 건너뛴다.
- `lala-calibration-reviewer`는 매일 21:00 Asia/Seoul에 최대 5개 세션만 검토하고 production을
  수정하지 않는다. file-tool safe root 안의 `/opt/data/calibration-staging/`에 보고서를 쓰고,
  `lala-calibration-report-publisher`가 21:10에 UTF-8/U+FFFD와 동명 충돌을 검사한 뒤 프로젝트로
  원자적으로 복사한다. `lala-cleanup`은 reviewer와 publisher 모두와 경합하지 않게 오프셋한다.

## Slack fast path 검증

1. `hermes mcp test lala-slack`에서 `process_slack_image` 하나만 노출되는지 확인한다.
2. `hermes config`에서 `platform_toolsets.slack`이 `skills`, `lala-slack` 두 항목인지 확인한다.
3. gateway를 재시작한 뒤 새 Slack thread에서 이미지와 메시지를 보낸다. 정상 경로는 skill load,
   `process_slack_image` 한 번, 최종 응답만 보여야 한다.
4. trace에 `read_file`, `terminal`, `execute_code`, `inspect_image`, 개별 technical note 조회 또는
   `apply_*`가 보이면 운영 fast path 이탈로 간주한다.
5. composite 오류는 request ID로 audit를 확인한다. 운영 thread에서 코드 탐색이나 fallback script를
   실행하지 않는다.

## 장애 확인

1. API `/health`, Hermes `/health/detailed`, MCP 초기화 로그 순서로 확인한다.
2. 사용자에게 받은 `request_id`로 `lala.audit` JSON 로그를 찾는다.
3. API 프로세스 재시작 시 만료되지 않은 `queued`/`analyzing` 요청은 SQLite 상태를 기준으로
   자동 재큐잉된다. 재처리 여부를 같은 `request_id`로 확인한다.
4. `AGENT_*` 오류는 Hermes 연결/timeout을 확인한다. Generate AI의 `EXECUTION_FAILED`는
   `LALA_IMAGEGEN_OPENAI_API_KEY`, OpenAI Image API HTTP 상태, timeout과 rate limit을 확인하되 key 값은 로그에 출력하지 않는다.
5. Generate AI 실패를 Remaster로 자동 대체하지 않는다. 원래 추천과 retryable 상태를 유지한다.
6. Cron은 `hermes cron runs <name> --limit 20`으로 실행 ledger를 확인한다. Hermes 내부 DB를 직접
   조회하거나 수정하지 않는다.
7. 21시 reviewer가 실패하면 서비스 요청에는 영향이 없다. 다음 실행에서 마지막 성공 보고서의 cursor부터
   재개하며, TTL로 이미지가 사라진 요청은 `unreviewable`로 기록하고 반복 vision 호출을 하지 않는다.

## 개인정보와 정리

`uv run lala-cleanup`을 최소 매시간 실행한다. 기본 TTL 24시간 이후 `var/assets`, `var/jobs`,
`output/imagegen/<request-id>`의 이미지가 제거되고 DB에는 계획 본문을 제외한 감사용 상태와 해시만
남는다. 삭제 전 보존 요구가 있으면 TTL 정책 ADR을 먼저 승인한다.

## 외부 연동 검증

저장소에는 사용자 데이터가 아닌 저조도 imagegen 회귀 fixture가 포함된다. 기본 테스트는 해당 fixture와
`httpx.MockTransport`로 `gpt-image-2`, `low`, `1024x1024`, multipart와 PNG metadata 제거 계약을
비용 없이 검증한다. 배포 후보 환경에서는 `LALA_IMAGEGEN_OPENAI_API_KEY`를 secret으로 주입한 뒤에만
`LALA_RUN_LIVE_IMAGEGEN=1 uv run pytest -m live tests/live`를 실행한다. 이 opt-in 검증은 실제 API 비용이 발생한다.

Vibe 연동 문서는 `/docs`, `/redoc`, `/openapi.json`, `/v1/capabilities`에서 확인한다. 배포 후
`schemas/openapi.json`과 실제 `/openapi.json`의 주요 operation ID가 일치하는지 검사한다.
