from google.adk.agents import Agent
from lifeos.tools import gmail_tool

inbox_agent = Agent(
    name="inbox_agent",
    model="gemini-2.0-flash",
    description="Reads and triages emails.",
    instruction=(
        "Use gmail_tool to fetch emails.\n"
        "Categorize into Urgent / Important / Later.\n"
        "Write short summaries and suggested replies."
    ),
    tools=[gmail_tool]
)
