# Empower ADK agents with tools

experimentLabschedule1 hour 30 minutesuniversal\_currency\_altNo costshow\_chartAdvanced

[](https://partner.skills.google/focuses/711657014/reviews?parent=course_session)

infoThis lab may incorporate AI tools to support your learning.

## GENAI105

## Overview

This lab covers the use of tools with Agent Development Kit agents.

From powerful tools provided by Google, like Google Search and Vertex AI Search, to the rich variety of tools available in the LangChain and CrewAI ecosystems, there are many tools to get started with.

Additionally, creating your own tool from a function only requires writing a good docstring!

This lab assumes you are familiar with the basics of ADK covered in the lab *Get started with Agent Development Kit (ADK)*.

## Objective

In this lab, you will learn about the ecosystem of tools available to ADK agents. You will also learn how to provide a function to an agent as a custom tool.

After this lab, you will be able to:

* Provide prebuilt Google, LangChain, or CrewAI tools to an agent
* Discuss the importance of structured docstrings and typing when writing functions for agent tools
* Write your own tool functions for an agent

## Setup and requirements

Tool use with the Agent Developer Kit

Leveraging tools effectively is what truly distinguishes intelligent agents from basic models. A **tool** is a block of code, like a function or a method, that executes specific actions such as interacting with databases, making API requests, or invoking other external services.

Tools empower agents to interact with other systems and perform actions beyond their core reasoning and generation capabilities. It's crucial to note that these tools operate independently of the agent's LLM, meaning that tools do not automatically possess their own reasoning abilities.

Agent Development Kit provides developers with a diverse range of tool options:

* **Pre-built Tools**: Ready-to-use functionalities such as Google Search, Code Execution, and Retrieval-Augmented Generation (RAG) tools.
* **Third-Party Tools**: Seamless integration of tools from external libraries like LangChain and CrewAI.
* **Custom Tools**: The ability to create custom tools tailored to specific requirements, by using language specific constructs and Agents-as-Tools. The SDK also provides asynchronous capabilities through Long Running Function Tools.

In this lab, you will explore these categories and implement one of each type.

## Available Pre-Built Tools from Google

Google provides several useful tools for your agents. They include:

**Google Search** (`google_search`): Allows the agent to perform web searches using Google Search. You simply add `google_search` to the agent's tools.

**Code Execution** (`built_in_code_execution`): This tool allows the agent to execute code, to perform calculations, data manipulation, or interact with other systems programmatically. You can use the pre-built `VertexCodeInterpreter` or any code executor that implements the `BaseCodeExecutor` interface.

**Retrieval** (`retrieval`): A package of tools designed to fetch information from various sources.

**Vertex AI Search Tool** (`VertexAiSearchTool`): This tool integrates with Google Cloud's Vertex AI Search service to allow the agent to search through your AI Applications data stores.

## Task 1. Install ADK and set up your environment

**Note:** Using an Incognito browser window is recommended for most Qwiklabs to avoid confusion between your Qwiklabs student account and other accounts logged into Google Cloud. If you are using Chrome, the easiest way to accomplish this is to close any Incognito windows, then right click on the \*\*Open Google Cloud console\*\* button at the top of this lab and select \*\*Open link in Incognito window\*\*.### Enable Vertex AI recommended APIs

1. In this lab environment, the **Vertex AI API has been enabled for you**. If you were to follow these steps in your own project, you could enable it by navigating to Vertex AI and following the prompt to enable it.

### Prepare a Cloud Shell Editor tab

2. With your Google Cloud console window selected, open Cloud Shell by pressing the **G** key and then the **S** key on your keyboard. Alternatively, you can click the Activate Cloud Shell button (![Activate Cloud Shell](https://cdn.qwiklabs.com/0R1bagVsqDIuRxFoBFZDlx4p2FrWrR8pyIX90XlMIMo%3D)) in the upper right of the Cloud console.
3. Click **Continue**.
4. When prompted to authorize Cloud Shell, click **Authorize**.
5. In the upper right corner of the Cloud Shell Terminal panel, click the **Open in new window** button ![Open in new window button](https://cdn.qwiklabs.com/g4I7jXdmqqSAUtXFvEv%2BUVPf%2FJ7v3AbMmd4cSeruvGI%3D).
6. In the Cloud Shell Terminal, enter the following to open the Cloud Shell Editor to your home directory:

   ```
   cloudshell workspace ~
   ```

   **Copied!**
7. Close any additional tutorial or Gemini panels that appear on the right side of the screen to save more of your window for your code editor.
8. Throughout the rest of this lab, you can work in this window as your IDE with the Cloud Shell Editor and Cloud Shell Terminal.

### Download and install ADK and code samples for this lab

9. Paste the following commands into the Cloud Shell Terminal to download code for this lab from a Cloud Storage bucket:

   ```
   gcloud storage cp -r gs://YOUR_GCP_PROJECT_ID-bucket/adk_tools .
   ```

   **Copied!**
10. Update your `PATH` environment variable, **install ADK**, and install some additional requirements for this lab by running the following commands in the Cloud Shell Terminal.

    ```
    export PATH=$PATH:"/home/${USER}/.local/bin"
    python3 -m pip install google-adk[extensions] -r adk_tools/requirements.txt
    ```

    **Copied!**

    **Note:** `google-adk[extensions]` is used to install additional dependencies required for Crew AI tools.

## Task 2. Create a search app that will be used to ground responses on your own data

In a later task, **you will use the Google-provided Vertex AI Search tool to ground responses on your own data in an AI Applications data store**. Since the app's data store needs a little while to ingest data, you will set it up now, then use it to ground responses on your data in a later task.

1. In your browser tab still showing the Cloud Console, navigate to **AI Applications** by searching for it at the top of the console.
2. Select the terms and conditions checkbox and click **Continue and activate the API**.
3. From the left-hand navigation menu, select **Data Stores**.
4. Select **Create data store**.
5. Find the **Cloud Storage** card and click **Select** on it.
6. Select **Unstructured documents (PDF, HTML, TXT and more)**
7. Example documents have been uploaded to Cloud Storage for you. They relate to the fictional discovery of a new planet named Persephone. A fictional planet is used in this case so that the model cannot have learned anything about this planet during its training.
   For a GCS path, enter `<ql-variable key="project_0.project_id" placeholder="YOUR_GCP_PROJECT_ID"><code class=" default highlight ">YOUR_GCP_PROJECT_ID</code></ql-variable>-bucket/planet-search-docs`.
8. Click **Continue**.
9. Keep the **location** set to **global**.
10. For a **data store name**, enter: `Planet Search`
11. Click **Create**.
12. Click **Apps** on the left-hand nav.
13. Click **Create a new app**.
14. Find the card for a **Custom search (general)** app and click **Create**.
15. **Name** the app `Planet Search`
16. Provide a **Company name** of `Planet Conferences`
17. Click **Continue**.
18. Select the checkbox next to the **Planet Search** data store.
19. Select **Create**.
20. Once your app is created, **click the AI Applications logo** in the upper left to return to your app dashboard.
21. **Copy the ID** value of your app displayed in the Apps table. Save it in a text document as you will need it later.
    For now, you will give the data store some time to ingest its data. Later you will provide your search app to an agent to ground its responses.

Click **Check my progress** to verify the objective.

Create a data store and search app.

## Third-Party Tools

ADK allows you to use tools available from third-party AI libraries like LangChain and CrewAI.

## Task 3. Use a LangChain Tool

The LangChain community has created a [large number of tool integrations](https://python.langchain.com/docs/integrations/tools/) to access many sources of data, integrate with various web products, and accomplish many things. Using community tools within ADK can save you rewriting a tool that someone has already created.

1. Back in your browser tab displaying the Cloud Shell Editor, use the file explorer on the left-hand side to navigate to the directory **adk\_tools/langchain\_tool\_agent**.
2. Write a **.env** file to provide authentication details for this agent directory by running the following in the Cloud Shell Terminal:

   ```
   cd ~/adk_tools
   cat << EOF > langchain_tool_agent/.env
   GOOGLE_GENAI_USE_VERTEXAI=TRUE
   GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
   GOOGLE_CLOUD_LOCATION=GCP_LOCATION
   MODEL=gemini-2.5-flash
   EOF
   ```

   **Copied!**
3. Copy the `.env` file to the other agent directories you will use in this lab by running the following:

   ```
   cp langchain_tool_agent/.env crewai_tool_agent/.env
   cp langchain_tool_agent/.env function_tool_agent/.env
   cp langchain_tool_agent/.env vertexai_search_tool_agent/.env
   ```

   **Copied!**
4. Click on the **agent.py** file in the **langchain\_tool\_agent** directory.
5. Notice the import of the `LangchainTool` class. This is a wrapper class that allows you to use LangChain tools within Agent Development Kit.
6. **Add the following code** where indicated in the `agent.py` file to add the [LangChain Wikipedia tool](https://python.langchain.com/docs/integrations/tools/wikipedia/) to your agent. This will allow your agent to search for information on [Wikipedia](https://www.wikipedia.org/):

   ```
       tools = [
           # Use the LangchainTool wrapper...
           LangchainTool(
               # to pass in a LangChain tool.
               # In this case, the WikipediaQueryRun tool,
               # which requires the WikipediaAPIWrapper as
               # part of the tool.
               tool=WikipediaQueryRun(
                 api_wrapper=WikipediaAPIWrapper()
               )
           )
       ]
   ```

   **Copied!**
7. In the Cloud Shell Terminal, from the **adk\_tools** project directory, **launch the Agent Development Kit Dev UI** with the following commands:

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
10. From the **Select an agent** dropdown on the left, select the **langchain\_tool\_agent** from the dropdown.
11. Query the agent with:

    ```
    Who was Grace Hopper?
    ```

    **Copied!**

    **Output:**

    ![Langchain Wikipedia Tool](https://cdn.qwiklabs.com/EGBnHPzbBor8%2B2uEPGcM5WGimGUG5mkdoukR26MecHw%3D)
12. Click the agent icon (![agent_icon](https://cdn.qwiklabs.com/0qmcUwc%2BaHGB6en11vU3HeZL1%2FsZuhC48PulduLYczg%3D)) next to the agent's chat bubble indicating the use of the **wikipedia** tool.
13. Notice that the content includes a `functionCall` with the query to Wikipedia.
14. At the top of the tab, click the **forward button** to move to the next event.
15. Exploring this event, you can see the result retrieved from Wikipedia used to generate the model's response.
16. When you are finished asking questions of this agent, close the dev UI browser tab.
17. Select the Cloud Shell Terminal panel and press **CTRL + C** to stop the server.

Click **Check my progress** to verify the objective.

Use a LangChain Tool.

## Task 4. Use a CrewAI Tool

You can similarly use [CrewAI Tools](https://github.com/crewAIInc/crewAI-tools), using a `CrewaiTool` wrapper.

1. To do so, using the Cloud Shell Editor file explorer, navigate to the directory **adk\_tools/crewai\_tool\_agent**.
2. Click on the **agent.py** file in the **crewai\_tool\_agent** directory.
3. Notice the import of the `CrewaiTool` class from ADK and the `ScrapeWebsiteTool` from `crewai_tools`.
4. Add the following code where indicated in the `agent.py` file to add the [CrewAI Scrape Website tool](https://docs.crewai.com/en/tools/web-scraping/scrapewebsitetool) to your agent, along with a name and description:

   ```
       tools = [
           CrewaiTool(
               name="scrape_apnews",
               description=(
                   """Scrapes the latest news content from
                   the Associated Press (AP) News website."""
               ),
               tool=ScrapeWebsiteTool(website_url='https://apnews.com/')
           )
       ]
   ```

   **Copied!**

   The `ScrapeWebsiteTool` will load content from the Associated Press news website [apnews.com](https://apnews.com/).
5. You'll run this agent using the command line interface to be familiar with it as a convenient way to test an agent quickly. In the Cloud Shell Terminal, from the **adk\_tools** project directory, launch the agent with the ADK command line UI with:

   ```
   adk run crewai_tool_agent
   ```

   **Copied!**
6. While the agent loads, it may display some warnings. You can ignore these. When you are presented the `user:` prompt, enter:

   ```
   Get 10 of the latest headlines from AP News.
   ```

   **Copied!**

   **Output:**

   ```
   Using Tool: Read website content
   [crewai_tool_agent]: Here are the latest headlines from AP News:
   ...
   ```
7. Notice that the command line interface also indicates to you when a tool is being used.
8. In the Terminal, respond to the next `user:` prompt with `exit` **to exit the command line interface**.
9. Scroll back in your Terminal history to find where you ran `adk run crewai_tool_agent`, and notice that the command line interface provided you a log file to tail. Copy and run that command to view more details of the execution:

   ```
   tail -F /tmp/agents_log/agent.latest.log
   ```

   **Copied!**
10. Press **CTRL + C** to stop tailing the log file and return to the command prompt.

Click **Check my progress** to verify the objective.

Use a CrewAI Tool.

## Task 5. Use a function as a custom tool

When pre-built tools don't fully meet specific requirements, you can create your own tools. This allows for tailored functionality, such as connecting to proprietary databases or implementing unique algorithms.

The most straightforward way to create a new tool is to write a standard Python function with a [docstring written in a standard format](https://google.github.io/adk-docs/tools/function-tools/#docstring) and pass it to your model as a tool. This approach offers flexibility and quick integration.

When writing a function to be used as a tool, there are a few important things to keep in mind:

* **Parameters:** Your function can accept any number of parameters, each of which can be of any JSON-serializable type (e.g., string, integer, list, dictionary). It's important to avoid setting default values for parameters, as the large language model (LLM) does not currently support interpreting them.
* **Return type:** The preferred return type for a Python Function Tool is a dictionary. This allows you to structure the response with key-value pairs, providing context and clarity to the LLM. For example, instead of returning a numeric error code, return a dictionary with an `"error_message"` key containing a human-readable explanation. As a best practice, include a `"status"` key in your return dictionary to indicate the overall outcome (e.g., `"success"`, `"error"`, `"pending"`), providing the LLM with a clear signal about the operation's state.
* **Docstring:** The docstring of your function serves as the tool's description and is sent to the LLM. Therefore, a well-written and comprehensive docstring is crucial for the LLM to understand how to use the tool effectively. Clearly explain the purpose of the function, the meaning of its parameters, and the expected return values.

Define a function and use it as a tool by completing the following steps:

1. Using the Cloud Shell Editor file explorer, navigate to the directory **adk\_tools/function\_tool\_agent**.
2. In the **function\_tool\_agent** directory, click on the **agent.py** file.
3. Notice that the functions `get_date()` and `write_journal_entry()` have docstrings formatted properly for an ADK agent to know when and how to use them. They include:

   * A clear description of what each function does
   * an `Args:` section describing the function's input parameters with JSON-serializable types
   * a `Returns:` section describing what the function returns, with the preferred response type of a `dict`
4. To pass the function to your agent to use as a tool, add the following code where indicated in the `agent.py` file:

   ```
       tools=[get_date, write_journal_entry]
   ```

   **Copied!**
5. You will run this agent using the dev UI to see how its tools allow you to easily visualize tool requests and responses. In the Cloud Shell Terminal, from the **adk\_tools** project directory, run the dev UI again with the following command (if the server is still running from before, stop the running server first with **CTRL+C**, then run the following to start it again):

   ```
   adk web
   ```

   **Copied!**
6. Click the **http://127.0.0.1:8000** link in the Terminal output.
7. A new browser tab will open with the ADK Dev UI.
8. From the **Select an agent** dropdown on the left, select the **function\_tool\_agent**.
9. Start a conversation with the agent with:

   ```
   hello
   ```

   **Copied!**
10. The agent should prompt you about your day. **Respond with a sentence about how your day is going** (like `It's been a good day. I did a cool ADK lab.`) and it will write a journal entry for you.
    **Example Output:**
    ![Journaling Tool Function](https://cdn.qwiklabs.com/M4AR%2BOHlB0enhYBCd4d1nLhObCJ2eKnJlKQCfp2eZ4g%3D)
11. Notice that your agent shows buttons for your custom tool's request and the response. You can click on each to see more information about each of these events.
12. Close the dev UI tab.
13. In the Cloud Shell Editor, you can find your dated journal entry file in the **adk\_tools** directory. (You may want to use the Cloud Shell Editor's menu to enable View > Word Wrap to see the full text without lots of horizontal scrolling.)
14. Stop the server, by clicking on the Cloud Shell Terminal panel and pressing **CTRL + C**.

    #### Best practices for writing functions to be used as tools include


    * **Fewer Parameters are Better:** Minimize the number of parameters to reduce complexity.
    * **Use Simple Data Types:** Favor primitive data types like `str` and `int` over custom classes when possible.
    * **Use Meaningful Names:** The function's name and parameter names significantly influence how the LLM interprets and utilizes the tool. Choose names that clearly reflect the function's purpose and the meaning of its inputs.
    * **Break Down Complex Functions:** Instead of a single `update_profile(profile: Profile)` function, create separate functions like `update_name(name: str)`, `update_age(age: int)`, etc.
    * **Return status:** Include a `"status"` key in your return dictionary to indicate the overall outcome (e.g., `"success"`, `"error"`, `"pending"`) to provide the LLM a clear signal about the operation's state.

Click **Check my progress** to verify the objective.

Use a function as a custom tool.

## Task 6. Use Vertex AI Search as a tool to ground on your own data

In this task, you will discover how easy it is to deploy a RAG application using an Agent Development Kit agent with the built-in Vertex AI Search tool from Google and the AI Applications data store you created earlier.

1. Return to your **Cloud Shell Editor** tab and select the **adk\_tools/vertexai\_search\_tool\_agent** directory.
2. Click on the **agent.py** file in the **vertexai\_search\_tool\_agent** directory.
3. Add an import of the `VertexAiSearchTool` class where indicated at the bottom of the imports:

   ```
   from google.adk.tools import VertexAiSearchTool
   ```

   **Copied!**
4. Update the code where the `VertexAiSearchTool` is instantiated. In the path being passed to `search_engine_id`, update `YOUR_PROJECT_ID` to `YOUR_GCP_PROJECT_ID` and update `YOUR_SEARCH_APP_ID` to the search app ID you copied in the earlier task.
5. Add the following line where indicated in the agent definition to provide the agent the tool:

   ```
       tools=[vertexai_search_tool]
   ```

   **Copied!**

   You can confirm your data store is ready for use by selecting the data store's name on the **AI Applications > Data Stores** page in the console.

   The **Activity** and **Documents** tabs provide statuses on the import and indexing of your documents. When the **Activity** tab reports "Import completed", your data store should be ready to query.
6. In the Cloud Shell Terminal, from the **adk\_tools** project directory, **launch the command line interface** with the following command. You'll include the `--reload_agents` flag so that the Dev UI reloads your agent when you make changes.

   ```
   adk web --reload_agents
   ```

   **Copied!**

   **Note:** If you did not shut down your previous `adk web` session, select the Cloud Shell Terminal panel where it is running and press **CTRL + C**. If you can't find the Cloud Shell Terminal tab you used before, the default port of 8000 will be blocked, but you can launch the Dev UI with a new port by using `adk web --port 8001`.
7. Click the **http://127.0.0.1:8000** to open the ADK Dev UI.
8. From the **Select an agent** dropdown on the left, select the **vertexai\_search\_tool\_agent**.
9. Query the agent about the fictional planet described in your Cloud Storage documents with:

   ```
   Is the new planet Persephone suitable for habitation?
   ```

   **Copied!**

   **Example output (yours may be a little different)**

   ```
   Based on the "Persephone Survey: What we Know So Far" document, Persephone exhibits several characteristics that suggest it could be habitable:

   - Location: It orbits within the habitable zone of its star.
   - Temperature: The average surface temperature is estimated to be around 18°C (64°F).
   ...
   ```

### Using AgentTool to integrate search tools with other tools

Search tools come with an implementation limitation in that you cannot mix search tools and non-search tools in the same agent. To get around this, you can wrap an agent with a search tool with an AgentTool, and then use that agent-as-a-tool to conduct searches alongside other tools.

To see that in action:

10. Ensure you have the **adk\_tools/vertexai\_search\_tool\_agent/agent.py** file open.
11. Update the root\_agent's `tools` parameter to include the `get_date` function tool:

    ```
        tools=[vertexai_search_tool, get_date]
    ```

    **Copied!**
12. In the ADK Dev UI, ask the agent:

    ```
    What is today's date?
    ```

    **Copied!**

    **Expected output:**

    ![Error showing message that multiple tools are supported when all are search tools.](https://cdn.qwiklabs.com/c288d6l8RS55NVTrnJhLhnQhXZayOFt%2BlLH04fJkg7g%3D)
13. Back in the **adk\_tools/vertexai\_search\_tool\_agent/agent.py** file, paste the following code above your root\_agent. This agent is dedicated to using the search tool and contains both the search tool and instructions to use it:

    ```
    vertexai_search_agent = Agent(
        name="vertexai_search_agent",
        model=os.getenv("MODEL"),
        instruction="Use your search tool to look up facts.",
        tools=[vertexai_search_tool]
    )
    ```

    **Copied!**
14. Then replace the **root\_agent's** tools parameter with the following to wrap the agent created in the previous step with the `AgentTool()` :

    ```
        tools=[
            AgentTool(vertexai_search_agent, skip_summarization=False),
            get_date
        ]
    ```

    **Copied!**
15. Now you can query your agent and receive both search results and use the `get_date()` function.
    Back in the ADK Dev UI browser tab, click **+ New Session**.
16. Ask again:

    ```
    What is today's date?
    ```

    **Copied!**

    The agent should respond with the correct date.
17. Then to invoke the search tool, ask:

    ```
    When is the PlanetCon conference?
    ```

    **Copied!**

    Expected output:

    ```
    The PlanetCon: Persephone conference is scheduled for October 26th - 28th, 2028.
    ```
18. Feel free to ask the agent more questions about this new planet and the conference where its discovery will be announced. When you are satisfied, close the dev UI tab.
19. When you are finished asking questions of this agent, close the browser tab, select the Cloud Shell Terminal window where the server is running, and press **CTRL + C** to stop the server.

Click **Check my progress** to verify the objective.

Use a Google-provided tool.

## Even More Types of Tools!

The following tool types are good for you to know about, but you will not implement them in this lab.

### The LongRunningFunctionTool Class

This tool is a subclass of FunctionTool. It's designed for tasks that require a significant amount of processing time that should be called without blocking the agent's execution.

When using a `LongRunningFunctionTool`, your Python function can initiate the long-running operation and optionally return an intermediate result to keep the model and user informed about the progress (e.g., status updates or estimated completion time). The agent can then continue with other tasks.

An example is a human-in-the-loop scenario where the agent needs human approval before proceeding with a task.

### Application Integration workflows as tools

With [Application Integration](https://cloud.google.com/application-integration/docs/overview), you can use a drag-and-drop interface in the Google Cloud Console to build tools, data connections, and data transformations using Integration Connector’s 100+ pre-built connectors for Google Cloud products and third-party systems like Salesforce, ServiceNow, JIRA, SAP, and more. You can then use an ADK `ApplicationIntegrationToolset` to [allow your agents to connect to those sources or call your workflows](https://google.github.io/adk-docs/tools/google-cloud-tools/#application-integration-tools).

### Model Context Protocol (MCP) Tools

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open standard designed to standardize how Large Language Models (LLMs) like Gemini and Claude communicate with external applications, data sources, and tools. ADK helps you both use and consume MCP tools in your agents, whether you're trying to build a tool to call an MCP service, or exposing an MCP server for other developers or agents to interact with your tools.

Refer to the [MCP Tools documentation](https://google.github.io/adk-docs/tools/mcp-tools/) for code samples and design patterns that help you use ADK together with MCP servers, including:

* **Using Existing MCP Servers within ADK:** An ADK agent can act as an MCP client and use tools provided by external MCP servers.
* **Exposing ADK Tools via an MCP Server:** How to build an MCP server that wraps ADK tools, making them accessible to any MCP client.

For more information on using MCP with ADK agents, see the lab [Use Model Context Protocol (MCP) Tools with ADK Agents](https://partner.skills.google/catalog_lab/32353).

## Congratulations!

In this lab, you’ve learned to:

* Provide prebuilt Google, LangChain, or CrewAI tools to an agent
* Write your own tool functions for an agent
* Discuss the importance of structured docstrings and typing when writing functions for agent tools

## Next Steps

To learn more about building and deploying agents using Agent Development Kit, check out these labs:

* [Build multi-agent systems with ADK](https://partner.cloudskillsboost.google/catalog_lab/32044)
* [Deploy ADK agents to Agent Engine](https://partner.cloudskillsboost.google/catalog_lab/32019)

### Google Cloud training and certification

...helps you make the most of Google Cloud technologies. [Our classes](https://cloud.google.com/training) include technical skills and best practices to help you get up to speed quickly and continue your learning journey. We offer fundamental to advanced level training, with on-demand, live, and virtual options to suit your busy schedule. [Certifications](https://cloud.google.com/certification/) help you validate and prove your skill and expertise in Google Cloud technologies.

**Manual Last Updated November 18, 2025**

**Lab Last Tested November 06, 2025**

Copyright 2023 Google LLC All rights reserved. Google and the Google logo are trademarks of Google LLC. All other company and product names may be trademarks of the respective companies with which they are associated.

[](https://partner.skills.google/paths/3033/course_sessions/33216468/labs/606589)

[](https://partner.skills.google/paths/3033/course_sessions/33216468/quizzes/606591)

# 

# 

# 

[](https://partner.skills.google/focuses/711657014/set_up_lab_forward_url?course_template=1275&parent=course_session)

# 

[](https://partner.skills.google/focuses/711657014/set_up_lab_forward_url?course_template=1275&parent=course_session)

# 

# 

# 

# 

# 

# 

[](https://partner.skills.google/paths/3033/course_templates/1275/preview)
