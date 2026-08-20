from app.services.knowledge_loader import KnowledgeLoader

loader = KnowledgeLoader()

documents = loader.load_documents()

print(f"Total Documents: {len(documents)}")

print("\nFirst Document:\n")

print(documents[0].page_content[:500])

print("\nMetadata:\n")

print(documents[0].metadata)