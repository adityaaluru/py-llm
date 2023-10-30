from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://c692095c.databases.neo4j.io"
AUTH = ("neo4j", "S9FZesHQALoOcO0hqIj2t-oZHAtu4DLpVY_NwT7CQzo")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()