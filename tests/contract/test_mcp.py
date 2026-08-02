from __future__ import annotations

import pytest

from lala.config import Settings
from lala.mcp.server import create_mcp


@pytest.mark.asyncio
async def test_mcp_exposes_only_scoped_llm_and_renderer_tools(settings: Settings) -> None:
    tools = await create_mcp(settings).list_tools()
    by_name = {tool.name: tool for tool in tools}

    assert set(by_name) == {
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


@pytest.mark.asyncio
async def test_mcp_schema_pins_builtin_imagegen_execution(settings: Settings) -> None:
    tools = {tool.name: tool for tool in await create_mcp(settings).list_tools()}
    parameter_schema = tools["apply_generate_ai"].inputSchema
    generate = parameter_schema["$defs"]["GenerateAIParameters"]["properties"]

    assert generate["execution_mode"]["const"] == "codex-imagegen-builtin"
    assert generate["output_format"]["const"] == "png"
