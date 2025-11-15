from google.adk.agents import WorkflowAgent
from lifeos.workflows.schedule_workflow import schedule_workflow
from lifeos.workflows.maintenance_workflow import morning_parallel, maintenance_loop
from lifeos.agents.habit_agent import habit_agent
from lifeos.agents.inbox_agent import inbox_agent
from lifeos.agents.knowledge_agent import knowledge_agent

orchestrator_agent = WorkflowAgent(
    name="lifeos_orchestrator",
    model="gemini-2.0-flash",
    description="Main orchestrator for LifeOS.",
    instruction=(
        "Understand the user's request and route it.\n"
        "Use workflows for:\n"
        "- 'plan_day' → planning workflow\n"
        "- 'morning_maintenance' → parallel workflow\n"
        "- 'run_maintenance_loop' → loop workflow\n"
        "Otherwise route to the closest agent (habit/email/notes)."
    ),
    workflows={
        "plan_day": schedule_workflow,
        "morning_maintenance": morning_parallel,
        "run_maintenance_loop": maintenance_loop,
    }
)
