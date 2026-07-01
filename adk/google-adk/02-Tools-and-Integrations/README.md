# Module 2: Tools and Integrations

> [!TIP]
> Tools operate independently of the LLM's reasoning engine. This module covers everything from Google tools to standalone REST APIs.

## 🎯 Module Goal
Learn how to empower ADK agents with various tools to interact with external APIs, search the web, execute code, and retrieve information.

## 🧠 Key Concepts Explained

- **Custom Function Tools (Standalone)**: See the `standalone_agent` folder. You can use standard Python `requests` to call any REST API. This proves ADK is framework-agnostic.
- **Third-Party Integrations**: ADK supports wrappers like `LangchainTool` and `CrewaiTool`.
- **Pre-Built Tools**: Functionalities provided by Google, such as `google_search` or `VertexAiSearchTool`.

## ✅ Revision Checklist
- [ ] How do you configure ADK to use the generic Gemini API instead of Vertex AI?
- [ ] Why is the Python docstring critical when creating a custom function tool?

## 🚀 How to Run
Navigate to `standalone_agent/` and follow the instructions in that directory to test a completely standalone weather agent!
