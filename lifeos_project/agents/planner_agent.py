from google.adk.agents import Agent
from lifeos.tools import calendar_tool, calculate_productivity

planner_agent = Agent(
    name="planner_agent",
    model="gemini-2.0-flash",
    description="Creates structured daily/weekly plans.",
    instruction=(
        "Create structured, prioritized daily or weekly plans.\n"
        "- Use calendar_tool to check events.\n"
        "- Use productivity metrics if needed.\n"
        "Always provide a clean list with time blocks."
    ),
    tools=[calendar_tool, calculate_productivity]
)
