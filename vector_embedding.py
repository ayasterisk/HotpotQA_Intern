from sentence_transformers import SentenceTransformer
from neo4j_connection import get_session

model = SentenceTransformer("all-MiniLM-L6-v2")

session = get_session()

result = session.run("""
MATCH (d:Document)
RETURN elementId(d) AS id, d.text AS text
""")

for record in result:

    embedding = model.encode(record["text"]).tolist()

    session.run("""
    MATCH (d)
    WHERE elementId(d) = $id
    SET d.embedding = $embedding
    """, id=record["id"], embedding=embedding)

session.close()

print("Embedding completed")