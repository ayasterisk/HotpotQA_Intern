from neo4j_connection import get_session

INDEX_NAME = "document_embedding_index"
DIMENSION = 384


def create_vector_index():
    session = get_session()

    check_query = """
    SHOW INDEXES
    YIELD name
    WHERE name = $index_name
    RETURN name
    """

    result = session.run(check_query, index_name=INDEX_NAME)

    if result.single():
        print(f"Vector index '{INDEX_NAME}' already exists.")
        session.close()
        return

    create_query = f"""
    CREATE VECTOR INDEX {INDEX_NAME}
    FOR (d:Document)
    ON (d.embedding)
    OPTIONS {{
        indexConfig: {{
            `vector.dimensions`: {DIMENSION},
            `vector.similarity_function`: 'cosine'
        }}
    }}
    """

    session.run(create_query)

    session.close()

    print("Vector index created successfully!")


if __name__ == "__main__":
    create_vector_index()