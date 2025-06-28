from crewai import Agent
from llms import cloudllm

def dataLoader():
    return Agent(
        name="DataLoader",
        role="Data Loader Agent",
        goal=(
            "Load and validate the uploaded CSV file. "
            "Ensure the file path is correct and the file exists. "
            "Prepare it for the next phase of data analysis."
        ),
        backstory=(
            "You are responsible for receiving data from the user, validating the file path, "
            "ensuring the data is loadable, and passing it forward to the EDA Expert agent "
            "for further analysis."
        ),
        verbose=True,
        allow_delegation=False,
        llm=cloudllm()
    )
