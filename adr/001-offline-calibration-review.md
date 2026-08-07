---
status: accepted
date: 2026-08-07
deciders: [user, hermes]
---

# ADR-001: 실시간 품질 비교 대신 야간 오프라인 캘리브레이션을 사용한다

## 배경

실시간 이미지 편집에서 원본과 결과를 다시 vision model로 비교하면 지연과 비용이 증가한다.
반면 schema·근거·도구 capability·파일 안전 검증만으로는 renderer별 파라미터의 실제 체감 강도와
반복되는 미학적 실패를 충분히 학습하기 어렵다.

## 결정

1. 실제 서비스는 원본과 결과의 미학적 전후 품질 gate를 실행하지 않는다.
2. 실제 서비스는 EditPlan schema, active evidence, 도구 capability, version, 파라미터 범위,
   LUT manifest, 출력 형식·해상도·메타데이터 등 빠른 계약·안전 gate를 유지한다.
3. planner는 versioned renderer capability 및 parameter calibration registry 전문을 입력으로 받아
   이미지 전체 문맥으로 도구와 파라미터를 선택한다. registry를 단어→수치 규칙으로 사용하지 않는다.
4. 매일 21:00 Asia/Seoul 개발 cron이 마지막 성공 검토 이후 Slack 이미지 편집 세션을 제한된
   batch로 검토한다. TTL 안에 원본과 결과가 모두 있을 때만 오프라인 전후 품질을 평가한다.
5. 야간 검토는 비식별 calibration 후보 보고서만 발행한다. 한 세션을 근거로 production 코드,
   technical library, renderer 또는 runtime skill을 즉시 수정하지 않는다.
6. 반복된 독립 실패, 사용자 피드백, 기존 benchmark의 무회귀가 함께 확인된 후보만 별도 개발
   검증에서 calibration version을 올려 반영한다. 모든 반영은 rollback 가능해야 한다.
7. 사용자 이미지·프롬프트·세션 전문은 raw, technical-library 또는 calibration 보고서에 복사하지
   않는다. 보고서에는 request/session ID, 도구·버전·파라미터, 비식별 지표와 원인 분류만 남긴다.

## 결과

- 서비스 응답 시간은 전후 vision 평가에 의존하지 않는다.
- capability와 calibration의 변화가 버전·hash로 재현 가능해진다.
- 야간 cron 실패는 서비스 요청을 막지 않는다.
- 품질 개선은 즉시 자동 drift가 아니라 보고서→benchmark→승인된 반영 순서를 따른다.
- 24시간 TTL을 유지하려면 21:00 검토와 cleanup이 경합하지 않도록 운영 순서를 분리해야 한다.
