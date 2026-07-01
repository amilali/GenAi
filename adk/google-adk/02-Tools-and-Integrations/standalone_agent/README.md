# Module 5: Standalone ADK (Without Google Cloud)

> [!TIP]
> You do not need Google Cloud Platform (GCP) or Vertex AI to use the Google Agent Development Kit! You can use it purely with the standard Gemini Developer API and generic external services.

## 🎯 Module Goal
Learn how to configure ADK to run in a fully standalone mode and how to integrate standard, non-Google public APIs (like a weather service) into your agent workflow.

## 🧠 Key Concepts Explained

- **Disabling Vertex AI**: By default, many ADK tutorials assume you are on GCP. By explicitly setting the environment variable `GOOGLE_GENAI_USE_VERTEXAI="0"`, you tell ADK to use the generic Gemini developer API (via a simple `GOOGLE_API_KEY`) instead of looking for GCP project credentials.
- **Removing Cloud Logging**: Standard Python logging or print statements work perfectly fine. You do not need to import `google.cloud.logging` to track what your agent is doing.
- **Generic API Tools**: ADK is framework-agnostic when it comes to tools. If you can write a Python function to call a REST API using the standard `requests` library, you can give it to an ADK agent as a tool. No special Google integrations required.

## ✅ Revision Checklist
Can you answer these questions confidently?
- [ ] What environment variable must be set to `0` to prevent ADK from trying to authenticate with Google Cloud?
- [ ] Do you need a Google Cloud Project to build an ADK agent?
- [ ] How does the agent know how to format its HTTP request to the external Weather API?

## 🚀 How to Run

1. **Set up the Environment**:
   Copy `.env.example` to `.env`.
   ```bash
   cp .env.example .env
   ```
   Add your `GOOGLE_API_KEY`. (You can get a free one from Google AI Studio).

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Agent**:
   ```bash
   python3 agent.py
   ```
   Ask the agent: *"What is the weather like in Tokyo?"* and watch it fetch real-time data from a non-Google REST API!
