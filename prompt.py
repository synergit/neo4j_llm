from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

# approach 1
# llm = OpenAI(openai_api_key="")

# approach 2
llm = OpenAI(
    openai_api_key=os.getenv('OPENAI_API_KEY'),
    model="gpt-3.5-turbo-instruct",
    temperature=0
)

# 1
# template = PromptTemplate(template="""
# You are a cockney fruit and vegetable seller.
# Your role is to assist your customer with their fruit and vegetable needs.
# Respond using cockney rhyming slang.

# Tell me about the following fruit: {fruit}
# """, input_variables=["fruit"])

# response = llm.invoke(template.format(fruit="apple"))

# 2
# prompt = PromptTemplate.from_template(template="""
# You are a cockney fruit and vegetable seller.
# Your role is to assist your customer with their fruit and vegetable needs.
# Respond using cockney rhyming slang.

# Tell me about the following fruit: {fruit}
# """)
# response = llm.invoke(prompt.format(fruit='banana'))

# 3
prompt = PromptTemplate.from_file('prompt.txt')
response = llm.invoke(prompt.format(fruit='orange'))


print(response)