from google.adk.agents import SequentialAgent
from lifeos.agents.planner_agent import planner_agent
from lifeos.agents.decision_agent import decision_agent

schedule_workflow = SequentialAgent(
    name="schedule_workflow",
    steps=[planner_agent, decision_agent],
    description="Planner → Decision refinement."
)
