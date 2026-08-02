# 운영 가이드

## 배포 전

- `LALA_API_KEY`, `LALA_SIGNING_SECRET`, `HERMES_API_KEY`, Slack 토큰을 secret store에서 주입한다.
- `LALA_VAR_DIR`, `LALA_RAW_DIR`, `LALA_TECHNICAL_LIBRARY_DIR`, `LALA_OUTPUT_DIR`를 쓰기 가능한
  영속 볼륨으로 지정한다.
- Hermes 호스트와 scheduler에 `TZ=Asia/Seoul`을 설정한다.
- Hermes 서비스의 `HERMES_MODEL` 또는 `model.default`를 무인 작업에 사용할 모델로 설정한다.
  per-job override가 필요하면 등록 후 Hermes의 `cronjob` update 도구나 dashboard에서 model/provider를
  지정한다. 현재 `hermes cron create` CLI에는 해당 override flag가 없다.
- `config/hermes/config.example.yaml`을 병합하고 `lala-tools` MCP의 명시된 renderer/raw/technical
  도구만 노출한다.
- 등록 직후 Hermes의 `cronjob.update`로 수집 작업은
  `enabled_toolsets=["web","file","skills","mcp-lala-tools"]`, Curator 작업은
  `enabled_toolsets=["file","skills","mcp-lala-tools"]`로 고정한다. CLI로만 운영할 때는
  `hermes tools`의 `cron` 플랫폼을 최소 권한으로 설정하고 실행 이력에서 실제 도구 목록을 확인한다.
- `SLACK_ALLOWED_USERS`와 `slack.allowed_channels`를 실제 ID allowlist로 설정한다.
- 배포 계정으로 Codex CLI에 로그인하고 `LALA_CODEX_EXECUTABLE`이 가리키는 실행 파일에서
  `$imagegen` 내장 도구를 사용할 수 있는지 확인한다. 서비스에 `OPENAI_API_KEY`를 주입하지 않는다.
- `skills.write_approval=false`는 Hermes의 prompt self-improvement를 즉시 반영한다. 변경을 사전
  검토해야 하는 환경은 `true`로 바꾸고 `~/.hermes/pending/skills/` 승인 절차를 운영한다.
- `PYTHONUTF8=1`을 설정하고 `uv run python scripts/validate_utf8.py`를 실행한다.
- `scripts/register-hermes-cron.sh`를 실행한 뒤 두 작업을 `hermes cron run <name>`으로
  수동 검증한다. 스크립트는 같은 이름이 이미 있으면 생성을 건너뛴다.

## 장애 확인

1. API `/health`, Hermes `/health/detailed`, MCP 초기화 로그 순서로 확인한다.
2. 사용자에게 받은 `request_id`로 `lala.audit` JSON 로그를 찾는다.
3. API 프로세스 재시작 시 만료되지 않은 `queued`/`analyzing` 요청은 SQLite 상태를 기준으로
   자동 재큐잉된다. 재처리 여부를 같은 `request_id`로 확인한다.
4. `AGENT_*` 오류는 Hermes 연결/timeout을, `EXECUTION_FAILED`는 renderer 또는 Codex CLI 로그인·
   `$imagegen` 가용성을 확인한다.
5. Generate AI 실패를 Remaster로 자동 대체하지 않는다. 원래 추천과 retryable 상태를 유지한다.
6. Cron은 `hermes cron runs <name> --limit 20`으로 실행 ledger를 확인한다. Hermes 내부 DB를 직접
   조회하거나 수정하지 않는다.

## 개인정보와 정리

`uv run lala-cleanup`을 최소 매시간 실행한다. 기본 TTL 24시간 이후 `var/assets`, `var/jobs`,
`output/imagegen/<request-id>`의 이미지가 제거되고 DB에는 계획 본문을 제외한 감사용 상태와 해시만
남는다. 삭제 전 보존 요구가 있으면 TTL 정책 ADR을 먼저 승인한다.

## 외부 연동 검증

저장소에는 Codex 내장 `$imagegen`으로 실제 생성하고 편집한 저조도 fixture가 포함된다. 기본 테스트는
그 fixture와 fake `codex exec` runner로 비용 없이 계약을 검증한다. 배포 후보 환경에서는 로그인된
Codex 계정으로 `LALA_RUN_LIVE_IMAGEGEN=1 uv run pytest -m live tests/live`를 실행해 built-in
`$imagegen`과 PNG output 복사 계약을 확인한다.

Vibe 연동 문서는 `/docs`, `/redoc`, `/openapi.json`, `/v1/capabilities`에서 확인한다. 배포 후
`schemas/openapi.json`과 실제 `/openapi.json`의 주요 operation ID가 일치하는지 검사한다.
