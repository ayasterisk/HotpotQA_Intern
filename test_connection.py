from neo4j_connection import get_session

session = get_session()

result = session.run("RETURN 'Connected to Neo4j Aura' AS message")

for record in result:
    print(record["message"])

session.close()