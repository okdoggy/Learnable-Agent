---
status: accepted
date: 2026-08-07
---

# ADR 003: Slack 이미지 요청은 단일 runtime fast path로 처리한다

## 맥락

Slack 첨부 이미지 요청이 저수준 MCP 도구 조립으로 처리되면서 technical note 개별 조회, workspace 수동 복사, 반복 검사와 renderer 재실행이 발생했다. workspace handoff 실패 후에는 file·terminal·code 도구로 소스 탐색과 임시 스크립트 작성까지 이어져 한 요청이 24 iteration, 약 9분 걸렸다.

## 결정

1. Slack 이미지 방법 문의와 결과 요청은 `process_slack_image` MCP 도구 한 번으로 처리한다.
2. 이 도구가 cache attachment 등록, 안전한 PNG 정규화, inspection, Hermes 계획, EditPlan 검증과 선택적 실행을 순서대로 책임진다.
3. `recommend`는 계획까지만, `edit`는 렌더링까지 수행한다.
4. Slack 플랫폼에는 `skills`와 `lala-slack` MCP toolset만 노출한다. `lala-slack`은 `process_slack_image`만 노출한다.
5. 운영 오류는 사용자용 오류와 request ID를 반환하고 종료한다. file·terminal·code fallback과 production 수정은 금지한다.
6. 기존 저수준 MCP 도구는 개발·Vibe·knowledge workflow 호환을 위해 `lala-tools`에 유지하되 Slack fast path에서는 직접 호출하지 않는다.

## 결과

- 정상 Slack 이미지 요청은 skill 로드 후 MCP 1회와 최종 응답으로 제한된다.
- attachment와 request workspace의 handoff가 결정론적으로 수행된다.
- Slack 운영 세션에서 소스 코드 수정과 임시 스크립트 실행이 도구 수준에서 차단된다.
- semantic 도구·파라미터 선택은 내부 Hermes planner가 계속 수행하므로 키워드 기반 의미 판단은 도입하지 않는다.
