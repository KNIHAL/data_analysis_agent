# cli.py
import os
import shutil
import click
from main import run_analysis_agent

@click.command()
def cli():
    click.secho("🎉 Welcome to Data Analysis Agent", fg='cyan')

    # Get the API Key from the user
    api_key = click.prompt("🔐 Enter your OpenAI API Key", hide_input=True)

    # Save it to .env file
    if api_key:
        with open(".env", "w") as f:
            f.write(f"OPENAI_API_KEY={api_key}\n")
        click.secho("🔐 API key saved to .env file", fg="green")
    else:
        click.secho("❌ API key is required to continue.", fg="red")
        return

    # Get file path from user
    file_path = click.prompt("📁 Enter path to your CSV file")
    if not os.path.exists("data"):
        os.makedirs("data")

    new_path = os.path.join("data", "uploaded.csv")
    shutil.copy(file_path, new_path)
    click.secho("✅ File copied to data/uploaded.csv", fg="green")

    # Ask user for data analysis query
    query = click.prompt("❓ What question do you want to ask about your data?")

    # Run the agent
    click.secho("🧠 Running analysis... please wait ⏳", fg='yellow')
    report_path = run_analysis_agent(csv_path=new_path, query=query)

    # Final report
    click.secho(f"✅ Report saved to {report_path}", fg='green')
    if click.confirm("📂 Open the report now?"):
        os.system(f"start {report_path}" if os.name == "nt" else f"open {report_path}")

if __name__ == "__main__":
    cli()
