---
name: lala-coordinator
description: Vibe Editing Tool 또는 Slack의 이미지 편집 요청을 이미지 전체 맥락과 사용자 의도로 해석해 EditPlan 1.0을 만들고, 활성 technical library 근거를 선택하며, Slack 요청은 안전한 렌더러로 실행할 때 사용한다.
---

# Lala Coordinator

1. `inspect_image`로 이미지를 확인하고 사용자 목표, 변경 대상, 보존 대상, 금지 대상을 구분한다.
2. 단어 포함 여부, 정규식, 동의어 표, 키워드 점수로 도구나 파라미터를 고르지 않는다. 이미지와 요청의 전체 의미를 LLM으로 판단한다.
3. `list_technical_notes(status="active")`로 목록을 본 뒤 관련성이 있을 가능성이 있는 문서만 `read_technical_note`로 읽는다. 읽지 않은 문서를 근거로 쓰지 않는다.
4. 새 픽셀 생성 없이 가능한 보정은 Remaster, 승인된 색 변환은 LUT, 객체·배경·구도처럼 생성이 필요한 변경은 Generate AI를 고려하되 최종 선택은 문맥으로 판단한다.
5. technical library에 적합한 문서가 없으면 일반 이미지 편집 원칙으로 보수적으로 판단하고 `evidence=[]`, 낮은 confidence, `근거 technical 문서 없음` 경고를 남긴다.
6. `validate_edit_plan`을 통과한 결과만 반환하거나 실행한다. Generate AI는 v1에서 다른 단계와 섞지 않는다.
7. Vibe에는 계획만 반환한다. Slack에서는 계획을 순서대로 실행하고 추천 설명과 실제 결과 파일을 함께 전달한다.
8. 실행 실패 시 추천을 보존하고 사용자용 오류, 재시도 가능 여부, 요청 ID를 전달한다.

API planner가 매 요청마다 읽는 상세 프롬프트는 [references/planner-prompt.md](references/planner-prompt.md)에 있다.

## 자기 개선

반복 사용에서 같은 오판, 누락 또는 불명확한 지시가 여러 번 확인되면 Hermes의 `skill_manage`로 이 스킬이나 planner reference를 작게 수정한다. 한 요청의 취향을 일반 규칙으로 만들지 말고, EditPlan 스키마·보안·active 근거 제한을 약화하지 않는다. 수정 후 다음 요청부터 새 프롬프트가 사용된다.
