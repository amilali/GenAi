import nbformat
import sys

def create_code_cell(source):
    return nbformat.v4.new_code_cell(source=source)

try:
    with open('FinanceAnalysis.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Agent 2: Trading Strategy Agent
    trading_strategy_agent_source = """trading_strategy_agent = Agent(
    role="Trading Strategy Developer",
    goal="Develop and test various trading strategies based on insights from the Data Analyst.",
    backstory="Equipped with a deep understanding of financial markets and quantitative analysis, this agent devises and refines trading strategies.",
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)"""

    # Agent 3: Execution Agent
    execution_agent_source = """execution_agent = Agent(
    role="Trade Advisor",
    goal="Suggest optimal trade execution strategies based on approved trading strategies.",
    backstory="This agent specializes in analyzing the timing, price, and logistical details of potential trades.",
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)"""

    # Agent 4: Risk Management Agent
    risk_management_agent_source = """risk_management_agent = Agent(
    role="Risk Advisor",
    goal="Evaluate and provide insights on the risks associated with potential trading activities.",
    backstory="Armed with a deep understanding of risk assessment models and market dynamics, this agent scrutinizes the potential risks of proposed trades.",
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)"""

    # Task 1: Data Analysis Task
    data_analysis_task_source = """data_analysis_task = Task(
    description="Continuously monitor and analyze market data for selected assets.",
    expected_output="Meaningful insights and alerts about significant market movements.",
    agent=data_analyst_agent
)"""

    # Task 2: Strategy Development Task
    strategy_development_task_source = """strategy_development_task = Task(
    description="Develop and refine trading strategies based on the insights from the Data Analyst and user-defined risk tolerance.",
    expected_output="A set of potential trading strategies that align with the user's risk tolerance.",
    agent=trading_strategy_agent
)"""

    # Task 3: Execution Planning Task
    execution_planning_task_source = """execution_planning_task = Task(
    description="Analyze approved trading strategies to determine the best execution methods for individual trades.",
    expected_output="Detailed execution plans suggesting how and when to execute trades.",
    agent=execution_agent
)"""

    # Task 4: Risk Assessment Task
    risk_assessment_task_source = """risk_assessment_task = Task(
    description="Evaluate the risks associated with the proposed trading strategies and execution plans.",
    expected_output="A comprehensive risk analysis report detailing potential risks and mitigation recommendations.",
    agent=risk_management_agent
)"""

    # Crew
    crew_source = """crew = Crew(
    agents=[data_analyst_agent, trading_strategy_agent, execution_agent, risk_management_agent],
    tasks=[data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task],
    verbose=True
)"""

    # Add the cells
    cells_to_add = [
        create_code_cell(trading_strategy_agent_source),
        create_code_cell(execution_agent_source),
        create_code_cell(risk_management_agent_source),
        create_code_cell(data_analysis_task_source),
        create_code_cell(strategy_development_task_source),
        create_code_cell(execution_planning_task_source),
        create_code_cell(risk_assessment_task_source),
        create_code_cell(crew_source)
    ]
    
    nb.cells.extend(cells_to_add)

    with open('FinanceAnalysis.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
        
    print("Successfully updated FinanceAnalysis.ipynb")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
