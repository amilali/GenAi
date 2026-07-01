# Module 1: Basic Concepts

> [!TIP]
> This is your starting point for Google Agent Development Kit (ADK). Understand the core components before moving onto complex workflows.

## 🎯 Module Goal
Learn how to initialize a basic conversational agent, manage session state locally, and interact with the agent using the ADK Command Line Interface (CLI).

## 🧠 Key Concepts Explained

- **Agent**: The core building block designed to accomplish specific tasks. It is powered by an LLM (like Gemini) to reason and generate responses based on the provided instructions.
- **Session & State**: A conversation with an agent happens within a *Session*. The session tracks history (Events) and working memory (State) so the agent remembers what was said earlier.
- **Runner**: The engine that manages the execution flow. In this module, the `InMemoryRunner` is used to quickly run and test agents locally without needing a complex backend infrastructure.
- **Interactive CLI**: ADK provides a command-line interface (`adk run`) to easily chat with your agent in the terminal, making it simple to iterate and debug.

## ✅ Revision Checklist
Can you answer these questions confidently?
- [ ] What is the role of an Agent in the ADK framework?
- [ ] How does an agent remember the context of an ongoing conversation?
- [ ] What is the purpose of the `InMemoryRunner`?

## 🚀 How to Run

1. **Set up the Environment**:
   Copy the example environment variables to a new `.env` file.
   ```bash
   cp example_env .env
   ```
   Edit `.env` and add your `GOOGLE_API_KEY`.

2. **Run the Agent CLI**:
   Launch the interactive command line session.
   ```bash
   python3 agents.py
   # OR using the ADK CLI if configured:
   # adk run normal_agent
   ```
