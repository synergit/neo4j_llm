from langchain_community.graphs import Neo4jGraph

# test mneo4j connection
graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="pleaseletmein"
)
# result = graph.query("""
# MATCH (m:Movie{title: 'Toy Story'}) 
# RETURN m.title, m.plot, m.poster
# """)

# print(result)
print(graph.schema)

# graph = Neo4jGraph(
#     url="bolt://44.195.69.132:7687",
#     username="neo4j",
#     password="bore-successes-trail"
# )
# graph.refresh_schema()
# print(graph.schema)




