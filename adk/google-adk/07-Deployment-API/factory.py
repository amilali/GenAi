from google.adk import Agent
from google.adk.runners import InMemoryRunner
from config import Settings

def create_api_agent(settings: Settings) -> Agent:
    """
    Enterprise Pattern: Factory for the Agent
    Injects configuration rather than relying on global state.
    """
    return Agent(
        name="api_assistant",
        model=settings.model_name,
        instruction="You are a highly efficient API backend assistant. Provide concise answers."
    )

def create_runner(settings: Settings, agent: Agent) -> InMemoryRunner:
    """
    Enterprise Pattern: Factory for the Runner
    In production, this could easily be swapped to a custom runner
    using a database-backed SessionService (like in Module 06).
    """
    return InMemoryRunner(
        agent=agent, 
        app_name=settings.app_name
    )
