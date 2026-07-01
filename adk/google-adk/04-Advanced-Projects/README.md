# Module 4: Advanced Projects & Evaluation

> [!TIP]
> This module brings all the ADK concepts together into cohesive applications and introduces evaluation and auditing.

## 🎯 Module Goal
Explore full applications built using ADK to see how Agents, Tools, and Workflows come together. Additionally, learn about system evaluation by using an auditor agent.

## 🧠 Key Concepts Explained

- **Integrated Developer Experience**: As seen in these project files, organizing agents into modules (like `app_agent`, `llm_auditor`) allows for a clean, scalable codebase.
- **LLM Auditor**: When building agentic workflows, you can build specialized agents (auditors) whose sole purpose is to evaluate the outputs and execution trajectories of other agents. This ensures reliability and correctness.
- **Callback Logging**: ADK allows you to attach callbacks to agents. These are custom code snippets that run at specific points (e.g., before an LLM call, after an LLM call), allowing you to intercept, modify, or log behavior seamlessly.

## ✅ Revision Checklist
Can you answer these questions confidently?
- [ ] How do you combine `SequentialAgent` and `LoopAgent` to create an advanced generative pipeline?
- [ ] What is the purpose of an LLM Auditor agent in a production system?
- [ ] How do callbacks help in debugging and tracking an agent's execution?

## 🚀 How to Run

Explore the subdirectories within this module.
For example, to run the primary app agent:
```bash
python3 -m pip install -r requirements.txt
# Run your specific agent scripts from here
```
*Note: Make sure your `.env` file is properly configured with your keys at the root of the project you are running.*
