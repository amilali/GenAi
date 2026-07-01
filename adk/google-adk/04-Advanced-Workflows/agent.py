import asyncio
import os
import logging
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.workflows import SequentialAgent
from google.adk.runners import InMemoryRunner
from google.genai import types

# Enterprise Pattern: Configure Structured Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("AdvancedWorkflows")

# Enterprise Pattern: Configuration injection (basic form)
def load_config() -> dict:
    load_dotenv()
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"
    return {
        "model": os.getenv("MODEL", "gemini-2.5-flash")
    }

# Enterprise Pattern: Factory Functions for Agents
# Avoid global agent instances to ensure testability and prevent state leakage across threads.

def create_researcher_agent(model_name: str) -> Agent:
    """Factory to create a researcher agent."""
    return Agent(
        name="researcher",
        model=model_name,
        instruction="Write a brief 2-sentence summary of the history of the provided topic. Output only the summary."
    )

def create_formatter_agent(model_name: str) -> Agent:
    """Factory to create a formatter agent."""
    return Agent(
        name="formatter",
        model=model_name,
        instruction="Take the input text and format it into a neat markdown blockquote. Add a polite sign-off."
    )

def create_report_workflow(model_name: str) -> SequentialAgent:
    """Factory to build the Sequential workflow orchestrator."""
    logger.info("Initializing Sequential Workflow Agent.")
    return SequentialAgent(
        name="report_generator",
        description="Researches a topic and formats it.",
        sub_agents=[
            create_researcher_agent(model_name),
            create_formatter_agent(model_name)
        ]
    )

async def main():
    config = load_config()
    workflow_agent = create_report_workflow(config["model"])
    
    # Instantiate the Runner locally inside the execution context
    runner = InMemoryRunner(agent=workflow_agent, app_name="workflow_app")
    session = await runner.session_service.create_session(app_name="workflow_app", user_id="user1")
    
    logger.info("Application ready. Waiting for user input.")
    print("\n[System] Give me a historical topic, and my automated team will research and format it.")
    user_input = input("You: ").strip()
    
    if not user_input:
        logger.warning("No input provided. Exiting.")
        return
    
    logger.info(f"User requested research on: '{user_input}'")
    content = types.Content(role="user", parts=[types.Part.from_text(text=user_input)])
    
    # We still use print for the final streamed output to the console for UX, 
    # but application events are handled by the logger.
    print("\nAgent: ", end="", flush=True)
    async for event in runner.run_async(user_id="user1", session_id=session.id, new_message=content):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
    print("\n")
    logger.info("Workflow execution completed successfully.")

if __name__ == "__main__":
    asyncio.run(main())
