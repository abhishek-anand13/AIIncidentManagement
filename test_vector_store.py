from app.services.vector_store import VectorStore

print("Creating Vector Store...")

vector_store = VectorStore()

print("Collection Name:")
print(vector_store.collection.name)

print("\nEverything is working!")