from app.services.vector_store import VectorStore

print("=" * 70)
print("Testing ChromaDB")
print("=" * 70)

vector_store = VectorStore()

# Get everything stored in the collection
results = vector_store.collection.get()

documents = results["documents"]
metadatas = results["metadatas"]
ids = results["ids"]

print(f"\nTotal Indexed Chunks : {len(ids)}")

print("\nFirst Stored Chunk")
print("-" * 70)

print("Document ID:")
print(ids[0])

print("\nDocument:")
print(documents[0])

print("\nMetadata:")
print(metadatas[0])

print("\n")

print("=" * 70)
print("ChromaDB Verification Successful!")
print("=" * 70)