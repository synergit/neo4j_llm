from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from uuid import uuid4
from langchain_community.graphs import Neo4jGraph
from langchain_community.chat_message_histories import Neo4jChatMessageHistory

import openai_load

chat_llm = openai_load.load_model()

SESSION_ID = str(uuid4())
print(f"Session ID: {SESSION_ID}")

# graph = Neo4jGraph(
#     url="bolt://localhost:7687",
#     username="neo4j",
#     password="pleaseletmein"
# )
graph = Neo4jGraph(
    url="bolt://44.195.69.132:7687",
    username="neo4j",
    password="bore-successes-trail"
)
print(graph.schema)


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
    return Neo4jChatMessageHistory(session_id=session_id, graph=graph)


chat_chain = prompt | chat_llm | StrOutputParser()

chat_with_message_history = RunnableWithMessageHistory(
    chat_chain,
    get_memory,
    input_messages_key="question",
    history_messages_key="chat_history",
)


current_weather = """
    {
        "surf": [
            {"beach": "Fistral", "conditions": "6ft waves and offshore winds"},
            {"beach": "Bells", "conditions": "Flat and calm"},
            {"beach": "Watergate Bay", "conditions": "3ft waves and onshore winds"}
        ]
    }"""

while True:
    question = input("> ")

    response = chat_with_message_history.invoke(
        {
            "context": current_weather,
            "question": question,
            
        }, 
        config={
            "configurable": {"session_id": SESSION_ID}
        }
    )
    
    print(response)