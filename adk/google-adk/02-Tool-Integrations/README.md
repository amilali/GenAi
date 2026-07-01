# Module 2: Tool Integrations

> [!TIP]
> Tools are what turn simple chatbots into powerful autonomous agents. Tools operate independently of the LLM's reasoning engine.

## 🎯 Module Goal
Learn how to empower ADK agents with various tools to interact with external APIs, search the web, execute code, and retrieve information.

## 🧠 Key Concepts Explained

- **Pre-Built Tools**: Ready-to-use functionalities provided by Google, such as `google_search`, `built_in_code_execution`, and `VertexAiSearchTool` for RAG (Retrieval-Augmented Generation).
- **Third-Party Integrations**: ADK supports wrappers like `LangchainTool` and `CrewaiTool`. This allows you to leverage massive ecosystems of community-built tools directly in your ADK agents.
- **Custom Function Tools**: The easiest way to create a tool is to write a standard Python function. 
  - *Critical Rule*: The function must have a properly formatted docstring! The LLM reads the docstring to understand *when* and *how* to use the tool.
  - *Best Practice*: Return a Python dictionary containing a `"status"` key.
- **Agent-as-a-Tool (`AgentTool`)**: You can wrap an entire agent in an `AgentTool` wrapper and give it to another agent as a tool. This is highly useful to bypass limitations (like combining search tools and non-search tools in the same root agent).
- **LongRunningFunctionTool**: Used for operations that take a long time (or require human approval) so they don't block the agent's main execution loop.

## ✅ Revision Checklist
Can you answer these questions confidently?
- [ ] Why is the Python docstring critical when creating a custom function tool?
- [ ] How do you integrate a community tool from LangChain into ADK?
- [ ] Why might you use `AgentTool` instead of assigning a tool directly to the root agent?
- [ ] What is the preferred return type for a custom Python function tool?

## 🚀 How to Run

1. **Set up the Environment**:
   Inside this module, ensure you have a `.env` file containing your GCP Project details and Model configurations (e.g., `GOOGLE_GENAI_USE_VERTEXAI=TRUE`, `GOOGLE_CLOUD_PROJECT=...`).

2. **Run the Dev UI**:
   ADK comes with a web UI that is excellent for visualizing tool calls and responses.
   ```bash
   cd adk_tools
   adk web
   ```
   Open `http://127.0.0.1:8000` to select different agents (`langchain_tool_agent`, `function_tool_agent`, etc.) and test their specific tool integrations.
