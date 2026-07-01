# Module 6: Persistence

> [!TIP]
> Production apps cannot rely on `InMemoryRunner` because memory is wiped when the server restarts. You need a persistent backend.

## 🎯 Module Goal
Learn how to implement a custom Session Service to store conversation history and state in a database (like SQLite or JSON) so agents remember users across sessions.

## 🧠 Key Concepts Explained

- **`SessionService`**: ADK's base class for managing sessions. By subclassing this, you can intercept `save_session()` and `load_session()` to push data to Cloud Firestore, PostgreSQL, or a local file.
- **Why it matters**: If a user chats with your agent on their phone, closes the app, and comes back tomorrow, the agent needs to pull their Session State and Events from a persistent database.

## 🚀 How to Run
```bash
python3 agent.py
```
*Try chatting, typing `exit`, and then running the script again. Notice how it remembers the conversation from the JSON file!*
