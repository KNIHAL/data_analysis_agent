from crewai import Task
from agents import insightGenerator

def insightTask(chart_task):
    return Task(
        description=(
            "Analyze the visualizations and EDA output to extract meaningful insights. "
            "Focus on trends, correlations, or unusual observations that may have analytical significance.\n\n"
            "{chart_task}"
        ),
        expected_output="A list of well-explained insights based on the data and visualizations.",
        agent=insightGenerator(),
        depend_on=chart_task
    )
