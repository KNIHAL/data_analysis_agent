from crewai import Crew, Process
from agents import dataLoader, edaExpert, chartGenerator, insightGenerator, reportWriter
from tasks import dataLoaderTask, edaTask, chartTask, insightTask, reportTask

def crew(file_path: str):
    loader_task = dataLoaderTask(file_path)
    eda_task = edaTask(loader_task)
    chart_task = chartTask(eda_task)
    insight_task = insightTask(chart_task)
    report_task = reportTask(insight_task)

    return Crew(
        agents=[
            dataLoader(),
            edaExpert(),
            chartGenerator(),
            insightGenerator(),
            reportWriter()
        ],
        tasks=[
            loader_task,
            eda_task,
            chart_task,
            insight_task,
            report_task
        ],
        process=Process.sequential,
        verbose=False
    )
