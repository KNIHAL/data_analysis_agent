from crewai import Agent
from llms import cloudllm
from tools import get_pandas_tool, get_repl_tool

def edaExpert():
    return Agent(
        name="EDAExpert",
        role="Expert Data Analysis Agent",
        goal=(
            "Perform exploratory data analysis on the given dataset. "
            "This includes calculating descriptive statistics (mean, median), detecting null values, "
            "and performing group-by operations or aggregations. "
            "Use the tools provided to run code and analyze the data, and return clean, readable answers."
        ),
        backstory=(
            "You are an EDA expert who specializes in analyzing raw data. "
            "You assist analysts and business users by uncovering important patterns, trends, and issues "
            "within datasets using Python and pandas."
        ),
        verbose=True,
        allow_delegation=False,
        llm=cloudllm(),
        tools=[
            get_pandas_tool(),
            get_repl_tool()
        ]
    )
