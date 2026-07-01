import asyncio
import os
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.runners import InMemoryRunner
from google.genai import types
from google.adk.tools import ToolContext

load_dotenv()
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"

# 1. Custom Tool to modify Session State
def save_destination_to_state(tool_context: ToolContext, destination: str) -> dict:
    """Saves the user's chosen travel destination to the session state.

    Args:
        destination: The country or city the user wants to visit.

    Returns:
        dict: Status of the save operation.
    """
    tool_context.state["destination"] = destination
    return {"status": "success", "message": f"Saved {destination} to state."}

# 2. Specialized Sub-Agents
travel_brainstormer = Agent(
    name="travel_brainstormer",
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    description="Helps the user brainstorm destinations if they don't know where to go.",
    instruction="Brainstorm 3 unique travel destinations. Do not plan the trip.",
)

attractions_planner = Agent(
    name="attractions_planner",
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    description="Helps the user build a list of things to do once they know their destination.",
    instruction="""Ask the user for their destination. 
    Use the save_destination_to_state tool to save it. 
    If they have a destination in state: { destination? }, suggest 3 attractions for it.""",
    tools=[save_destination_to_state]
)

# 3. Root Parent Agent (Router)
root_agent = Agent(
    name="steering",
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    instruction="""You are a routing agent. 
    If they need help deciding where to go, route to 'travel_brainstormer'.
    If they know where they want to go, route to 'attractions_planner'.""",
    sub_agents=[travel_brainstormer, attractions_planner]
)

async def main():
    runner = InMemoryRunner(agent=root_agent, app_name="routing_app")
    session = await runner.session_service.create_session(app_name="routing_app", user_id="user1")
    
    print("Agent: Do you know where you want to travel, or need help brainstorming?")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]: break
        
        content = types.Content(role="user", parts=[types.Part.from_text(text=user_input)])
        async for event in runner.run_async(user_id="user1", session_id=session.id, new_message=content):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text: print(part.text, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
