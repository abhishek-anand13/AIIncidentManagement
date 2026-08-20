from app.agents.knowledge_agent import KnowledgeAgent

agent = KnowledgeAgent()

context = agent.retrieve(
    "Database connection timeout after deployment"
)

print("\nKnowledge Found:", context.found)
print("Confidence:", context.confidence)

print("\nRetrieved Chunks:\n")

for chunk in context.retrieved_chunks:

    print("=" * 60)

    print("Category :", chunk.category)
    print("Section  :", chunk.section)
    print("Source   :", chunk.source)
    print("Distance :", f"{chunk.distance:.4f}")

    print("\nContent:\n")

    print(chunk.content)