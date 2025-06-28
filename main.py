import os
from crew import crew
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Ensure report directory exists
os.makedirs("report", exist_ok=True)

def run_analysis_agent(csv_path: str, query: str) -> str:
    """
    Runs the full CrewAI data analysis pipeline and saves the result to a Markdown report.
    """
    result = crew(file_path=csv_path).kickoff(inputs={
        "file_path": csv_path,
        "query": query
    })

    # Save to report/analysis.md
    report_path = "report/analysis.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(result)

    return report_path
