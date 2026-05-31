from app.rag.embeddings import get_embedding
from app.rag.vector_store import collection


def retrieve_context(
    question: str,
    top_k: int = 3
):

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