from crewai import Task
from agents import chartGenerator

def chartTask(eda_task):
    return Task(
        description=(
            "Generate meaningful charts from the EDA findings. Include histograms, bar plots, scatter plots, or any chart "
            "that can reveal structure or pattern in the data.\n\n"
            "{eda_task}"
        ),
        expected_output="Clean and informative visualizations that highlight trends or anomalies in the data.",
        agent=chartGenerator(),
        depend_on=eda_task
    )
