from crewai import Agent
from llms import cloudllm

def insightGenerator():
    return Agent(
        name="InsightGen",
        role="Insight Generator Agent",
        goal=(
            "Extract deep and meaningful insights from the given data — such as trends, correlations, and anomalies — "
            "to support analytical storytelling."
        ),
        backstory=(
            "You are an expert insight generator with a sharp eye for critical patterns in datasets. "
            "Your job is to interpret statistical outputs and findings from the EDA and chart generation steps, "
            "then turn them into clear insights that can be used in a report or presentation."
        ),
        verbose=True,
        allow_delegation=False,
        llm=cloudllm(),
    )
