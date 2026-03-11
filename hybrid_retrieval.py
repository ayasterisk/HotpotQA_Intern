from sentence_transformers import SentenceTransformer
from neo4j_connection import get_session

model = SentenceTransformer("all-MiniLM-L6-v2")


def hybrid_retrieve(question, k=5):

    session = get_session()

    # tạo embedding cho câu hỏi
    question_embedding = model.encode(question).tolist()

    query = """
    CALL db.index.vector.queryNodes(
        'document_embedding_index',
        $k,
        $embedding
    )
    YIELD node, score

    OPTIONAL MATCH (node)-[:BRIDGE*1..2]->(neighbor)

    WITH node, score, collect(neighbor) AS neighbors

    RETURN
        node.title AS title,
        node.text AS text,
        score,
        [n IN neighbors | n.text] AS neighbor_texts
    """

    result = session.run(
        query,
        k=k,
        embedding=question_embedding
    )

    documents = []

    for record in result:

        text = record["text"]

        # thêm context từ graph neighbors
        if record["neighbor_texts"]:
            text += " ".join(record["neighbor_texts"])

        documents.append({
            "title": record["title"],
            "text": text,
            "score": record["score"]
        })

    session.close()

    return documents