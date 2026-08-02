#!/usr/bin/env bash
set -euo pipefail

: "${LALA_PROJECT_ROOT:?Set LALA_PROJECT_ROOT to the absolute repository path}"

export TZ="Asia/Seoul"
export PYTHONUTF8="1"

lala_hermes_home="$(dirname "$(hermes config path)")"
lala_plugin_source="${LALA_PROJECT_ROOT}/.hermes/plugins/lala-web-openai-codex"
lala_plugin_target="${lala_hermes_home}/plugins/lala-web-openai-codex"
lala_raw_dir="${LALA_PROJECT_ROOT}/raw"

mkdir -p "${lala_hermes_home}/plugins" "${lala_raw_dir}"
ln -sfn "${lala_plugin_source}" "${lala_plugin_target}"
hermes plugins enable lala-web-openai-codex --no-allow-tool-override
hermes config set web.search_backend openai-codex
hermes config set web.extract_backend openai-codex
hermes config set web.openai_codex.allowed_domains \
  '["adobe.com","youtube.com","youtu.be","petapixel.com","fstoppers.com"]'
hermes config set mcp_servers.lala-tools.env.LALA_PROJECT_ROOT "${LALA_PROJECT_ROOT}"
hermes config set mcp_servers.lala-tools.env.LALA_RAW_DIR "${lala_raw_dir}"

lala_existing_cron_jobs="$(hermes cron list)"

if [[ "${lala_existing_cron_jobs}" != *"lala-knowledge-collector"* ]]; then
  hermes cron create "0 9 * * *" \
    "Hermes LLM이 GPT 기반 web_search와 web_extract만 사용해 허용된 전문가 자료를 탐색하고 전체 의미를 읽어, LALA_PROJECT_ROOT/raw 아래에 한 파일 한 시나리오의 UTF-8 한국어 raw 문서로 저장한 뒤 신규/중복/거부/실패 수를 보고하라. browser 또는 navigate를 사용하지 마라." \
    --skill knowledge-collector \
    --name "lala-knowledge-collector" \
    --workdir "${LALA_PROJECT_ROOT}"
else
  echo "lala-knowledge-collector already exists; skipped"
fi

if [[ "${lala_existing_cron_jobs}" != *"lala-library-curator"* ]]; then
  hermes cron create "0 10 * * *" \
    "Hermes LLM이 validated raw의 반복성과 의미를 전체 문맥으로 비교해 001-xxxx.md 형식의 technical 문서를 발행하고 active/candidate/충돌 수를 보고하라. 단어·alias 점수로 군집화하지 마라." \
    --skill library-curator \
    --name "lala-library-curator" \
    --workdir "${LALA_PROJECT_ROOT}"
else
  echo "lala-library-curator already exists; skipped"
fi
