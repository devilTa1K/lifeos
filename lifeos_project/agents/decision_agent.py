from google.adk.agents import Agent

decision_agent = Agent(
    name="decision_agent",
    model="gemini-2.0-flash",
    description="Prioritizes tasks and adjusts schedules.",
    instruction=(
        "Given tasks/plans/emails/habits, decide top priorities.\n"
        "Explain why each priority was chosen.\n"
        "Return clean ranked list of priorities."
    )
)
