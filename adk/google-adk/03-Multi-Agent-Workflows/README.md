# Module 3: Multi-Agent Workflows

> [!TIP]
> This module represents the true power of ADK: building scalable multi-agent systems by composing multiple specialized agents in a hierarchy.

## 🎯 Module Goal
Learn how to create a hierarchical tree of agents (parents and sub-agents), manage long-term state data between them, and use Workflow Agents (`SequentialAgent`, `LoopAgent`, `ParallelAgent`) to orchestrate complex pipelines.

## 🧠 Key Concepts Explained

### 1. Hierarchical Agent Tree (Routing)
Instead of a single massive agent prompt, ADK uses a tree structure. 
- A **`root_agent`** acts as a parent. It evaluates the user's intent and transfers the conversation to a specialized **sub-agent** based on that sub-agent's `description`.
- This mirrors real-world collaborative teams and provides strict control over the flow of the conversation.

### 2. Session State
- Each conversation occurs in a `Session` object.
- The `State` is a dictionary within the session. Agents can read from the state (using key templating in instructions like `{ key_name? }`) and write to it (using custom tool functions).
- State allows you to maintain data structures (like a list of choices or a document draft) across multiple turns and between different agents.

### 3. Workflow Agents
These are special parent agents designed for orchestrated automation (running without breaking for a user turn):
- **`SequentialAgent`**: Executes its sub-agents linearly (Agent A -> Agent B -> Agent C). Great for "Plan and Execute" workflows.
- **`LoopAgent`**: Executes its sub-agents in a loop repeatedly until a `max_iterations` limit is hit, or an agent uses an `exit_loop` tool. Perfect for "Iterative Refinement" (e.g. Writer -> Critic -> Writer).
- **`ParallelAgent`**: Executes its sub-agents concurrently. Excellent for tasks that can fan out (e.g., getting reviews from multiple independent experts simultaneously).

## ✅ Revision Checklist
Can you answer these questions confidently?
- [ ] How does a parent agent know which sub-agent to route to?
- [ ] How can an agent read a value from the Session State dictionary inside its instruction prompt?
- [ ] Which workflow agent would you use to have three separate researchers gather information at the exact same time?
- [ ] Which workflow agent would you use to iteratively improve a document until it meets a specific quality threshold?

## 🚀 How to Run

1. **Set up the Environment**:
   Ensure you have a `.env` file copied into the `workflow_agents` directory.
   
2. **Run the Interactive CLI**:
   ```bash
   adk run parent_and_subagents
   ```
   Or use the Dev UI to visualize the Agent Graph:
   ```bash
   adk web --reload_agents
   ```
   *Tip: In the Dev UI, check out the "Event View" graph and the "State" tab to see how state values are updated!*
