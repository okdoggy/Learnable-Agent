# Offline calibration

`reports/`는 매일 21:00 Asia/Seoul 개발 cron이 staging에 작성하고 21:10 deterministic publisher가
원자적으로 발행하는 비식별 후보 보고서다. 보고서는 production을 자동 수정하지 않으며 사용자
이미지·프롬프트·세션 전문을 저장하지 않는다. 반복된 독립 실패와 benchmark 무회귀가 확인된
후보만 `config/parameter-registry.yaml`의 새 calibration version으로 별도 개발 검증 후 반영한다.

## 승격 계약

런타임 planner는 active technical-library와 versioned registry를 읽어 계획을 만들지만, runtime에서
이미지를 다시 채점하거나 LUT cube·manifest·registry를 자동 변경하지 않는다. 특히 grain/halation 같은
대기 효과는 active `restrained-atmospheric-softness` evidence와 registry의 보수적 시작 상한을 모두
통과해야 한다.

보고서의 후보는 다음을 모두 만족한 경우에만 별도 개발 작업으로 승격할 수 있다.

1. 독립된 반복 사례와 사용자 피드백을 비식별로 확인한다.
2. 고정된 권리 확보 TC에서 기존 registry와 candidate registry를 직접 시각 비교한다.
3. benchmark 무회귀와 active evidence ID/version 일치를 확인한다.
4. review 결과와 rollback 정보를 포함한 명시적 승인 뒤에만 `calibration_version`을 올린다.

cube 변경은 planner/registry parameter 선택으로 해결되지 않는 LUT 고유 curve 결함이 TC에서 입증된
경우에만 후순위로 검토한다.
