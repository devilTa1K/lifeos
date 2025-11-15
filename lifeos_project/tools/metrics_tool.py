from google.adk.tools import function_tool

@function_tool
def calculate_productivity(streak: int, total: int):
    if total == 0:
        percent = 0
    else:
        percent = (streak / total) * 100

    return {
        "streak": streak,
        "total": total,
        "percentage": percent,
        "message": f"Consistency: {percent:.2f}%"
    }
