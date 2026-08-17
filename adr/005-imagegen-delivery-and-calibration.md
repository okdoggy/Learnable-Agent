---
status: accepted
date: 2026-08-17
deciders: [user, hermes]
supersedes: [ADR-004 decision 4 response-size rejection]
---

# ADR-005: Generate AI는 1K를 요청하되 응답 크기 불일치만으로 차단하지 않고 LUT 보정은 TC로 시작한다

## 배경

`gpt-image-2` renderer는 지원 1K 크기(`1024x1024`, `1536x1024`, `1024x1536`) 중 입력 비율에 가장 가까운 값을 `size`로 요청한다. 그러나 API가 요청과 다른 크기의 유효 PNG를 반환했을 때 기존 구현은 해상도 불일치만으로 결과를 전달하지 않았다.

사용자는 Slack과 Vibe Editing 모두에서 1K Generate AI 결과를 받되, 응답 크기 차이만으로 정상 결과가 버려지지 않기를 원한다. 또한 LUT의 전반적인 뿌연 인상을 임의 수치 변경이 아니라 재현 가능한 test case(TC) 결과로 판단하려 한다.

## 결정

1. Generate AI renderer는 계속 renderer-owned 지원 1K `size`를 OpenAI Image API에 요청한다. 호출자가 별도 크기를 제공하지 않는 경우 기본은 `1024x1024` 1K다.
2. API 응답은 PNG 안전성, 이미지 디코딩, 출력 경로, EXIF orientation 적용, 메타데이터 제거, 최대 파일/픽셀 제한을 계속 검증한다.
3. API 응답의 실제 width×height가 요청한 1K 크기와 다르다는 사실만으로는 결과를 차단하지 않는다. renderer는 실제 결과 크기를 측정하고 Slack/Vibe 결과 계약에 기록한다.
4. 원본 입력의 임의 width×height를 OpenAI `size` 값으로 직접 요청하지 않는다. 현재 지원되는 1K 크기만 요청하며, 원본 입력은 crop 또는 padding으로 인위 변경하지 않는다.
5. Slack과 Vibe Editing은 동일한 `OpenAIImagegenRunner`를 통해 같은 요청·검증·실제 결과 크기 보고 정책을 사용한다.
6. LUT 보정은 사용자 이미지나 프롬프트를 TC에 복사하지 않는다. synthetic chart와 라이선스가 확인된 고정 fixture로 LUT별 명도 대비, 끝점, 색 편향, skin-like patch, halation·grain의 증분 효과를 측정한다.
7. TC 측정은 실제 서비스의 전후 vision quality gate가 아니다. ADR-001의 야간 오프라인 검토와 함께 calibration 후보를 만들며, 반복된 독립 실패·benchmark 무회귀·명시적 승인 전에는 production LUT 수치나 manifest를 변경하지 않는다.

## 결과

- OpenAI의 유효한 이미지 결과가 단순 해상도 차이로 폐기되지 않는다.
- 사용자는 실제 API 응답 크기를 확인할 수 있다.
- 지원되지 않는 arbitrary image size를 요청해 API 실패를 유발하지 않는다.
- LUT의 뿌연 느낌은 취향 기반 추측이 아니라 versioned TC baseline과 offline calibration으로 개선한다.
