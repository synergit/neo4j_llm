from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage  
import openai_load

chat_llm = openai_load.load_model()

# instructions = SystemMessage(content="""
# You are a surfer dude, having a conversation about the surf conditions on the beach.
# Respond using surfer slang.
# """)

instructions = SystemMessage(content="""
You are a IBM employee dude, having a conversation about promoting IBM products.
Avoid being wordy.
""")

question = HumanMessage(content="what is the best AI product?")

response = chat_llm.invoke([
    instructions,
    question
])

print(response)