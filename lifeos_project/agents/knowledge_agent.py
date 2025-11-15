from google.adk.agents import Agent
from lifeos.tools import notes_reader

knowledge_agent = Agent(
    name="knowledge_agent",
    model="gemini-2.0-flash",
    description="Reads and summarizes documents.",
    instruction=(
        "Use notes_reader MCP tool to read files.\n"
        "Summarize documents and extract key actions.\n"
        "If asked about weekly work → infer from note content."
    ),
    tools=[notes_reader]
)
