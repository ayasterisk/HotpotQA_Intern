from hybrid_retrieval import hybrid_retrieve

question = "Who directed the film Creed?"

docs = hybrid_retrieve(question)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(docs):

    print(f"Document {i+1}")
    print("Title:", doc["title"])
    print("Text:", doc["text"][:200])
    print()