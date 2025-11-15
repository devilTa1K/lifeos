from google.adk.tools import mcp_tool

notes_reader = mcp_tool(
    name="notes_reader",
    description="Reads local notes/files.",
    commands=[
        {
            "name": "read_file",
            "description": "Read a file from disk",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"]
            }
        }
    ]
)
