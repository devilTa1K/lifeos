from google.adk.app import AdkApp
from lifeos.agents.orchestrator import orchestrator_agent
from lifeos.memory.memory_service import session_service, memory_service

app = AdkApp(
    root_agent=orchestrator_agent,
    session_service=session_service,
    memory_service=memory_service,
    name="lifeos",
)

if __name__ == "__main__":
    print("LifeOS – Personal Operating System")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "exit":
            break

        response = app.run(user_input)
        print("\n[LifeOS]:\n", response, "\n")
