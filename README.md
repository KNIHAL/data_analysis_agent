# 📊 Data Analysis Agent (powered by CrewAI)

This project is an intelligent data analysis pipeline built using [CrewAI](https://github.com/joaomdmoura/crewai). It allows you to upload a CSV file, ask natural language questions about the data, and receive a fully generated report including EDA, charts, insights, and a markdown summary.

## 🚀 Features

- Load and validate a CSV file
- Run automated EDA using pandas and code execution tools
- Generate meaningful charts (histogram, bar, scatter)
- Extract insights (trends, correlations, anomalies)
- Write a clean markdown report (`report/analysis.md`)
- CLI interface to guide you through the process

## 🧠 Powered By
- [CrewAI](https://github.com/joaomdmoura/crewai)
- [LangChain Tools](https://python.langchain.com/docs/integrations/tools/)
- `click` for CLI
- `dotenv` for environment variable management


## 🛠️ How to Use

1. Install dependencies:
```bash
pip install -r requirements.txt

```
2. Run the CLI:
```bash
python cli.py

```
3. Provide:

Your OpenAI API Key
Path to your CSV
Your question/query about the dataset

4. Check your 'report/analysis.md' for results

### 📝 Example Query
What are the top 5 features impacting customer churn?
### 🛡️ Environment Variables
You'll be prompted to enter your OpenAI API key, which will be saved in a .env file

## 📄 License
See LICENSE file.

## 🤝 Contributing
See CONTRIBUTING.md for contribution guidelines.




