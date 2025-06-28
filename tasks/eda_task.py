from crewai import Task
from agents import edaExpert

def edaTask(data_loader_task):
    return Task(
        description=(
            "Perform exploratory data analysis (EDA) on the DataFrame provided. "
            "Use pandas and Python to understand structure, detect missing values, data types, summary stats, and "
            "patterns that are relevant to the user query. Use appropriate tools for exploration.\n\n"
            "{data_loader_task}"
        ),
        expected_output="A detailed summary of EDA findings and statistics in markdown format.",
        agent=edaExpert(),
        depend_on=data_loader_task
    )
