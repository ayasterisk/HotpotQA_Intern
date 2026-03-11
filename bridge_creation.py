from datasets import load_from_disk
from neo4j_connection import get_session

dataset = load_from_disk("hotpot_mini_1k")

session = get_session()

bridge_count = 0

for item in dataset:

    titles = item["supporting_facts"]["title"]

    # bỏ duplicate trong cùng câu hỏi
    titles = list(dict.fromkeys(titles))

    if len(titles) < 2:
        continue

    for i in range(len(titles) - 1):

        t1 = titles[i]
        t2 = titles[i + 1]

        session.run(
            """
            MATCH (a:Document {title:$t1})
            MATCH (b:Document {title:$t2})
            MERGE (a)-[:BRIDGE]->(b)
            """,
            t1=t1,
            t2=t2
        )

        bridge_count += 1

session.close()

print("Bridge edges created:", bridge_count)