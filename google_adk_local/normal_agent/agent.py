import asyncio
import os
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.runners import InMemoryRunner
from google.genai import types

# Load environment variables from .env file
load_dotenv()

# Basic configuration
# Ensure you have the GOOGLE_API_KEY environment variable set.
DEFAULT_MODEL = "gemini-flash-latest"

model_name = os.getenv("MODEL", DEFAULT_MODEL)

# 1. Initialize the LLM Agent
# We define the model and the persona (instruction)
# This must be exposed as 'root_agent' for the adk CLI to find it.
root_agent = Agent(
    model=model_name,
    name="helpful_assistant",
    instruction="You are a helpful and friendly AI assistant. Keep answers concise.",
)

# Force using Google AI API (Local/Non-Vertex)
# os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"

async def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        return
    
    print(f"Initializing agent with model: {model_name} (Local/API Key mode)")

    # 2. Set up the Runner
    # The runner handles the orchestration of the agent and state.
    # InMemoryRunner keeps the session state in memory.
    runner = InMemoryRunner(
        agent=root_agent,
        app_name="my_adk_app",
    )

    # 3. Create a Conversation Session
    # Sessions track the history of the conversation for a user.
    user_id = "local_user"
    session = await runner.session_service.create_session(
        app_name="my_adk_app",
        user_id=user_id
    )
    print(f"Session created (ID: {session.id})")
    print("Type 'exit' or 'quit' to stop.")

    # 4. Run the Conversation Loop
    while True:
        try:
            user_input = input("\nUser: ").strip()
        except EOFError:
            break

        if not user_input or user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Construct the message object using google.genai types
        content = types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)]
        )

        print("Agent: ", end="", flush=True)
        
        # runner.run_async executes the turn and yields events (e.g. chunks of response)
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session.id,
            new_message=content,
        ):
            # Process and display the response content
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        print(part.text, end="", flush=True)
        print() # New line after response

if __name__ == "__main__":
    asyncio.run(main())
