from app.rag.loader import load_law_documents
from app.rag.chunker import chunk_text
from app.rag.embeddings import get_embedding
from app.rag.vector_store import collection


def build_index():

    docs = load_law_documents()

    count = 0

    for doc in docs:

        chunks = chunk_text(
            doc["text"]
        )

        for chunk in chunks:

            embedding = get_embedding(
                chunk
            )

            collection.add(
                ids=[f"chunk_{count}"],
                documents=[chunk],
                embeddings=[embedding],
                metadatas=[
                    {
                        "source":
                        doc["filename"]
                    }
                ]
            )

            count += 1

    print(
        f"Indexed {count} chunks"
    )


if __name__ == "__main__":
    build_index()