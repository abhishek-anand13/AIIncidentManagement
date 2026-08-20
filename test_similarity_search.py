from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore

embedding_service = EmbeddingService()

vector_store = VectorStore()

query = "Database connection timeout after deployment"

query_embedding = embedding_service.create_embedding(query)

results = vector_store.search(
    query_embedding=query_embedding,
    top_k=5
)

print("=" * 70)
print("Semantic Search Results")
print("=" * 70)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i in range(len(documents)):

    print(f"\nResult {i+1}")

    print("-" * 60)

    print(f"Distance : {distances[i]:.4f}")

    print(f"Category : {metadatas[i]['category']}")

    print(f"Section : {metadatas[i]['section']}")

    print(f"Source : {metadatas[i]['source']}")

    print("\nContent:")

    print(documents[i])

    print("\n")