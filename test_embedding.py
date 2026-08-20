from app.services.embedding_service import EmbeddingService

embedding_service = EmbeddingService()

vector = embedding_service.create_embedding(
    "Database connection timeout"
)

print(type(vector))
print(len(vector))
print(vector[:10])