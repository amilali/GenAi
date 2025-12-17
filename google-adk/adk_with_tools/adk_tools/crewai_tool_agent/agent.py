import os
import sys
sys.path.append("..")
import google.cloud.logging
from callback_logging import log_query_to_model, log_model_response

from dotenv import load_dotenv

from google.genai import types
from google.adk import Agent
from google.adk.tools.crewai_tool import CrewaiTool
from crewai_tools import ScrapeWebsiteTool


load_dotenv()
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

root_agent = Agent(
    name="crewai_tool_agent",
    model=os.getenv("MODEL"),
    description="Agent to write files.",
    instruction="Write files as requested by the user.",
    generate_content_config=types.GenerateContentConfig(
        temperature=0
    ),    
    tools = [
        CrewaiTool(
            name="scrape_apnews",
            description=(
                """Scrapes the latest news content from the Associated Press (AP) News website."""
            ),
            tool=ScrapeWebsiteTool(website_url='https://apnews.com/')
        )
    ],

    before_model_callback=log_query_to_model,
    after_model_callback=log_model_response,    
    # Add the CrewAI ScrapeWebsiteTool below


)