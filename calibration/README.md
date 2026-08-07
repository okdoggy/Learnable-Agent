# Offline calibration

`reports/`는 매일 21:00 Asia/Seoul 개발 cron이 staging에 작성하고 21:10 deterministic publisher가
원자적으로 발행하는 비식별 후보 보고서다. 보고서는 production을 자동 수정하지 않으며 사용자
이미지·프롬프트·세션 전문을 저장하지 않는다. 반복된 독립 실패와 benchmark 무회귀가 확인된
후보만 `config/parameter-registry.yaml`의 새 calibration version으로 별도 개발 검증 후 반영한다.
