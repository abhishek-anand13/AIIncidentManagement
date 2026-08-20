import chromadb


class VectorStore:
    """
    Handles all interactions with the ChromaDB vector database.
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="storage/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name="incident_knowledge"
        )

    def add_document(
        self,
        document_id: str,
        text: str,
        embedding: list,
        metadata: dict,
    ):
        """
        Store a document chunk in ChromaDB.
        """

        self.collection.add(
            ids=[document_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata],
        )

    def search(
        self,
        query_embedding: list,
        top_k: int = 5
    ):
        """
        Perform semantic similarity search.
        """

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results