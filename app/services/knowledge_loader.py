from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import MarkdownHeaderTextSplitter


class KnowledgeLoader:
    """
    Loads enterprise markdown documents
    and splits them into semantic chunks.
    """

    def __init__(self):

        self.knowledge_path = Path("data/knowledge_base")

        self.headers = [
            ("#", "Header1"),
            ("##", "Header2"),
        ]

    def load_documents(self):

        loader = DirectoryLoader(
            path=str(self.knowledge_path),
            glob="**/*.md",
            loader_cls=TextLoader
        )

        return loader.load()

    def split_documents(self):

        documents = self.load_documents()

        splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.headers
        )

        chunks = []

        for document in documents:

            split_docs = splitter.split_text(
                document.page_content
            )

            for chunk in split_docs:

                chunk.metadata["source"] = document.metadata["source"]

                chunks.append(chunk)

        return chunks