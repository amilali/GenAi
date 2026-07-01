# Google Agent Development Kit (ADK) - Master Curriculum

Welcome to the structured learning path for the Google Agent Development Kit (ADK). This repository has been organized into a clear, sequential curriculum to help you learn, practice, and revise the core concepts of building agentic applications.

> [!NOTE]
> Agent Development Kit (ADK) is a powerful framework that allows you to easily connect multiple agents to one another for complex but easy-to-maintain workflows.

## Course Modules

Follow these modules in order to build your understanding of the framework:

### [Module 1: Basic Concepts](./01-Basic-Concepts/)
Start here. Learn the foundational building blocks of ADK. You'll initialize a basic agent, set up your environment, and use `InMemoryRunner` to manage a session state and interact via the CLI.

### [Module 2: Tool Integrations](./02-Tool-Integrations/)
Agents are most powerful when they can interact with the outside world. This module covers empowering agents with pre-built tools (like Google Search), third-party tools (LangChain, CrewAI), and your own custom Python functions. You'll also learn about Vertex AI Search integration.

### [Module 3: Multi-Agent Workflows](./03-Multi-Agent-Workflows/)
Learn how to build complex systems where multiple specialized agents collaborate. This module dives into hierarchical parent/sub-agent routing, manipulating session states to pass data, and orchestrating flows using `SequentialAgent`, `LoopAgent`, and `ParallelAgent`.

### [Module 4: Advanced Projects](./04-Advanced-Projects/)
Bring everything together in a comprehensive project. This module demonstrates integrating tools, multi-agent workflows, state management, and introduces specialized auditing agents (`llm_auditor`) to monitor and evaluate your systems.

### [Module 5: Standalone ADK](./05-Standalone-ADK/)
Learn how to run ADK completely independent of Google Cloud Platform (GCP). Use the generic Developer Gemini API instead of Vertex AI, and learn how to use a standard REST API as a custom function tool without relying on Google-specific services or logging.

---

## How to use these modules for Revision
Each folder contains its own `README.md` designed as a study companion. Inside you will find:
1. **Module Goal**: What you should understand.
2. **Key Concepts**: Simplified explanations for quick recall.
3. **Revision Checklist**: Questions to test your understanding.
4. **Execution Steps**: How to run the local examples.

Happy learning!
