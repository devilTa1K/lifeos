from google.adk.tools import OpenApiTool

from .habits_tool import update_habit
from .metrics_tool import calculate_productivity
from .notes_mcp_tool import notes_reader

gmail_tool = OpenApiTool.from_yaml("tools/gmail_openapi.yaml")
calendar_tool = OpenApiTool.from_yaml("tools/calendar_openapi.yaml")

__all__ = [
    "update_habit",
    "calculate_productivity",
    "notes_reader",
    "gmail_tool",
    "calendar_tool",
]
