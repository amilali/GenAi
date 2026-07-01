import asyncio
import os
import json
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.runners import Runner
from google.adk.sessions import SessionService, Session
from google.genai import types

load_dotenv()
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"

# 1. Create a Custom Session Service backed by a local JSON file
class FileBackedSessionService(SessionService):
    def __init__(self, filepath="database.json"):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump({}, f)

    async def create_session(self, app_name: str, user_id: str) -> Session:
        session = Session(app_name=app_name, user_id=user_id, id=f"{app_name}_{user_id}_session")
        await self.save_session(session)
        return session

    async def load_session(self, app_name: str, user_id: str, session_id: str) -> Session:
        with open(self.filepath, "r") as f:
            data = json.load(f)
        if session_id in data:
            # Reconstruct session from JSON dict (simplified for example)
            session = Session(**data[session_id])
            return session
        return await self.create_session(app_name, user_id)

    async def save_session(self, session: Session):
        with open(self.filepath, "r") as f:
            data = json.load(f)
        
        # Serialize the session model to dict
        data[session.id] = session.model_dump()
        
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

# 2. Basic Agent
memory_agent = Agent(
    name="memory_assistant",
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    instruction="You are an assistant with long-term memory. Acknowledge past interactions if the user brings them up."
)

async def main():
    # 3. Use the custom SessionService in a standard Runner
    session_service = FileBackedSessionService()
    runner = Runner(agent=memory_agent, app_name="memory_app", session_service=session_service)
    
    session = await session_service.load_session("memory_app", "user1", "memory_app_user1_session")
    
    print("--- Persistent ADK Agent ---")
    print(f"Loaded session with {len(session.events)} past events.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]: break
        
        content = types.Content(role="user", parts=[types.Part.from_text(text=user_input)])
        async for event in runner.run_async(user_id="user1", session_id=session.id, new_message=content):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text: print(part.text, end="", flush=True)
        print()

if __name__ == "__main__":
    asyncio.run(main())
