from google.adk.agents import Agent
from lifeos.tools import update_habit, calculate_productivity

habit_agent = Agent(
    name="habit_agent",
    model="gemini-2.0-flash",
    description="Tracks and analyzes habits.",
    instruction=(
        "Use update_habit tool to modify streaks.\n"
        "Use calculate_productivity to compute consistency.\n"
        "Provide motivational feedback."
    ),
    tools=[update_habit, calculate_productivity]
)
