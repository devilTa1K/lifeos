from google.adk.tools import function_tool

habit_data = {}

@function_tool
def update_habit(habit_name: str, success: bool):
    if habit_name not in habit_data:
        habit_data[habit_name] = {"streak": 0, "total": 0}

    habit_data[habit_name]["total"] += 1

    if success:
        habit_data[habit_name]["streak"] += 1
    else:
        habit_data[habit_name]["streak"] = 0

    return habit_data[habit_name]
