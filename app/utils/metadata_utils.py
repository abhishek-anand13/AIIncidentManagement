from pathlib import Path


class MetadataUtils:
    """
    Utility class for generating document IDs and metadata
    for ChromaDB indexing.
    """

    @staticmethod
    def build_document_id(chunk, chunk_number: int) -> str:
        """
        Generate a unique document ID.

        Example:
        INC001_database_timeout_Symptoms_1
        """

        source = Path(chunk.metadata["source"]).stem
        section = chunk.metadata.get("Header1", "Unknown")

        # Make section safe for IDs
        section = (
            section.lower()
            .replace(" ", "_")
            .replace("/", "_")
        )

        return f"{source}_{section}_{chunk_number}"

    @staticmethod
    def build_metadata(chunk) -> dict:
        """
        Build clean metadata for ChromaDB.
        """

        source_path = Path(chunk.metadata["source"])

        return {
            "source": source_path.name,
            "category": source_path.parent.name,
            "section": chunk.metadata.get("Header1", "Unknown")
        }