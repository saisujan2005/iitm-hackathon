from app.rag.loader import (
    load_law_documents
)

from app.rag.chunker import (
    chunk_text
)

docs = load_law_documents()

for doc in docs:

    chunks = chunk_text(
        doc["text"]
    )

    print(
        f"\n{doc['filename']}"
    )

    print(
        f"Chunks: {len(chunks)}"
    )

    print("\nFirst Chunk:\n")

    print(chunks[0][:500])