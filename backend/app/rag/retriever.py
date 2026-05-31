import re

from app.rag.embeddings import get_embedding
from app.rag.vector_store import collection


def retrieve_context(
    question: str,
    top_k: int = 5
):

    # Detect section references

    section_match = re.search(
        r"section\s+(\d+[A-Z]?)",
        question,
        re.IGNORECASE
    )

    if section_match:

        section_number = (
            section_match.group(1)
        )

        # Search all chunks

        all_docs = collection.get()

        matching_chunks = []

        for doc in all_docs["documents"]:

            if (
                f"{section_number}."
                in doc
            ):

                matching_chunks.append(
                    doc
                )

        if matching_chunks:

            return "\n\n".join(
                matching_chunks[:3]
            )

    # Fallback to semantic search

    embedding = get_embedding(
        question
    )

    results = collection.query(
        query_embeddings=[
            embedding
        ],
        n_results=top_k
    )

    documents = results[
        "documents"
    ][0]

    return "\n\n".join(
        documents
    )