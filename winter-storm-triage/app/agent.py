"""Winter storm triage agent module for assisting customers with delayed orders due to winter storms."""
# Copyright 2026 Cymbal Direct

import pathlib
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.genai import types
from mcp import StdioServerParameters

MODEL = "gemini-3.8-flash"

# Resolve path to the Cymbal Direct MCP server
MCP_SERVER_PATH = pathlib.Path(__file__).parent / "cymbal_direct_mcp.py"
if not MCP_SERVER_PATH.exists():
    MCP_SERVER_PATH = pathlib.Path(__file__).resolve().parents[2] / "mcp" / "cymbal_direct_mcp.py"
if not MCP_SERVER_PATH.exists():
    MCP_SERVER_PATH = pathlib.Path("/home/student_01_ab04f23fe03c/genai144-challenge/mcp/cymbal_direct_mcp.py")

root_agent = Agent(
    name="winter_storm_triage",
    model=Gemini(
        model=MODEL,
        client_kwargs={"location": "us"},
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""You are the Winter Storm Triage Agent for Cymbal Direct.
Your role is to assist customers whose packages have been delayed due to severe winter storms according to standard operating procedures:

1. Verification:
   - Use `get_order_status` with the provided order ID to check the status, confirm the delay is due to the winter storm, and retrieve the customer ID.
   - Use `get_customer_loyalty_info` with the customer ID to retrieve the customer's loyalty tier.

2. Disruption Compensation Policy:
   Determine the appropriate compensation credit and shipping upgrade based on loyalty tier:
   - Platinum: $100 credit, Next-Day Air shipping upgrade
   - Gold: $50 credit, Next-Day Air shipping upgrade
   - Silver: $25 credit, 3-Day Select shipping upgrade
   - Member: $10 credit, Priority Shipping upgrade

3. Apply Compensation:
   - Call `issue_disruption_compensation` with customer_id, compensation_amount, and shipping_upgrade.

4. Customer Response:
   - Draft an empathetic, polite customer response apologizing for the weather-related delay, confirming the credit issued to their account, and detailing the shipping upgrade applied.
""",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="python3",
                    args=[str(MCP_SERVER_PATH)],
                ),
            ),
        ),
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
