# This is the cloud LLM API key config file. USe according to your interest.
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

cloudllm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=os.getenv("OPENAI_API_KEY")
)
