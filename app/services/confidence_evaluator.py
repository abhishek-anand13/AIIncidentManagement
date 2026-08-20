from app.models.knowledge_context import RetrievedChunk


class ConfidenceEvaluator:
    """
    Evaluates the quality of retrieved knowledge.
    """

    HIGH_DISTANCE_THRESHOLD = 0.75
    MEDIUM_DISTANCE_THRESHOLD = 1.0

    MIN_HIGH_MATCHES = 3
    MIN_MEDIUM_MATCHES = 2

    def evaluate(
        self,
        retrieved_chunks: list[RetrievedChunk]
    ) -> str:
        """
        Determine retrieval confidence.
        """

        # No knowledge found
        if not retrieved_chunks:
            return "LOW"

        best_distance = min(
            chunk.distance
            for chunk in retrieved_chunks
        )

        average_distance = (
            sum(
                chunk.distance
                for chunk in retrieved_chunks
            )
            / len(retrieved_chunks)
        )

        number_of_chunks = len(retrieved_chunks)

        print("\n------ Confidence Evaluation ------")
        print(f"Best Distance    : {best_distance:.4f}")
        print(f"Average Distance : {average_distance:.4f}")
        print(f"Retrieved Chunks : {number_of_chunks}")
        print("-----------------------------------")

        # High confidence
        if (
            best_distance <= self.HIGH_DISTANCE_THRESHOLD
            and number_of_chunks >= self.MIN_HIGH_MATCHES
        ):
            return "HIGH"

        # Medium confidence
        if (
            best_distance <= self.MEDIUM_DISTANCE_THRESHOLD
            and number_of_chunks >= self.MIN_MEDIUM_MATCHES
        ):
            return "MEDIUM"

        return "LOW"