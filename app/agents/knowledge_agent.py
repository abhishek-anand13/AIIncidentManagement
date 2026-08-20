from app.models.knowledge_context import (
    KnowledgeContext,
    RetrievedChunk,
)

from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore
from app.services.confidence_evaluator import ConfidenceEvaluator


class KnowledgeAgent:
    """
    Responsible for retrieving relevant enterprise knowledge.
    """

    # Maximum acceptable semantic distance
    MAX_DISTANCE = 1.0

    def __init__(self):
        """
        Initialize all services required by the Knowledge Agent.
        """

        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore()

        self.confidence_evaluator = ConfidenceEvaluator()

    def retrieve(
        self,
        incident_description: str,
        top_k: int = 5
    ) -> KnowledgeContext:
        """
        Retrieve the most relevant enterprise knowledge
        for the given incident.
        """

        # Step 1: Convert incident description into an embedding
        query_embedding = self.embedding_service.create_embedding(
            incident_description
        )

        # Step 2: Search ChromaDB
        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        # Step 3: Remove weak matches
        filtered_results = self._filter_results(
            documents,
            metadatas,
            distances
        )

        # Step 4: Convert filtered results into RetrievedChunk objects
        retrieved_chunks = []

        for document, metadata, distance in filtered_results:

            retrieved_chunks.append(

                RetrievedChunk(

                    category=metadata["category"],

                    section=metadata["section"],

                    source=metadata["source"],

                    content=document,

                    distance=distance

                )

            )

        # Step 5: Evaluate confidence
        confidence = self.confidence_evaluator.evaluate(
            retrieved_chunks
        )

        # Step 6: Return structured knowledge context
        return KnowledgeContext(

            found=len(retrieved_chunks) > 0,

            confidence=confidence,

            retrieved_chunks=retrieved_chunks

        )

    def _filter_results(
        self,
        documents,
        metadatas,
        distances
    ):
        """
        Remove weak semantic matches before sending
        them to the AI.
        """

        filtered = []

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            if distance <= self.MAX_DISTANCE:

                filtered.append(
                    (
                        document,
                        metadata,
                        distance
                    )
                )

        return filtered