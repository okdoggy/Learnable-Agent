---
name: lala-calibration-reviewer
description: 매일 21:00 Asia/Seoul에 최근 Slack 이미지 편집 세션을 오프라인으로 검토해 renderer capability·parameter calibration 오류와 불필요한 과정을 비식별 후보 보고서로 남길 때 사용한다.
---

# Lala Calibration Reviewer

이 작업은 개발용 오프라인 검토다. 실제 서비스 요청을 처리하거나 사용자에게 결과를 전달하지 않는다.

1. 주입된 context의 `latest_report`, `report_filename`, `max_sessions_per_run`을 확인한다.
2. `session_search`로 최근 Slack 이미지 편집 세션을 찾고 마지막 보고서 이후의 미검토 세션을 우선한다. Hermes session DB를 직접 읽거나 수정하지 않는다.
3. 사용자 부정 피드백, 실행 오류, 긴 재시도, 도구 capability와 맞지 않는 계획, calibration 범위를 크게 벗어난 요청을 우선하며 한 번에 최대 5개만 검토한다.
4. 세션 transcript에서 request ID, 실제 도구·engine version·파라미터·evidence와 존재하는 원본/결과 경로만 상관관계로 사용한다. 사용자 문장이나 이미지 내용을 보고서에 복사하지 않는다.
5. 원본과 결과가 모두 TTL 안에 존재할 때만 `vision_analyze`로 개발용 전후 품질을 비교한다. 파일이 없으면 반복 호출하지 말고 `unreviewable`과 이유를 기록한다.
6. 문제를 이미지 해석, evidence 선택, capability 불일치, parameter calibration, renderer, workspace handoff, 불필요한 호출, 검수 누락으로 분류한다.
7. 한 사례의 취향을 일반화하지 않는다. production 수정 후보는 여러 독립 세션의 반복, 사용자 피드백, benchmark 무회귀가 필요하다고 표시한다.
8. [references/report-format.md](references/report-format.md)에 따라 context의 절대 `report_filename`에 UTF-8/LF 보고서 하나를 쓴다. 이 staging 보고서는 21:10 deterministic publisher가 프로젝트 `calibration/reports/`로 원자적으로 복사한다.
9. 이 cron에서는 production 코드, renderer, `technical-library/`, `raw/`, `lala-coordinator`를 수정하지 않는다. 보고서와 calibration 후보만 남긴다.
10. 이미지·프롬프트·세션 전문·토큰·비공개 URL을 저장하거나 로그에 기록하지 않는다.

보고할 대상이 없더라도 cursor, 검색 범위, 검토 0건과 backlog 여부를 기록해 cron 성공을 검증할 수 있게 한다.
