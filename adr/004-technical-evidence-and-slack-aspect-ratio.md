---
status: accepted
date: 2026-08-07
deciders: [user, hermes]
supersedes: [ADR-002 Generate AI output-size restriction, AGENTS.md rule 7 output-size restriction]
---

# ADR-004: 편집 응답의 technical-library 근거와 Slack Generate AI 종횡비를 보장한다

## 결정

1. 이미지 보정·편집 요청마다 Hermes planner는 이미지와 사용자 요청의 전체 맥락에 맞는 `status: active` technical-library 문서를 선택해 계획의 근거로 사용한다. 실제 제공된 문서만 선택하고 ID와 version을 evidence에 기록한다.
2. 사용자 응답은 선택·참고한 technical-library ID와 version을 항상 명시한다. 활성 문서에 현재 요청을 뒷받침할 수 있는 기술이 없으면 근거 없는 편집 계획을 제시하지 않고 그 사실을 명확히 알린다.
3. Slack에서 Generate AI가 선택되면 renderer는 입력 이미지 종횡비에 가장 가까운 OpenAI 1K 출력 크기(`1024x1024`, `1536x1024`, `1024x1536`)를 요청한다. model `gpt-image-2`, quality `low`, PNG와 전용 API key 계약은 유지한다.
4. 출력 크기는 planner 또는 사용자 입력이 아닌 renderer가 입력 이미지 치수에서 결정한다. 응답에는 실제 요청한 출력 크기를 포함한다.

## 결과

- 응답의 technical-library 근거가 사용자가 확인할 수 있는 형태로 남는다.
- 정사각형 강제 출력으로 인한 Slack 이미지의 과도한 구도 손실을 줄인다.
- API가 선택한 1K 크기로 응답하지 않으면 결과를 전달하지 않는다.
