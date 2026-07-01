import os
import sys
sys.path.append("..")
import google.cloud.logging
from callback_logging import log_query_to_model, log_model_response
from dotenv import load_dotenv
from google.adk.tools import VertexAiSearchTool
from google.adk import Agent
from google.adk.tools import AgentTool

from .tools import get_date

# Add the VertexAiSearchTool import below


load_dotenv()
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

YOUR_SEARCH_APP_ID = 'planet-search_1765974057946'
YOUR_PROJECT_ID = 'qwiklabs-gcp-00-fab9260ba896'

# Create your vertexai_search_tool and update its path below
vertexai_search_tool = VertexAiSearchTool(
    search_engine_id="projects/{YOUR_PROJECT_ID}/locations/global/collections/default_collection/engines/{YOUR_SEARCH_APP_ID}"
)

root_agent = Agent(
    # A unique name for the agent.
    name="root_agent",
    # The Large Language Model (LLM) that agent will use.
    model=os.getenv("MODEL"),
    # A short description of the agent's purpose, so other agents
    # in a multi-agent system know when to call it.
    description="Answer questions using your data store access.",
    # Instructions to set the agent's behavior.
    instruction="You analyze new planet discoveries and engage with the scientific community on them.",
    # Callbacks to log the request to the agent and its response.
    before_model_callback=log_query_to_model,
    after_model_callback=log_model_response,
    # Add the tools instructed below
       tools=[
       vertexai_search_tool,
    get_date
    ]
)
