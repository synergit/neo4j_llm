from langchain_openai import OpenAIEmbeddings
from langchain_community.graphs import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector
from langchain.schema import Document
from langchain.chains import RetrievalQA

import os
from dotenv import load_dotenv
import openai_load

load_dotenv()

llm = openai_load.load_model()

embedding_provider = OpenAIEmbeddings(
    openai_api_key=os.getenv('OPENAI_API_KEY'),
)

graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="pleaseletmein"
)

# A list of Documents
# documents = [
#     Document(
#         page_content="chloe wang has been working at IBM for 8 years",
#         metadata={"source": "local"}
#     )
# ]

# new_vector = Neo4jVector.from_documents(
#     documents,
#     embedding_provider,
#     graph=graph,
#     index_name="moviePlots",
#     node_label="Chunk",
#     text_node_property="text",
#     embedding_node_property="embedding",
#     create_id_index=True,
# )

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    graph=graph,
    index_name="moviePlots",
    embedding_node_property="plotEmbedding",
    text_node_property="plot",
)

print(movie_plot_vector)

# print(graph.schema)

result = movie_plot_vector.similarity_search("A movie where aliens land and attack earth.")
for doc in result:
    print(doc.metadata["title"], "-", doc.page_content)