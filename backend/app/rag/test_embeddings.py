from app.rag.embeddings import (
    get_embedding
)

vector = get_embedding(
    "Section 129 helmet law"
)

print(
    f"Vector length: {len(vector)}"
)

print(
    vector[:10]
)