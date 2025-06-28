from crewai import Agent
from crewai_tools import FileWriteTool
from llms import cloudllm

file_tool = FileWriteTool(file_path="reports/analysis_report.md")

def reportWriter():
    return Agent(
        name="Reporter",
        role="Report Writer Agent",
        goal=(
            "Write a report in markdown or HTML format by combining the outputs from the other agents "
            "(EDA Expert, Chart Generator, and Insight Generator)."
        ),
        backstory=(
            "You are a professional report writer with great skills in summarizing data analysis tasks. "
            "You know how to write simple, clean, and easy-to-understand reports by combining the insights, "
            "charts, and analysis from the other agents. Your reports are well-formatted and useful for business or research."
        ),
        verbose=True,
        allow_delegation=False,
        llm=cloudllm(),
        tools=[file_tool]
    )
