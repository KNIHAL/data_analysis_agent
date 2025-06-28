from crewai import Task
from agents import reportWriter

def reportTask(insight_task):
    return Task(
        description=(
            "Write a professional and structured data analysis report using the findings, charts, and insights from all previous steps. "
            "Include a summary, methodology, key findings, visualizations, and conclusions. Format it in markdown.\n\n"
            "{insight_task}"
        ),
        expected_output="A complete report saved to `report/analysis.md`.",
        agent=reportWriter(),
        markdown=True,
        output_file="report/analysis.md",
        depend_on=insight_task
    )
