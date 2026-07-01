# Google Agent Development Kit (ADK) - Master Curriculum

Welcome to the structured learning path for the Google Agent Development Kit (ADK). This repository has been organized into a clear, sequential curriculum to help you learn, practice, and revise the core concepts of building agentic applications.

> [!NOTE]
> Agent Development Kit (ADK) is a powerful framework that allows you to easily connect multiple agents to one another for complex but easy-to-maintain workflows.

## The "Scratch to Pro" Curriculum

Follow these modules in order to build your understanding from basic scripts to production-ready enterprise systems:

### [Module 1: Basics](./01-Basics/)
Start here. Learn to initialize an agent, set up your environment, and use `InMemoryRunner` for basic CLI interactions.

### [Module 2: Tools and Integrations](./02-Tools-and-Integrations/)
Agents are most powerful when they can interact with the outside world. Learn how to empower agents with pre-built Google tools, wrappers (LangChain/CrewAI), and completely standalone REST API tools using Python `requests`.

### [Module 3: Routing and State](./03-Routing-and-State/)
Understand the Hierarchical Agent Tree. Learn how a parent agent routes conversations to specialized sub-agents, and how to use the Session State to pass data between them.

### [Module 4: Advanced Workflows](./04-Advanced-Workflows/)
Learn how to use Workflow Agents (`SequentialAgent`, `LoopAgent`, `ParallelAgent`) to orchestrate complex chains of actions without waiting for user input.

### [Module 5: Evaluation and Auditing](./05-Evaluation-and-Auditing/)
**[PRO CONCEPT]** Learn how to use Callbacks and the `llm_auditor` pattern to build an "LLM-as-a-Judge". Automatically audit and score your primary agents for safety and accuracy.

### [Module 6: Persistence](./06-Persistence/)
**[PRO CONCEPT]** `InMemoryRunner` memory is wiped on restart. Learn how to subclass `SessionService` to store conversation history and state in a persistent database (like JSON/SQLite/Firestore) across sessions.

### [Module 7: Deployment API](./07-Deployment-API/)
**[PRO CONCEPT]** Learn how to wrap your ADK `Runner` inside a `FastAPI` application to serve your agent as a standard REST endpoint to web frontends or for deployment to Google Cloud Run.

---

## How to use these modules for Revision
Each folder contains its own `README.md` designed as a study companion. Inside you will find:
1. **Module Goal**: What you should understand.
2. **Key Concepts**: Simplified explanations for quick recall.
3. **Revision Checklist**: Questions to test your understanding.
4. **Execution Steps**: How to run the local examples.

Happy learning!
