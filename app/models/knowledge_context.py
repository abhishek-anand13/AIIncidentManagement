from pydantic import BaseModel
from typing import List


class RetrievedChunk(BaseModel):
    """
    Represents one chunk retrieved from the knowledge base.
    """

    category: str
    section: str
    source: str
    content: str
    distance: float


class KnowledgeContext(BaseModel):
    """
    Final response returned by the Knowledge Agent.
    """

    found: bool
    confidence: str
    retrieved_chunks: List[RetrievedChunk]