https://partner.skills.google/paths/3033/course_templates/1275/labs/606594


# Build Multi-Agent Systems with ADK

experimentLabschedule1 hour 30 minutesuniversal\_currency\_altNo costshow\_chartAdvanced

[](https://partner.skills.google/focuses/711657018/reviews?parent=course_session)

infoThis lab may incorporate AI tools to support your learning.

## GENAI106

## Overview

This lab covers orchestrating multi-agent systems within the Google Agent Development Kit (Google ADK).

This lab assumes that you are familiar with the basics of ADK and tool use as covered in the labs:

* Get started with Google Agent Development Kit (ADK)
* Empower ADK agents with tools

## Objectives

In this lab, you will:

* Create multiple agents and relate them to one another with parent to sub-agent relationships.
* Build content across multiple turns of conversation and multiple agents by writing to a session's state dictionary.
* Instruct agents to read values from the session state to use as context for their responses.
* Use workflow agents to pass the conversation between agents directly.

## Setup and requirements

#### Before you click the Start Lab button

Read these instructions. Labs are timed and you cannot pause them. The timer, which starts when you click **Start Lab**, shows how long Google Cloud resources will be made available to you.

This Qwiklabs hands-on lab lets you do the lab activities yourself in a real cloud environment, not in a simulation or demo environment. It does so by giving you new, temporary credentials that you use to sign in and access Google Cloud for the duration of the lab.

#### What you need

To complete this lab, you need:

* Access to a standard internet browser (Chrome browser recommended).
* Time to complete the lab.

**Note:** If you already have your own personal Google Cloud account or project, do not use it for this lab.

**Note:** If you are using a Pixelbook, open an Incognito window to run this lab.

### How to start your lab and sign in to the Google Cloud console

1. Click the **Start Lab** button. If you need to pay for the lab, a dialog opens for you to select your payment method. On the left is the Lab Details pane with the following:

   * The Open Google Cloud console button
   * Time remaining
   * The temporary credentials that you must use for this lab
   * Other information, if needed, to step through this lab
2. Click **Open Google Cloud console** (or right-click and select **Open Link in Incognito Window** if you are running the Chrome browser).
   The lab spins up resources, and then opens another tab that shows the Sign in page.
   ***Tip:*** Arrange the tabs in separate windows, side-by-side.
   **Note:** If you see the **Choose an account** dialog, click **Use Another Account**.
3. If necessary, copy the **Username** below and paste it into the **Sign in** dialog.

   ```
   student-02-c07ce34a4730@qwiklabs.net
   ```

   **Copied!**

   You can also find the Username in the Lab Details pane.
4. Click **Next**.
5. Copy the **Password** below and paste it into the **Welcome** dialog.

   ```
   Ndmp6L6kH7eT
   ```

   **Copied!**

   You can also find the Password in the Lab Details pane.
6. Click **Next**.
   **Important:** You must use the credentials the lab provides you. Do not use your Google Cloud account credentials.**Note:** Using your own Google Cloud account for this lab may incur extra charges.
7. Click through the subsequent pages:

   * Accept the terms and conditions.
   * Do not add recovery options or two-factor authentication (because this is a temporary account).
   * Do not sign up for free trials.

After a few moments, the Google Cloud console opens in this tab.

**Note:** To access Google Cloud products and services, click the **Navigation menu** or type the service or product name in the **Search** field. ![Navigation menu icon and Search field](https://cdn.qwiklabs.com/9Fk8NYFp3quE9mF%2FilWF6%2FlXY9OUBi3UWtb2Ne4uXNU%3D)## Multi-Agent Systems

The Agent Development Kit empowers developers to get more reliable, sophisticated, multi-step behaviors from generative models. Instead of writing long, complex prompts that may not deliver results reliably, you can construct a flow of multiple, simple agents that can collaborate on complex problems by dividing tasks and responsibilities.

This architectural approach offers several key advantages such as:

* **Easier to design:** You can think in terms of agents with specific jobs and skills.
* **Specialized functions with more reliable performance:** Specialized agents can learn from clear examples to become more reliable at their specific tasks.
* **Organization:** Dividing the workflow into distinct agents allows for a more organized, and therefor easier to think about, approach.
* **Improvability and maintainability:** It is easier to improve or fix a specialized component rather than make changes to a complex agent that may fix one behavior but might impact others.
* **Modularity:** Distinct agents from one workflow can be easily copied and included in other similar workflows.

### The Hierarchical Agent Tree

![Tree structure showing hierarchical agents](https://cdn.qwiklabs.com/hc9s%2BOp9Z7JMMXEZLxYoHF%2Bi6Zm1aSaRgjeWOc%2BO7oY%3D)

In Agent Development Kit, you organize your agents in a tree-like structure. This helps limit the options for transfers for each agent in the tree, making it easier to control and predict the possible routes the conversation can take through the tree. Benefits of the hierarchical structure include:

* It draws **inspiration from real-world collaborative teams**, making it easier to design and reason about the behavior of the multi-agent system.
* It is **intuitive for developers**, as it mirrors common software development patterns.
* It provides **greater control over the flow** of information and task delegation within the system, making it easier to understand possible pathways and debug the system. For example, if a system has two report-generation agents at different parts of its flow with similar descriptions, the tree structure makes it easier to ensure that the correct one is invoked.

The structure always begins with the agent defined in the **root\_agent** variable (although it may have a different user-facing **name** to identify itself). The `root_agent` may act as a **parent** to one or more **sub-agents**. Each sub-agent agent may have its own sub-agents.

## Task 1. Install ADK and set up your environment

In this lab environment, the **Vertex AI API has been enabled for you**. If you were to follow these steps in your own project, you would enable it by navigating to Vertex AI and following the prompt to enable it.

### Prepare a Cloud Shell Editor tab

1. With your Google Cloud console window selected, open Cloud Shell by pressing the **G** key and then the **S** key on your keyboard. Alternatively, you can click the Activate Cloud Shell button (![Activate Cloud Shell](https://cdn.qwiklabs.com/4VN7LZSIdFTyYDAsU9S9rLW42Uc1xJb90mZnNQQCKec%3D)) in the upper right of the Cloud console.
2. Click **Continue**.
3. When prompted to authorize Cloud Shell, click **Authorize**.
4. In the upper right corner of the Cloud Shell Terminal panel, click the **Open in new window** button ![Open in new window button](https://cdn.qwiklabs.com/0YM9CoxqcCKGEd4zWU%2B4%2BI%2FLNhKzdahTCRN5Apwtz0U%3D).
5. In the Cloud Shell Terminal, enter the following to open the Cloud Shell Editor to your home directory:

   ```
   cloudshell workspace ~
   ```

   **Copied!**
6. Close any additional tutorial or Gemini panels that appear on the right side of the screen to save more of your window for your code editor.
7. Throughout the rest of this lab, you can work in this window as your IDE with the Cloud Shell Editor and Cloud Shell Terminal.

### Download and install ADK and code samples for this lab

1. Paste the following commands into the Cloud Shell Terminal to copy code files from a Cloud Storage bucket for this lab:

   ```
   gcloud storage cp -r gs://qwiklabs-gcp-02-46166d6bd366-bucket/adk_multiagent_systems .
   ```

   **Copied!**
2. Update your `PATH` environment variable, **install ADK**, and install additional lab requirements by running the following commands in the Cloud Shell Terminal.

   ```
   export PATH=$PATH:"/home/${USER}/.local/bin"
   python3 -m pip install google-adk -r adk_multiagent_systems/requirements.txt
   ```

   **Copied!**

## Task 2. Explore transfers between parent, sub-agent, and peer agents

The conversation always begins with the agent defined as the **root\_agent** variable.

The default behavior of a parent agent is to understand the **description** of each sub-agent and determine if control of the conversation should be transferred to a sub-agent at any point.

You can help guide those transfers in the parent's `instruction` by referring to the sub-agents by name (the values of their `name` parameter, not their variable names). Try an example:

1. In the Cloud Shell Terminal, run the following to create a `.env` file to authenticate the agent in the **parent\_and\_subagents** directory.

   ```
   cd ~/adk_multiagent_systems
   cat << EOF > parent_and_subagents/.env
   GOOGLE_GENAI_USE_VERTEXAI=TRUE
   GOOGLE_CLOUD_PROJECT=qwiklabs-gcp-02-46166d6bd366
   GOOGLE_CLOUD_LOCATION=global
   MODEL=gemini-2.5-flash
   EOF
   ```

   **Copied!**
2. Run the following command to copy that `.env` file to the **workflow\_agents** directory, which you will use later in the lab:

   ```
   cp parent_and_subagents/.env workflow_agents/.env
   ```

   **Copied!**
3. In the Cloud Shell Editor file explorer pane, navigate to the **adk\_multiagent\_systems/parent\_and\_subagents** directory.
4. Click on the **agent.py** file to open it.

**Tip:** Because Python code requires that we define our sub-agents before we can add them to an agent, in order to read an agent.py file in the order of the conversation flow, you may want to start reading with the bottom agent and work back towards the top.5. Notice that there are three agents here:

* a **root\_agent** named `steering` (its name is used to identify it in ADK's dev UI and command line interfaces). It asks the user a question (if they know where they'd like to travel or if they need some help deciding), and the user's response to that question will help this steering agent know which of its two sub-agents to steer the conversation towards. Notice that it only has a simple `instruction` that does not mention the sub-agents, but it is aware of its sub-agents' descriptions.
* a **travel\_brainstormer** that helps the user brainstorm destinations if they don't know where they would like to visit.
* an **attractions\_planner** that helps the user build a list of things to do once they know which country they would like to visit.

5. Make **travel\_brainstormer** and **attractions\_planner** sub-agents of the **root\_agent** by adding the following line to the creation of the **root\_agent**:

   ```
   sub_agents=[travel_brainstormer, attractions_planner]
   ```

   **Copied!**
6. **Save** the file.
7. Note that you don't add a corresponding *parent* parameter to the sub-agents. The hierarchical tree is defined only by specifying `sub_agents` when creating parent agents.
8. In the Cloud Shell Terminal, run the following to use the ADK command line interface to chat with your agent:

   ```
   cd ~/adk_multiagent_systems
   adk run parent_and_subagents
   ```

   **Copied!**
9. When you are presented the `[user]:` prompt, greet the agent with:

   ```
   hello
   ```

   **Copied!**

   **Example output (yours may be a little different):**

   ```
   user: hello
   [steering]: Hi there! Do you already have a country in mind for your trip, or would you like some help deciding where to go?
   ```
10. Tell the agent:

    ```
    I could use some help deciding.
    ```

    **Copied!**

    **Example output (yours may be a little different):**

    ```
    user: I could use some help deciding.
    [travel_brainstormer]: Okay! To give you the best recommendations, I need to understand what you're looking for in a trip.
    ...
    ```
11. Notice from the name **[travel\_brainstormer]** in brackets in the response that the **root\_agent** (named **[steering]**) has transferred the conversation to the appropriate sub-agent based on that sub-agent's `description` alone.
12. At the `user:` prompt, enter `exit` to end the conversation.
13. You can also provide your agent more detailed instructions about when to transfer to a sub-agent as part of its `instructions`. In the **agent.py** file, add the following lines to the **root\_agent**'s `instruction`:

    ```
    If they need help deciding, send them to
    'travel_brainstormer'.
    If they know what country they'd like to visit,
    send them to the 'attractions_planner'.
    ```

    **Copied!**
14. **Save** the file.
15. In the Cloud Shell Terminal, run the following to start the command line interface again:

    ```
    adk run parent_and_subagents
    ```

    **Copied!**
16. Greet the agent with:

    ```
    hello
    ```

    **Copied!**
17. Reply to the agent's greeting with:

    ```
    I would like to go to Japan.
    ```

    **Copied!**

    **Example output (yours may be a little different):**

    ```
    user: I would like to go to Japan.
    [attractions_planner]: Okay, I can help you with that! Here are some popular attractions in Japan:

    *   **Tokyo:**
        *   Senso-ji Temple
        *   Shibuya Crossing
        *   Tokyo Skytree
    *   **Kyoto:**
        ...
    ```
18. Notice that you have been transferred to the other sub-agent, **attractions\_planner**.
19. Reply with:

    ```
    Actually I don't know what country to visit.
    ```

    **Copied!**

    **Example output (yours may be a little different):**

    ```
    user: actually I don't know what country to visit
    [travel_brainstormer]: Okay! I can help you brainstorm some countries for travel...
    ```
20. Notice you have been transferred to the **travel\_brainstormer** agent, which is a **peer** agent to the **attractions\_planner**. This is allowed by default. If you wanted to prevent transfers to peers, you could have set the `disallow_transfer_to_peers` parameter to `True` on the **attractions\_planner** agent.
21. At the user prompt, type `exit` to end the session.

**Step-by-step pattern:** If you are interested in an agent that guides a user through a process step-by-step, one useful pattern can be to make the first step the `root_agent` with the second step agent its only sub-agent, and continue with each additional step being the only sub-agent of the previous step's agent.Click **Check my progress** to verify the objective.

Assessment Completed!

Explore transfers between parent, sub-agent, and peer agents

Assessment Completed!

## Task 3. Use session state to store and retrieve specific information

Each conversation in ADK is contained within a `Session` that all agents involved in the conversation can access. A session includes the conversation history, which agents read as part of the context used to generate a response. The session also includes a **session state** dictionary that you can use to take greater control over the most important pieces of information you would like to highlight and how they are accessed.

This can be particularly helpful to pass information between agents or to maintain a simple data structure, like a list of tasks, over the course of a conversation with a user.

To explore adding to and reading from state:

1. Return to the file **adk\_multiagent\_systems/parent\_and\_subagents/agent.py**
2. Paste the following function definition after the `# Tools` header:

   ```
   def save_attractions_to_state(
       tool_context: ToolContext,
       attractions: List[str]
   ) -> dict[str, str]:
       """Saves the list of attractions to state["attractions"].

       Args:
           attractions [str]: a list of strings to add to the list of attractions

       Returns:
           None
       """
       # Load existing attractions from state. If none exist, start an empty list
       existing_attractions = tool_context.state.get("attractions", [])

       # Update the 'attractions' key with a combo of old and new lists.
       # When the tool is run, ADK will create an event and make
       # corresponding updates in the session's state.
       tool_context.state["attractions"] = existing_attractions + attractions

       # A best practice for tools is to return a status message in a return dict
       return {"status": "success"}
   ```

   **Copied!**
3. In this code, notice:

   * The session is passed to your tool function as `ToolContext`. All you need to do is assign a parameter to receive it, as you see here with the parameter named `tool_context`. You can then use `tool_context` to access session information like conversation history (through `tool_context.events`) and the session state dictionary (through `tool_context.state`). When the `tool_context.state` dictionary is modified by your tool function, those changes will be reflected in the session's state after the tool finishes its execution.
   * The docstring provides a clear description and sections for argument and return values.
   * The commented function code demonstrates how easy it is to make updates to the state dictionary.
4. Add the tool to the **attractions\_planner** agent by adding the `tools` parameter when the agent is created:

   ```
   tools=[save_attractions_to_state]
   ```

   **Copied!**
5. Add the following bullet points to the **attractions\_planner** agent's existing `instruction`:

   ```
   - When they reply, use your tool to save their selected attraction
   and then provide more possible attractions.
   - If they ask to view the list, provide a bulleted list of
   { attractions? } and then suggest some more.
   ```

   **Copied!**
6. Notice the section in curly braces: `{ attractions? }`. This ADK feature, [key templating](https://google.github.io/adk-docs/sessions/state/#using-key-templating), loads the value of the `attractions` key from the state dictionary. The question mark after the `attractions` key prevents this from erroring if the field is not yet present.
7. You will now run the agent from the web interface, which provides a tab for you to see the changes being made to the session state. **Launch the Agent Development Kit Web UI** with the following command:

   ```
   adk web
   ```

   **Copied!**

   **Output**

   ```
   INFO:     Started server process [2434]
   INFO:     Waiting for application startup.
   +-------------------------------------------------------+
   | ADK Web Server started                                |
   |                                                       |
   | For local testing, access at http://localhost:8000.   |
   +-------------------------------------------------------+

   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit) 
   ```
8. To view the web interface in a new tab, click the **http://127.0.0.1:8000** link in the Terminal output.
9. A new browser tab will open with the ADK Dev UI.
10. From the **Select an agent** dropdown on the left, select the **parent\_and\_subagents** agent from the dropdown.
11. Start the conversation with: `hello`
12. After the agent greets you, reply with:

    ```
    I'd like to go to Egypt.
    ```

    **Copied!**

    You should be transferred to the **attractions\_planner** and be provided a list of attractions.
13. Choose an attraction, for example:

    ```
    I'll go to the Sphinx
    ```

    **Copied!**
14. You should receive an acknowledgement in the response, like: *Okay, I've saved The Sphinx to your list. Here are some other attractions...*
15. Click the response tool box (marked with a check mark) to view the event created from the tool's response. Notice that it includes an **actions** field which includes **state\_delta** describing the changes to the state.
16. You should be prompted by the agent to select more attractions. Reply to the agent by **naming one of the options it has presented**.
17. On the left-hand navigation menu, click the "X" to exit the focus on the event you inspected earlier.
18. Now in the sidebar, you should see the list of events and a few tab options. Select the **State** tab. Here you can view the current state, including your **attractions** array with the two values you have requested.
    ![Session State preview in the Web UI](https://cdn.qwiklabs.com/ILEPEgsj0jm36NlN1fZKw06%2BbOgoKvdm2lSOrWfP2GE%3D)
19. Send this message to the agent:

    ```
    What is on my list?
    ```

    **Copied!**
20. It should return your list formatted as a bulleted list according to its `instruction`.
21. When you are finished experimenting with the agent, close the web browser tab and press **CTRL + C** in the Cloud Shell Terminal to stop the server.
    Later in this lab, you will demonstrate how to use state to communicate between agents.

Click **Check my progress** to verify the objective.

Assessment Completed!

Use session state to store and retrieve specific information

Assessment Completed!

Instead of saving small pieces of information, if you would like to store your agent's entire text response in the state dictionary, you can set an `output_key` parameter when you define the agent, and its entire output will be stored in the state dictionary under that field name.## Workflow Agents

Parent to sub-agent transfers are ideal when you have multiple specialist sub-agents, and you want the user to interact with each of them.

However, if you would like agents to act one-after-another without waiting for a turn from the user, you can use **workflow agents**. Some example scenarios when you might use workflow agents include when you would like your agents to:

* **Plan and Execute:** When you want to have one agent prepare a list of items, and then have other agents use that list to perform follow-up tasks, for example writing sections of a document
* **Research and Write:** When you want to have one agent call functions to collect contextual information from Google Search or other data sources, then another agent use that information to produce some output.
* **Draft and Revise:** When you want to have one agent prepare a draft of a document, and then have other agents check the work and iterate on it

To accomplish these kinds of tasks, **workflow agents** have sub-agents and guarantee that each of their sub-agents acts. Agent Development Kit provides three built-in workflow agents and the opportunity to define your own:

* `SequentialAgent`
* `LoopAgent`
* `ParallelAgent`

Throughout the rest of this lab, you will build a multi-agent system that uses multiple LLM agents, workflow agents, and tools to help control the flow of the agent.

Specifically, you will build an agent that will develop a pitch document for a new hit movie: a biographical film based on the life of a historical character. Your sub-agents will handle the research, an iterative writing loop with a screenwriter and a critic, and finally some additional sub-agents will help brainstorm casting ideas and use historical box office data to make some predictions about box office results.

In the end, your multi-agent system will look like this (you can click on the image to see it larger):

![Diagram of a film_concept_team multi-agent system](https://cdn.qwiklabs.com/9o3xwlTjCWnoyd9fEEgInAHYJbCQHiU5JIYIN8rU9KY%3D)

But you will begin with a simpler version.

## Task 4. Begin building a multi-agent system with a SequentialAgent

The `SequentialAgent` executes its sub-agents in a linear sequence. Each sub-agent in its `sub_agents` list is run, one after the other, in the order they are defined.

This is ideal for workflows where tasks must be performed in a specific order, and the output of one task serves as the input for the next.

In this task, you will run a `SequentialAgent` to build a first version of your movie pitch-development multi-agent system. The first draft of your agent will be structured like this:

![Film_concept_team multi-agent system step 1](https://cdn.qwiklabs.com/11WKiwk%2FNgK7dk%2F0K6tk%2FkzjH8tx%2BuxeJeS3fncHjDs%3D)

* A **root\_agent** named **greeter** to welcome the user and request a historical character as a movie subject
* A `SequentialAgent` called **film\_concept\_team** will include:
  * A **researcher** to learn more about the requested historical figure from Wikipedia, using a LangChain tool covered in the lab *Empower ADK agents with tools*. An agent can choose to call its tool(s) multiple times in succession, so the researcher can take multiple turns in a row if it determines it needs to do more research.
  * A **screenwriter** to turn the research into a plot outline.
  * A **file\_writer** to title the resulting movie and write the results of the sequence to a file.

1. In the **Cloud Shell Editor**, navigate to the directory **adk\_multiagent\_systems/workflow\_agents**.
2. Click on the **agent.py** file in the **workflow\_agents** directory.
3. Read through this agent definition file. Because sub-agents must be defined before they can be assigned to a parent, to read the file in the order of the conversational flow, you can read the agents from the bottom of the file to the top.
4. You also have a function tool **append\_to\_state**. This function allows agents with the tool the ability to add content to a dictionary value in state. It is particularly useful for agents that might call a tool multiple times or act in multiple passes of a `LoopAgent`, so that each time they act their output is stored.
5. Try out the current version of the agent by launching the web interface from the Cloud Shell Terminal. You will use the `--reload_agents` argument to enable live reloading of agents based on agent changes:

   ```
   cd ~/adk_multiagent_systems
   adk web --reload_agents
   ```

   **Copied!**

   **Note:** If you did not shut down your previous `adk web` session, the default port of 8000 will be blocked, but you can launch the Dev UI with a new port by using `adk web --port 8001`, for example.
6. To view the web interface in a new tab, click the **http://127.0.0.1:8000** link in the Terminal output.
7. A new browser tab will open with the ADK Dev UI.
8. From the **Select an agent** dropdown on the left, select **workflow\_agents**.
9. Start the conversation with: `hello`. It may take a few moments for the agent to respond, but it should request you enter a historical figure to start your film plot generation.
10. When prompted to enter a historical figure, you can enter one of your choice or use one of these examples:

    * `Zhang Zhongjing` - a renowned Chinese physician from the 2nd Century CE.
    * `Ada Lovelace` - an English mathematician and writer known for her work on early computers
    * `Marcus Aurelius` - a Roman emperor known for his philosophical writings.
11. The agent should now call its agents one after the other as it executes the workflow and writes the plot outline file to your **\~/adk\_multiagent\_systems/movie\_pitches** directory. It should inform you when it has written the file to disk.
    If you don't see the agent reporting that it generated a file for you or want to try another character, you can click **+ New Session** in the upper right and try again.
12. View the agent's output in the Cloud Shell Editor. (You may need to use the Cloud Shell Editor's menu to enable View > Word Wrap to see the full text without lots of horizontal scrolling.)
13. In the ADK Dev UI, **click on one of the agent icons (![agent_icon](https://cdn.qwiklabs.com/0qmcUwc%2BaHGB6en11vU3HeZL1%2FsZuhC48PulduLYczg%3D))** representing a turn of conversation to bring up the **event view**.
14. The event view provides a visual representation of the tree of agents and tools used in this session. You may need to scroll in the event panel to see the full plot.

![adk web graph](https://cdn.qwiklabs.com/13FyRaWAhz%2B4P0TGiyaiGmU0IGRoARIfQlYcGasMy4o%3D)

15. In addition to the graph view, you can click on the **Request** tab of the event to see the information this agent received as part of its request, including the conversation history.
16. You can also click on the **Response** tab of the event to see what the agent returned.

**Note:** While this system can produce interesting results, it is not intended to imply that instructions can be so brief or adding examples can be skipped. The system's reliability would benefit greatly from the additional layer of adding more rigorous instructions and examples for each agent.Click **Check my progress** to verify the objective.

Assessment Completed!

Begin building a multi-agent system with a SequentialAgent

Assessment Completed!

## Task 5. Add a LoopAgent for iterative work

The `LoopAgent` executes its sub-agents in a defined sequence and then starts at the beginning of the sequence again without breaking for a user input. It repeats the loop until a number of iterations has been reached or a call to exit the loop has been made by one of its sub-agents (usually by calling a built-in `exit_loop` tool).

This is beneficial for tasks that require continuous refinement, monitoring, or cyclical workflows. Examples include:

* **Iterative Refinement:** Continuously improve a document or plan through repeated agent cycles.
* **Continuous Monitoring:** Periodically check data sources or conditions using a sequence of agents.
* **Debate or Negotiation:** Simulate iterative discussions between agents to reach a better outcome.

You will add a `LoopAgent` to your movie pitch agent to allow multiple rounds of research and iteration while crafting the story. In addition to refining the script, this allows a user to start with a less specific input: instead of suggesting a specific historical figure, they might only know they want a story about an ancient doctor, and a research-and-writing iteration loop will allow the agents to find a good candidate, then work on the story.

![Film_concept_team multi-agent system step 2](https://cdn.qwiklabs.com/gZKbLuj%2BZ6usxUe0wdEiFuOdbkWcOO98DEmL%2Fi8LGco%3D)

Your revised agent will flow like this:

* The **root\_agent** **greeter** will remain the same.
* The **film\_concept\_team** `SequentialAgent` will now consist of:
  * A **writers\_room** `LoopAgent` that will begin the sequence. It will consist of:
    * The **researcher** will be the same as before.
    * The **screenwriter** will be similar to before.
    * A **critic** that will offer critical feedback on the current draft to motivate the next round of research and improvement through the loop.
  * When the loop terminates, it will escalate control of the conversation back to the **film\_concept\_team** `SequentialAgent`, which will then pass control to the next agent in its sequence: the **file\_writer** that will remain as before to give the movie a title and write the results of the sequence to a file.

To make these changes:

1. In the **adk\_multiagent\_systems/workflow\_agents/agent.py** file, add this tool import so that you can provide an agent the ability to exit the loop when desired:

   ```
   from google.adk.tools import exit_loop
   ```

   **Copied!**
2. To determine when to exit the loop, add this **critic** agent to decide when the plot outline is ready. Paste the following new agent into the **agent.py** file under the **# Agents** section header (without overwriting the existing agents). Note that it has the `exit_loop` tool as one of its tools and instructions on when to use it:

   ```
   critic = Agent(
       name="critic",
       model=model_name,
       description="Reviews the outline so that it can be improved.",
       instruction="""
       INSTRUCTIONS:
       Consider these questions about the PLOT_OUTLINE:
       - Does it meet a satisfying three-act cinematic structure?
       - Do the characters' struggles seem engaging?
       - Does it feel grounded in a real time period in history?
       - Does it sufficiently incorporate historical details from the RESEARCH?

       If the PLOT_OUTLINE does a good job with these questions, exit the writing loop with your 'exit_loop' tool.
       If significant improvements can be made, use the 'append_to_state' tool to add your feedback to the field 'CRITICAL_FEEDBACK'.
       Explain your decision and briefly summarize the feedback you have provided.

       PLOT_OUTLINE:
       { PLOT_OUTLINE? }

       RESEARCH:
       { research? }
       """,
       before_model_callback=log_query_to_model,
       after_model_callback=log_model_response,
       tools=[append_to_state, exit_loop]
   )
   ```

   **Copied!**
3. Create a new `LoopAgent` called **writers\_room** that creates the iterative loop of the researcher, screenwriter, and critic. Each pass through the loop will end with a critical review of the work so far, which will prompt improvements for the next round. Paste the following above the existing **film\_concept\_team** `SequentialAgent`.

   ```
   writers_room = LoopAgent(
       name="writers_room",
       description="Iterates through research and writing to improve a movie plot outline.",
       sub_agents=[
           researcher,
           screenwriter,
           critic
       ],
       max_iterations=5,
   )
   ```

   **Copied!**
4. Note that the `LoopAgent` creation includes a parameter for `max_iterations`. This defines how many times the loop will run before it ends. Even if you plan to interrupt the loop via another method, it is a good idea to include a cap on the total number of iterations.
5. Update the **film\_concept\_team** `SequentialAgent` to replace the **researcher** and **screenwriter** with the **writers\_room** `LoopAgent` you just created. The **file\_writer** agent should remain at the end of the sequence. The **film\_concept\_team** should now look like this:

   ```
   film_concept_team = SequentialAgent(
       name="film_concept_team",
       description="Write a film plot outline and save it as a text file.",
       sub_agents=[
           writers_room,
           file_writer
       ],
   )
   ```

   **Copied!**
6. Return to the ADK Dev UI tab and click the **+ New Session** button in the upper right to start a new session.
7. Begin a new conversation with: `hello`
8. When prompted to choose a kind of historical character, choose one that interests you. Some ideas include:

   * `an industrial designer who made products for the masses`
   * `a cartographer (a map maker)`
   * `that guy who made crops yield more food`
9. Once you have chosen a type of character, the agent should work its way through iterations of the loop and finally give the film a title and write the outline to a file.
10. Using the Cloud Shell Editor, review the file generated, which should be saved in the **adk\_multiagent\_systems/movie\_pitches** directory. (Once again, you may need to use the Editor's menu to enable View > Word Wrap to see the full text without lots of horizontal scrolling.)

Click **Check my progress** to verify the objective.

Please add the critic agent and make sure it generates a response in the conversation.

Add a LoopAgent for iterative work

Please add the critic agent and make sure it generates a response in the conversation.

## Task 6. Use a "fan out and gather" pattern for report generation with a ParallelAgent

The `ParallelAgent` enables concurrent execution of its sub-agents. Each sub-agent operates in its own branch, and by default, they do not share conversation history or state directly with each other during parallel execution.

This is valuable for tasks that can be divided into independent sub-tasks that can be processed simultaneously. Using a `ParallelAgent` can significantly reduce the overall execution time for such tasks.

In this lab, you will add some supplemental reports -- some research on potential box office performance and some initial ideas on casting -- to enhance the pitch for your new film.

![Film_concept_team multi-agent system step 3](https://cdn.qwiklabs.com/9o3xwlTjCWnoyd9fEEgInAHYJbCQHiU5JIYIN8rU9KY%3D)

Your revised agent will flow like this:

* The **greeter** will the same.
* The **film\_concept\_team** `SequentialAgent` will now consist of:
  * The **writers\_room** `LoopAgent`, which will remain the same including:
    * The **researcher** agent
    * The **screenwriter** agent
    * The **critic** agent
  * Your new **preproduction\_team** `ParallelAgent` will then act, consisting of:
    * A **box\_office\_researcher** agent to use historical box office data to generate a report on potential box office performance for this film
    * A **casting\_agent** agent to generate some initial ideas on casting based on actors who have starred in similar films
  * The **file\_writer** that will remain as before to write the results of the sequence to a file.

While much of this example demonstrates creative work that would be done by human teams, this workflow represents how a complex chain of tasks can be broken across several sub-agents to produce drafts of complex documents which human team members can then edit and improve upon.

1. Paste the following new agents and `ParallelAgent` into your **workflow\_agents/agent.py** file under the `# Agents` header:

   ```
   box_office_researcher = Agent(
       name="box_office_researcher",
       model=model_name,
       description="Considers the box office potential of this film",
       instruction="""
       PLOT_OUTLINE:
       { PLOT_OUTLINE? }

       INSTRUCTIONS:
       Write a report on the box office potential of a movie like that described in PLOT_OUTLINE based on the reported box office performance of other recent films.
       """,
       output_key="box_office_report"
   )

   casting_agent = Agent(
       name="casting_agent",
       model=model_name,
       description="Generates casting ideas for this film",
       instruction="""
       PLOT_OUTLINE:
       { PLOT_OUTLINE? }

       INSTRUCTIONS:
       Generate ideas for casting for the characters described in PLOT_OUTLINE
       by suggesting actors who have received positive feedback from critics and/or
       fans when they have played similar roles.
       """,
       output_key="casting_report"
   )

   preproduction_team = ParallelAgent(
       name="preproduction_team",
       sub_agents=[
           box_office_researcher,
           casting_agent
       ]
   )
   ```

   **Copied!**
2. Update the existing **film\_concept\_team** agent's **sub\_agents** list to include the `preproduction_team` between the **writers\_room** and **file\_writer**:

   ```
   film_concept_team = SequentialAgent(
       name="film_concept_team",
       description="Write a film plot outline and save it as a text file.",
       sub_agents=[
           writers_room,
           preproduction_team,
           file_writer
       ],
   )
   ```

   **Copied!**
3. Update the **file\_writer**'s **instruction** to:

   ```
   INSTRUCTIONS:
   - Create a marketable, contemporary movie title suggestion for the movie described in the PLOT_OUTLINE. If a title has been suggested in PLOT_OUTLINE, you can use it, or replace it with a better one.
   - Use your 'write_file' tool to create a new txt file with the following arguments:
       - for a filename, use the movie title
       - Write to the 'movie_pitches' directory.
       - For the 'content' to write, include:
           - The PLOT_OUTLINE
           - The BOX_OFFICE_REPORT
           - The CASTING_REPORT

   PLOT_OUTLINE:
   { PLOT_OUTLINE? }

   BOX_OFFICE_REPORT:
   { box_office_report? }

   CASTING_REPORT:
   { casting_report? }
   ```

   **Copied!**
4. **Save** the file.
5. In the ADK Dev UI, click **+ New Session** in the upper right.
6. Enter `hello` to start the conversation.
7. When prompted, enter a new character idea that you are interested in. Some ideas include:

   * `that actress who invented the technology for wifi`
   * `an exciting chef`
   * `key players in the worlds fair exhibitions`
8. When the agent has completed its writing and report-generation, inspect the file it produced in the **adk\_multiagent\_systems/movie\_pitches** directory. If a part of the process fails, click **+ New session** in the upper right and try again.

## Custom workflow agents

When the pre-defined workflow agents of `SequentialAgent`, `LoopAgent`, and `ParallelAgent` are insufficient for your needs, `CustomAgent` provides the flexibility to implement new workflow logic. You can define patterns for flow control, conditional execution, or state management between sub-agents. This is useful for complex workflows, stateful orchestrations, or integrating custom business logic into the framework's orchestration layer.

Creation of a `CustomAgent` is out of the scope of this lab, but it is good to know that it exists if you need it!
