# Module 5: Evaluation and Auditing

> [!TIP]
> Pro developers don't just build agents; they test and evaluate them. This module introduces the `llm_auditor`.

## 🎯 Module Goal
Learn how to use callbacks and "LLM-as-a-Judge" agents to audit and score the outputs of your primary agents.

## 🧠 Key Concepts Explained

- **Callbacks**: Functions that trigger before or after an LLM executes. You can use these to log data or inject additional checks.
- **`llm_auditor`**: An ADK pattern where a secondary agent is spun up *during* the execution of your primary agent to grade its responses based on a rubric (e.g., "Is this response polite?", "Did it leak PII?").

## 🚀 How to Run
Check out the code in the `llm_auditor` directory to see how an auditor agent intercepts and grades the responses of a standard agent.
