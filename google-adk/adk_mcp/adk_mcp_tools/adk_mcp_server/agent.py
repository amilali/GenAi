import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, \
                    StdioServerParameters, StdioConnectionParams

# IMPORTANT: Replace this with the ABSOLUTE path to your adk_server.py script
PATH_TO_YOUR_MCP_SERVER_SCRIPT = "/home/student_00_9b06473d6aa3/adk_mcp_tools/adk_mcp_server/adk_server.py"

if PATH_TO_YOUR_MCP_SERVER_SCRIPT == "None":
    print("WARNING: PATH_TO_YOUR_MCP_SERVER_SCRIPT is not set. Please update it in agent.py.")
    # Optionally, raise an error if the path is critical

root_agent = LlmAgent(
    model=os.getenv("MODEL"),
    name='web_reader_mcp_client_agent',
    instruction="Use the 'load_web_page' tool to fetch content from a URL provided by the user.",
    ## Add the MCPToolset below:
    tools=[
    MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="python3", # Command to run your MCP server script
            args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT], # Argument is the path to the script
        ),
        timeout=15,
        ),
        tool_filter=['load_web_page'] # Optional: ensure only specific tools are loaded
    )
],
)