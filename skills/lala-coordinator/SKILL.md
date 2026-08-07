---
name: lala-coordinator
description: Slack 또는 Vibe Editing Tool의 이미지 편집 방법 문의와 결과 요청을 안전한 단일 fast path로 처리할 때 사용한다.
---

# Lala Coordinator

## Slack runtime fast path — 필수

Slack 메시지에 이미지 첨부가 있고 편집 방법 또는 편집 결과를 요청하면 다음 절차만 사용한다.

1. 사용자가 방법만 묻는 경우 `mode="recommend"`, 실제 결과를 요청하는 경우 `mode="edit"`로 정한다.
2. Hermes가 제공한 첨부 경로에서 basename만 취한다. 임의 경로나 원본 내용을 읽지 않는다.
3. `process_slack_image(cache_filename, prompt, mode)`를 정확히 한 번 호출한다. 이 호출이 첨부 등록, EXIF orientation 적용과 PNG 정규화, 이미지 검사, active technical 근거를 포함한 Hermes 계획, EditPlan 검증, 선택적 렌더링, 메타데이터 제거를 모두 수행한다.
4. 반환된 `message_ko`를 바탕으로 짧게 답한다. `mode="edit"`이고 `output_path`가 있으면 Slack 첨부로 결과를 전달한다.
5. 오류가 나면 반환된 사용자용 오류와 request ID를 전달하고 중단한다. 운영 요청을 디버깅이나 개발 작업으로 전환하지 않는다.

Slack runtime에서는 다음을 하지 않는다.

- `inspect_image`, `list_technical_notes`, `read_technical_note`, `validate_edit_plan`, `apply_remaster`, `apply_lut`, `apply_generate_ai`를 직접 조립하지 않는다.
- file search/read/write, terminal, Python 실행, process 조회, source code·ADR·README 탐색, 임시 스크립트 작성, 코드 또는 skill 수정을 하지 않는다.
- 추가 vision 비교, 결과 재검사, renderer 재실행, chunked/custom renderer fallback을 하지 않는다.
- `references/planner-prompt.md`를 별도로 읽지 않는다. fast path 내부 planner가 단일 원본으로 사용한다.

## Vibe와 명시적 개발 요청

- Vibe API는 기존 API planner와 EditPlan 계약을 사용한다.
- 사용자가 코드·설정·테스트 변경을 명시적으로 요청한 경우에만 개발 모드로 전환한다. Slack 이미지 운영 요청 자체는 개발 요청이 아니다.
- Generate AI는 OpenAI Image API의 고정 계약(`gpt-image-2`, `low`, `1024x1024`, PNG)을 사용한다.

## 운영 불변식

- 단어 포함 여부, 정규식, 동의어 표, 키워드 점수로 의미 결정을 구현하지 않는다.
- active technical library만 근거로 사용하고 실제 planner context에 제공된 ID와 version만 evidence에 기록한다.
- 실시간으로 원본·결과를 두 번째 vision model로 비교하지 않는다. 파일 형식·해상도·metadata 제거 등 저비용 안전 gate는 유지한다.
- 실행 실패 시 추천을 보존하고 사용자용 오류, 재시도 가능 여부, request ID를 전달한다.
- 반복 오판 분석과 prompt 개선은 별도 개발 또는 nightly calibration workflow에서만 수행하며 운영 요청 도중 production을 수정하지 않는다.

API planner의 단일 상세 프롬프트 원본은 [references/planner-prompt.md](references/planner-prompt.md)이다.
