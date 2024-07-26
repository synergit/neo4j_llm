from langchain_openai import OpenAI
import os
from dotenv import load_dotenv


# approach 1
# llm = OpenAI(openai_api_key="")

def load_model():
    load_dotenv()
    # approach 2
    llm = OpenAI(
        openai_api_key=os.getenv('OPENAI_API_KEY'),
        model="gpt-3.5-turbo-instruct",
        temperature=0.5
    )
    return llm