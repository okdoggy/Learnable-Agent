# Calibration review report format

```markdown
---
reviewed_at: <ISO-8601 Asia/Seoul>
previous_report: <relative path or null>
session_cursor: <last reviewed session id or null>
reviewed_count: <integer>
unreviewable_count: <integer>
backlog: <true|false>
status: candidate-review
---

# 야간 캘리브레이션 검토

## 범위
- 비식별 검색 범위와 선택 이유

## 요청별 판정
- session/request ID
- 도구와 engine/calibration version
- 파라미터와 evidence ID/version
- 분류, 관찰된 비식별 지표, 신뢰도
- 원본/결과가 없으면 unreviewable 이유

## 반복 패턴
- 독립 세션 수와 공통 원인

## Calibration 후보
- 변경 대상과 근거
- 필요한 benchmark와 예상 위험
- 자동 반영 금지 여부

## 불필요한 과정 후보
- 제거 또는 단순화 후보와 안전 조건

## 다음 cursor와 backlog
- 마지막 검토 session ID와 남은 건수 추정
```

사용자 프롬프트, 이미지 설명·픽셀, 세션 전문, 토큰, private URL은 포함하지 않는다.
