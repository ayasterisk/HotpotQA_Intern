from datasets import load_from_disk
from neo4j_connection import get_session

dataset = load_from_disk("hotpot_mini_1k")

session = get_session()

for item in dataset:

    titles = item["context"]["title"]
    sentences_list = item["context"]["sentences"]

    for title, sentences in zip(titles, sentences_list):

        text = " ".join(sentences)

        session.run("""
        CREATE (d:Document {
            title:$title,
            text:$text
        })
        """, title=title, text=text)

session.close()

print("Graph ingestion completed")