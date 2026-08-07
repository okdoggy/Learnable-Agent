# technical library 작성 형식

`TechnicalNoteSubmission`은 Hermes LLM의 의미 판단 결과다.

- `technical_id`: 안정적인 영문 slug
- `title_ko`, `summary_ko`: 기술과 적용 목표
- `status`: 반복 근거와 실행 가능성이 충분하면 active, 아니면 candidate
- `supported_tools`: 실제로 연결 가능한 Remaster, LUT 또는 Generate AI
- `raw_scenario_ids`: 판단에 사용한 모든 raw ID
- `applicability_ko`: 적용되는 이미지·조명·피사체 조건
- `procedure_ko`: 순서가 있는 기술 절차
- `parameter_guidance_ko`: 근거가 있는 값, 안전 범위 또는 조정 방향
- `rationale_ko`: 왜 이 기술이 반복적이고 의미 있는지
- `cautions_ko`, `conflicts_ko`: 실패 조건, 예외, 상충 근거

파일 번호, source URL, semantic version은 `publish_technical_note`가 검증된 raw 근거에서 계산한다. 출력은 UTF-8 Markdown이며 파일명은 `001-xxxx.md` 형식이다.

중요도와 필수 기술화 여부는 Hermes LLM이 raw와 기존 technical 문서의 전체 문맥으로 판단한다.
필수 기술화 대상인데 독립 근거가 부족한 경우 누락하지 말고 `candidate`로 발행한다. 충분한 독립
근거가 있을 때만 `active`로 발행한다. 최종 파일은 반드시 프로젝트의
`<LALA_PROJECT_ROOT>/technical-library/` 아래에 있어야 한다.
