from google.adk.agents import ParallelAgent, LoopAgent
from lifeos.agents.inbox_agent import inbox_agent
from lifeos.agents.habit_agent import habit_agent
from lifeos.agents.knowledge_agent import knowledge_agent

morning_parallel = ParallelAgent(
    name="morning_parallel",
    agents=[inbox_agent, habit_agent, knowledge_agent],
    description="Inbox + Habits + Notes in parallel."
)

maintenance_loop = LoopAgent(
    name="maintenance_loop",
    agent=morning_parallel,
    max_iterations=5,
    description="Looped daily maintenance."
)
