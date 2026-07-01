import asyncio
import os
import requests
from dotenv import load_dotenv
from google.adk import Agent
from google.adk.runners import InMemoryRunner
from google.genai import types

# 1. Load environment variables
load_dotenv()

# Force standard Gemini API (Disable Vertex AI / Google Cloud dependencies)
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"
model_name = os.getenv("MODEL", "gemini-2.5-flash")

# 2. Create a Custom Tool calling a generic Public API (wttr.in)
def get_current_weather(city: str) -> dict:
    """Fetches the current weather for a given city using a public REST API.

    Args:
        city: The name of the city to get the weather for (e.g., 'Tokyo', 'London').

    Returns:
        A dictionary containing the weather report or an error message.
    """
    try:
        # Using a completely non-Google public REST API
        response = requests.get(f"https://wttr.in/{city}?format=j1", timeout=5)
        response.raise_for_status()
        
        data = response.json()
        current_condition = data['current_condition'][0]
        
        return {
            "status": "success",
            "city": city,
            "temperature_celsius": current_condition['temp_C'],
            "description": current_condition['weatherDesc'][0]['value']
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Could not fetch weather for {city}. Error: {str(e)}"
        }

# 3. Initialize the Agent (No Google Cloud Logging callbacks required)
weather_agent = Agent(
    name="weather_assistant",
    model=model_name,
    instruction="""You are a helpful weather assistant. 
    Use your tool to fetch the current weather when asked. 
    Answer concisely and friendly.""",
    tools=[get_current_weather]
)

async def main():
    print("--- Standalone ADK Weather Agent ---")
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        print("Error: Please set a valid GOOGLE_API_KEY in your .env file.")
        return

    # 4. Set up Runner and Session
    runner = InMemoryRunner(agent=weather_agent, app_name="standalone_app")
    session = await runner.session_service.create_session(
        app_name="standalone_app",
        user_id="local_user"
    )
    
    print("Ready! Ask for the weather in any city (e.g., 'What is the weather in Paris?').")
    print("Type 'exit' to quit.\n")

    # 5. Conversation Loop
    while True:
        try:
            user_input = input("You: ").strip()
        except EOFError:
            break

        if not user_input or user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        content = types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)]
        )

        print("Agent: ", end="", flush=True)
        
        async for event in runner.run_async(
            user_id="local_user",
            session_id=session.id,
            new_message=content,
        ):
            # Show tool usage feedback to the user
            if event.tool_call_request:
                print(f"\n[Agent is using tool: {event.tool_call_request.calls[0].name}...]")
                print("Agent: ", end="", flush=True)
            
            # Print text response
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        print(part.text, end="", flush=True)
        print("\n")

if __name__ == "__main__":
    asyncio.run(main())
