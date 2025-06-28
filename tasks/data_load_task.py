from crewai import Task
from agents import dataLoader

def dataLoaderTask(file_path: str):
    return Task(
        description=(
            f"Verify that the provided file path is correct and the file is a valid data source: `{file_path}`. "
            "Load the file as a pandas DataFrame and confirm successful ingestion."
        ),
        expected_output="A valid pandas DataFrame loaded from the file path.",
        agent=dataLoader()
    )
