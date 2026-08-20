from app.services.knowledge_loader import KnowledgeLoader

loader = KnowledgeLoader()

chunks = loader.split_documents()

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:10], start=1):

    print("=" * 60)

    print(f"Chunk {i}")

    print(chunk.page_content)

    print(chunk.metadata)