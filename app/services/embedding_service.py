from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Responsible for converting text into vector embeddings.
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_embedding(self, text: str):
        """
        Convert text into an embedding vector.
        """
        return self.model.encode(text).tolist()