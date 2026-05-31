from app.rag.loader import load_law_documents

docs = load_law_documents()

print(
    f"Loaded {len(docs)} documents"
)

for doc in docs:

    print("\n")
    print("=" * 50)

    print(doc["filename"])

    print("=" * 50)

    print(
        doc["text"][:1000]
    )