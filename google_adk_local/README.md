# Google ADK Basic Agent Demo

This directory contains a basic AI "Agent" implementation using the Google Agent Development Kit (ADK).

## Setup

1. **Environment Variables**: 
   Copy `example_env` to a new file named `.env`:
   ```bash
   cp example_env .env
   ```
   Edit `.env` and add your `GOOGLE_API_KEY`.

2. **Run the Agent**:
   ```bash
   python3 agent.py
   ```

## Features
- Initializes a basic conversational agent.
- Uses `InMemoryRunner` to manage session state.
- Interactive CLI for chatting with the agent.
