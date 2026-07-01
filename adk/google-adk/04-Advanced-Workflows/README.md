# Module 4: Advanced Workflows

> [!TIP]
> Workflow Agents execute without waiting for a user turn. They orchestrate complex chains of actions between multiple sub-agents automatically.

## 🎯 Module Goal
Learn how to use ADK's built-in orchestrators: `SequentialAgent`, `LoopAgent`, and `ParallelAgent`.

## 🧠 Key Concepts Explained

- **`SequentialAgent`**: Executes sub-agents one after another in a linear pipeline. Useful for "Plan and Execute" architectures.
- **`LoopAgent`**: Executes sub-agents in a repeating circle until a maximum iteration limit is reached or an agent uses the `exit_loop` tool. Perfect for drafting and revision cycles (Writer -> Critic -> Writer).
- **`ParallelAgent`**: Executes sub-agents concurrently. Excellent for "Fan out and gather" workflows.

## 🚀 How to Run
```bash
python3 agent.py
```
*This will run a Sequential Agent that researches a topic and then writes a report automatically.*
