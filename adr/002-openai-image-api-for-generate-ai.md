---
status: accepted
date: 2026-08-07
deciders: [user, hermes]
supersedes: [AGENTS.md rule 7, Codex-only Generate AI design]
---

# ADR-002: Generate AI는 OpenAI Image API의 gpt-image-2를 사용한다

## 배경

Codex CLI의 내장 `$imagegen` 경로는 executable, Codex 로그인 상태, workspace handoff와 장시간
subprocess timeout에 의존해 Slack 이미지 생성 요청에서 간헐적으로 실패했다. 사용자는 이미지
생성·편집 요청에만 별도의 GPT API key를 사용하고 `gpt-image-2`, low quality, 1K 출력을 원한다.

## 결정

1. `generate_ai` 실행은 Codex CLI가 아니라 OpenAI `POST /v1/images/edits`를 직접 호출한다.
2. model은 `gpt-image-2`, quality는 `low`, size는 `1024x1024`, output format은 PNG로 고정한다.
3. 자격증명은 `LALA_IMAGEGEN_OPENAI_API_KEY` 환경변수로만 주입한다. key는 plan, 결과, 오류 또는 감사 로그에
   기록하지 않으며 Remaster, LUT, planner와 지식 수집에는 전달하지 않는다.
4. API key가 없으면 서비스 시작 전체를 막지 않고 Generate AI 요청만 한국어 비재시도 오류로 실패한다.
5. 429, 5xx와 transport timeout만 제한적으로 재시도한다. 정책·인증·잘못된 요청 오류는 재시도하지 않는다.
6. API 응답의 base64 이미지는 허용된 output 경로에 PNG로 저장한 뒤 기존 normalize·metadata 제거와
   해상도·파일 검증을 통과해야 사용자에게 전달한다.
7. Codex runner와 `LALA_CODEX_EXECUTABLE` 운영 경로는 제거한다. 자동 fallback은 두지 않는다.

## 결과

- Generate AI가 로컬 Codex 설치와 로그인 상태에 의존하지 않는다.
- Image API 비용은 Generate AI 요청에만 발생하며 low/1K로 제한된다.
- 출력은 정사각형 1024×1024이므로 원본 종횡비 보존이 필수인 요청은 planner warning 또는 다른
  편집 경로가 필요하다.
- OpenAI API key의 배포·회전과 API 가용성이 새로운 운영 의존성이 된다.
