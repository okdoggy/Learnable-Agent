# raw 문서 작성 형식

참고 구조는 `Samsung Support — Camera modes and settings — 상황별 촬영/보정 팁` 예시처럼 실전에 바로 쓰는 팁 카드 방식이다. 다만 예시와 달리 이 프로젝트는 한 Markdown 파일에 한 시나리오만 저장한다.

각 `RawScenarioSubmission`에는 다음 내용을 한국어로 작성한다.

- `situation_ko`: 언제 이 시나리오가 필요한지
- `workflow_ko`: 촬영 또는 편집 순서
- `scenario.method.steps`: 원문이 직접 말한 정확한 값 또는 수치 없는 정성 표현
- `editing_routine_ko`: 후처리 순서와 관찰할 결과
- `cautions_ko`: 실패 조건과 과도한 적용 위험
- `certainty_ko`: 출처가 직접 뒷받침한 내용과 LLM의 해석 범위

원문 전체를 복제하지 않고 URL, 작성자·게시자, 게시일, 접근일, 원문 언어를 보존한다. 모든 텍스트는 UTF-8로 전달한다.

발행은 반드시 `write_raw_scenario`로 수행한다. 최종 Markdown 위치는 프로젝트의
`<LALA_PROJECT_ROOT>/raw/YYYYMMDD/`이며 Hermes 세션 또는 임시 작업 폴더는 최종 저장소가 아니다.
