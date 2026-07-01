import logging
import os
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from google.genai import types

from config import Settings, get_settings
from factory import create_api_agent, create_runner

# Enterprise Pattern: Structured Logging for Web Services
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("api_server")

app = FastAPI(title="ADK Enterprise Production API")

# --- Dependency Injection Setup ---

def get_runner(settings: Settings = Depends(get_settings)):
    """FastAPI Dependency: Injects a properly configured Runner per request cycle."""
    # Note: In a real high-throughput production environment, you might cache the runner
    # at the application state level depending on your concurrency model.
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = settings.google_genai_use_vertexai
    agent = create_api_agent(settings)
    return create_runner(settings, agent)


# --- API Models ---

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
    status: str = "success"


# --- Service Layer & Routing ---

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    req: ChatRequest, 
    runner=Depends(get_runner), 
    settings: Settings = Depends(get_settings)
):
    """
    Endpoint for communicating with the ADK Agent.
    """
    logger.info(f"Received request from user_id: {req.user_id}")
    
    try:
        # 1. Load or create session
        session = await runner.session_service.create_session(
            app_name=settings.app_name, 
            user_id=req.user_id
        )
        
        # 2. Prepare message
        content = types.Content(role="user", parts=[types.Part.from_text(text=req.message)])
        
        # 3. Execute ADK Agent workflow
        logger.info(f"Executing agent task for session {session.id}...")
        full_response = ""
        
        async for event in runner.run_async(user_id=req.user_id, session_id=session.id, new_message=content):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        full_response += part.text
                        
        logger.info(f"Successfully generated response for user_id: {req.user_id}")
        return ChatResponse(reply=full_response)
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error processing agent request.")
