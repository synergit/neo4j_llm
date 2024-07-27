from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage  
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

import openai_load

chat_llm = openai_load.load_model()

# without chain
# instructions = SystemMessage(content="""
# You are a surfer dude, having a conversation about the surf conditions on the beach.
# Respond using surfer slang.
# """)

# instructions = SystemMessage(content="""
# You are a IBM employee dude, having a conversation about promoting IBM products.
# Avoid being wordy.
# """)

# question = HumanMessage(content="what is the best data product?")

# response = chat_llm.invoke([
#     instructions,
#     question
# ])

# print(response)

# with chain, but no context
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a surfer dude, having a conversation about the surf conditions on the beach. Respond using surfer slang.",
#         ),
#         (
#             "human", 
#             "{question}"
#         ),
#     ]
# )

# chat_chain = prompt | chat_llm | StrOutputParser()

# response = chat_chain.invoke({"question": "What is the weather like?"})

# print(response)

# with chain and context
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a surfer dude, having a conversation about the surf conditions on the beach. Respond using surfer slang.",
#         ),
#         ( "system", "{context}" ),
#         ( "human", "{question}" ),
#     ]
# )

# chat_chain = prompt | chat_llm | StrOutputParser()

current_weather = """
    {
        "surf": [
            {"beach": "Fistral", "conditions": "6ft waves and offshore winds"},
            {"beach": "Polzeath", "conditions": "Flat and calm"},
            {"beach": "Watergate Bay", "conditions": "3ft waves and onshore winds"}
        ]
    }"""

# response = chat_chain.invoke(
#     {
#         "context": current_weather,
#         "question": "What is the weather like on Watergate Bay?",
#     }
# )

# print(response)


# with chain, context and memory
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a surfer dude, having a conversation about the surf conditions on the beach. Respond using surfer slang.",
        ),
        ("system", "{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

memory = ChatMessageHistory()

def get_memory(session_id):
    return memory

chat_chain = prompt | chat_llm | StrOutputParser()

chat_with_message_history = RunnableWithMessageHistory(
    chat_chain,
    get_memory,
    input_messages_key="question",
    history_messages_key="chat_history",
)
print('<----- memory')
print(f'{memory}')
print('----->')
print()
response = chat_with_message_history.invoke(
    {
        "context": current_weather,
        "question": "Hi, I am at Watergate Bay, what is the surf like?"
    },
    config={"configurable": {"session_id": "none"}}
)
print(f'response:{response}')
print('<----- memory')
print(f'{memory}')
print('----->')
print()

response = chat_with_message_history.invoke(
    {
        "context": current_weather,
        "question": "Where I am?"
    },
    config={"configurable": {"session_id": "none"}}
)

print(f'response:{response}')
print('<----- memory')
print(f'{memory}')
print('----->/n')