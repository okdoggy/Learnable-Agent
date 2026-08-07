from __future__ import annotations

import pytest

from lala.config import Settings
from lala.mcp.server import build_runtime, create_mcp
from lala.renderers.imagegen import OpenAIImagegenRunner


@pytest.mark.asyncio
async def test_mcp_exposes_only_scoped_llm_and_renderer_tools(settings: Settings) -> None:
    tools = await create_mcp(settings).list_tools()
    by_name = {tool.name: tool for tool in tools}

    assert set(by_name) == {
        "process_slack_image",
        "inspect_image",
        "validate_edit_plan",
        "apply_remaster",
        "apply_lut",
        "apply_generate_ai",
        "list_raw_scenarios",
        "read_raw_scenario",
        "write_raw_scenario",
        "list_technical_notes",
        "read_technical_note",
        "publish_technical_note",
    }
    remaster_schema = by_name["apply_remaster"].inputSchema
    assert "brightness" in remaster_schema["$defs"]["RemasterParameters"]["properties"]
    assert "path" not in remaster_schema["properties"]
    slack_schema = by_name["process_slack_image"].inputSchema
    assert slack_schema["properties"]["mode"]["default"] == "edit"
    assert slack_schema["properties"]["mode"]["enum"] == ["recommend", "edit"]
    assert "cache_filename" in slack_schema["properties"]
    assert "path" not in slack_schema["properties"]
    raw_list_schema = by_name["list_raw_scenarios"].inputSchema
    assert raw_list_schema["properties"]["offset"]["default"] == 0
    assert raw_list_schema["properties"]["offset"]["minimum"] == 0


@pytest.mark.asyncio
async def test_mcp_schema_pins_openai_image_api_execution(settings: Settings) -> None:
    tools = {tool.name: tool for tool in await create_mcp(settings).list_tools()}
    parameter_schema = tools["apply_generate_ai"].inputSchema
    generate = parameter_schema["$defs"]["GenerateAIParameters"]["properties"]

    assert generate["execution_mode"]["const"] == "openai-image-api"
    assert generate["output_format"]["const"] == "png"


def test_mcp_runtime_uses_openai_image_api_by_default(settings: Settings) -> None:
    runtime = build_runtime(settings)

    assert isinstance(runtime.imagegen, OpenAIImagegenRunner)
