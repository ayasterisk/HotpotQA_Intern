from datasets import load_from_disk
from neo4j import GraphDatabase
from config import (
    NEO4J_URI,
    NEO4J_USERNAME,
    NEO4J_PASSWORD,
    NEO4J_DATABASE,
    DATA_PATH
)

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)


def upgrade_bridge():

    dataset = load_from_disk(DATA_PATH)

    with driver.session(database=NEO4J_DATABASE) as session:

        for row in dataset:

            titles = row["supporting_facts"]["title"]

            if len(titles) < 2:
                continue

            for i in range(len(titles) - 1):

                doc1 = titles[i]
                doc2 = titles[i + 1]

                session.run(
                    """
                    MATCH (d1:Document {title:$doc1})
                    MATCH (d2:Document {title:$doc2})
                    MATCH (d1)-[b:BRIDGE]->(d2)

                    SET b.qid = $qid
                    SET b.question = $question
                    SET b.type = $type
                    SET b.dataset = "hotpotqa"
                    """,
                    doc1=doc1,
                    doc2=doc2,
                    qid=row["id"],
                    question=row["question"],
                    type=row["type"],
                )

    print("Bridge upgrade completed")


if __name__ == "__main__":
    upgrade_bridge()