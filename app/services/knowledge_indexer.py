from app.services.embedding_service import EmbeddingService
from app.services.knowledge_loader import KnowledgeLoader
from app.services.vector_store import VectorStore
from app.utils.metadata_utils import MetadataUtils


class KnowledgeIndexer:
    """
    Reads enterprise knowledge,
    creates embeddings,
    and stores them in ChromaDB.
    """

    def __init__(self):
        self.loader = KnowledgeLoader()
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def index_knowledge(self):
        """
        Index all meaningful knowledge chunks into ChromaDB.
        """

        chunks = self.loader.split_documents()

        print(f"Found {len(chunks)} chunks.")

        indexed_count = 0
        skipped_count = 0

        # Sections that are useful for semantic retrieval
        allowed_sections = {
            "Symptoms",
            "Root Cause",
            "Resolution",
            "Lessons Learned",
            "Keywords",
            "Description",
            "Workaround",
            "Permanent Fix",
            "Related Runbook",
            "Purpose",
            "Preconditions",
            "Resolution Steps",
            "Verification",
            "Rollback",
            "Escalation",
            "Scope",
            "Responsibilities",
            "Procedure",
            "Escalation Matrix",
            "Communication Guidelines",
            "Best Practices"
        }

        for index, chunk in enumerate(chunks):

            section = chunk.metadata.get("Header1", "")

            # Skip chunks that don't add retrieval value
            if section not in allowed_sections:
                skipped_count += 1
                continue

            document_id = MetadataUtils.build_document_id(
                chunk,
                index
            )

            metadata = MetadataUtils.build_metadata(chunk)

            embedding = self.embedding_service.create_embedding(
                chunk.page_content
            )

            self.vector_store.add_document(
                document_id=document_id,
                text=chunk.page_content,
                embedding=embedding,
                metadata=metadata,
            )

            indexed_count += 1

        print(f"\nIndexed Chunks : {indexed_count}")
        print(f"Skipped Chunks : {skipped_count}")
        print("\nKnowledge Base Indexed Successfully!")