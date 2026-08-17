#!/usr/bin/env bash
set -euo pipefail

: "${LALA_PROJECT_ROOT:?Set LALA_PROJECT_ROOT to the absolute repository path}"

export TZ="Asia/Seoul"
export PYTHONUTF8="1"

lala_hermes_home="$(dirname "$(hermes config path)")"
lala_cron_script_name="lala-calibration-review-context.py"
lala_publisher_script_name="lala-calibration-report-publisher.py"
lala_cron_script_dir="${lala_hermes_home}/scripts"
lala_project_root_marker="${lala_cron_script_dir}/lala-calibration-project-root.txt"
mkdir -p "${lala_cron_script_dir}"
for lala_script_name in "${lala_cron_script_name}" "${lala_publisher_script_name}"; do
  if [[ -L "${lala_cron_script_dir}/${lala_script_name}" ]]; then
    unlink "${lala_cron_script_dir}/${lala_script_name}"
  fi
done
install -m 0755 "${LALA_PROJECT_ROOT}/scripts/calibration_review_context.py" \
  "${lala_cron_script_dir}/${lala_cron_script_name}"
install -m 0755 "${LALA_PROJECT_ROOT}/scripts/calibration_report_publisher.py" \
  "${lala_cron_script_dir}/${lala_publisher_script_name}"
printf '%s\n' "${LALA_PROJECT_ROOT}" > "${lala_project_root_marker}"

lala_existing_cron_jobs="$(hermes cron list)"

if [[ "${lala_existing_cron_jobs}" != *"lala-knowledge-collector"* ]]; then
  hermes cron create "0 9 * * *" \
    "Hermes LLM이 허용된 전문가 자료를 web 도구로 직접 탐색하고 전체 의미를 읽어, write_raw_scenario로 한 파일 한 시나리오의 UTF-8 한국어 raw 문서를 ${LALA_PROJECT_ROOT}/raw 아래에 저장하라. Hermes 임시 폴더에 직접 쓰지 말고 신규/중복/거부/실패 수와 실제 저장 경로를 보고하라." \
    --skill knowledge-collector \
    --name "lala-knowledge-collector" \
    --workdir "${LALA_PROJECT_ROOT}"
else
  echo "lala-knowledge-collector already exists; skipped"
fi

if [[ "${lala_existing_cron_jobs}" != *"lala-library-curator"* ]]; then
  hermes cron create "0 10 * * *" \
    "Hermes LLM이 ${LALA_PROJECT_ROOT}/raw의 validated 문서를 빠짐없이 순회하고 전체 문맥으로 중요도와 반드시 기술화할 원리를 판단하라. publish_technical_note로 ${LALA_PROJECT_ROOT}/technical-library 아래에 001-xxxx.md를 발행하고 실제 저장 경로와 active/candidate/보류/병합/충돌 결정을 보고하라. Hermes 임시 폴더에 직접 쓰거나 단어·alias 점수로 군집화하지 마라." \
    --skill library-curator \
    --name "lala-library-curator" \
    --workdir "${LALA_PROJECT_ROOT}"
else
  echo "lala-library-curator already exists; skipped"
fi


if [[ "${lala_existing_cron_jobs}" != *"lala-calibration-reviewer"* ]]; then
  TZ="UTC" hermes cron create "0 12 * * *" \
    "lala-calibration-reviewer 스킬을 따라 마지막 성공 보고서 이후의 Slack 이미지 편집 세션을 최대 5건 검토하라. context의 parameter_calibration_policy와 active technical-library를 함께 읽고, TTL 안의 원본과 결과가 모두 있을 때만 개발용 전후 품질을 비교하라. capability·parameter calibration 오류와 불필요한 과정을 분류하고, 후보마다 evidence ID/version, 현재 calibration version, 반복성, 고정 TC 비교 필요 여부를 비식별로 기록하라. context의 promotion_requirements를 모두 충족하지 않은 후보는 production 변경 제안으로 승격하지 마라. production을 수정하지 말고 사용자 이미지·프롬프트·세션 전문을 저장하지 않은 비식별 후보 보고서를 context의 절대 report_filename에 작성하라. 21:10 publisher가 이를 ${LALA_PROJECT_ROOT}/calibration/reports로 발행한다." \
    --skill lala-calibration-reviewer \
    --script "${lala_cron_script_name}" \
    --name "lala-calibration-reviewer" \
    --deliver local \
    --workdir "${LALA_PROJECT_ROOT}"
else
  echo "lala-calibration-reviewer already exists; skipped"
fi


if [[ "${lala_existing_cron_jobs}" != *"lala-calibration-report-publisher"* ]]; then
  TZ="UTC" hermes cron create "10 12 * * *" \
    --script "${lala_publisher_script_name}" \
    --no-agent \
    --name "lala-calibration-report-publisher" \
    --deliver local \
    --workdir "${LALA_PROJECT_ROOT}"
else
  echo "lala-calibration-report-publisher already exists; skipped"
fi
