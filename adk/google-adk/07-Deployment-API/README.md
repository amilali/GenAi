# Module 7: Deployment API (FastAPI)

> [!TIP]
> This is how you serve your ADK agent to the world! Wrap it in FastAPI to create an endpoint for web frontends, mobile apps, or to deploy on Google Cloud Run.

## 🎯 Module Goal
Learn how to wrap your ADK `Runner` inside a FastAPI application to expose it as an HTTP REST endpoint.

## 🧠 Key Concepts Explained

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **Stateless Endpoints**: In an API, every HTTP request is stateless. You pass the `user_id` and `session_id` in the request body, load the session from the `SessionService`, append the new message, and return the agent's response as a JSON string.
- **Streaming vs Polling**: While ADK supports async streaming (`async for event in runner.run_async()`), for standard APIs, you often await the final response and send it back as one JSON packet.

## 🚀 How to Run

1. **Install requirements**:
   ```bash
   pip install fastapi uvicorn google-adk
   ```

2. **Start the API Server**:
   ```bash
   uvicorn main:app --reload
   ```

3. **Test the Endpoint**:
   Open a new terminal and send a POST request:
   ```bash
   curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d '{"user_id": "test_user", "message": "Hello, who are you?"}'
   ```
