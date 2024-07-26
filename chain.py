from langchain.prompts import PromptTemplate
import openai_load

llm = openai_load.load_model()

# with chain, example 1
# template = PromptTemplate(template="""
# You are a cockney fruit and vegetable seller.
# Your role is to assist your customer with their fruit and vegetable needs.
# Respond using cockney rhyming slang.

# Tell me about the following fruit: {fruit}
# """, input_variables=["fruit"])

# llm_chain = template | llm

# response = llm_chain.invoke({"fruit": "apple"})

# print(response)

from langchain.schema import StrOutputParser

template = PromptTemplate.from_template("""
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Output JSON as {{"description": "your response here"}}

Tell me about the following fruit: {fruit}
""")

llm_chain = template | llm | StrOutputParser()

response = llm_chain.invoke({"fruit": "apple"})

print(response)


# without chain
# response = llm.invoke(template.format(fruit="apple"))

# print(response)