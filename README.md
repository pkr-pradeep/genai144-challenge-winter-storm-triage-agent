# GenAI 144 Challenge - Winter Storm Triage Agent

This repository contains the solution and implementation for the Cymbal Direct Winter Storm Triage Agent challenge using Google Cloud and Google Agent Development Kit (ADK).

## Repository Structure

- **`.agents/skills/winter-storm-triage/`**: Standard operating procedures skill for handling winter storm disruption triage, loyalty compensation matrix, and customer response drafting.
- **`mcp/`**: FastMCP server (`cymbal_direct_mcp.py`) providing logistics tools:
  - `get_order_status`
  - `get_customer_loyalty_info`
  - `issue_disruption_compensation`
- **`winter-storm-triage/`**: Scaffolded ADK agent project (`agents-cli`):
  - Model: `gemini-3.8-flash` (location: `us`)
  - Integration: MCP toolset integration with `cymbal_direct_mcp.py`
  - Deployment target: Agent Runtime in `us-west1`
- **`GEMINI.md`**: Workspace rules and coding standards.
- **`summary_task*.md`**: Task completion summaries and verification logs.
