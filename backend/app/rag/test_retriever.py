from app.rag.retriever import (
    retrieve_context
)

question = (
    "Can police seize my vehicle?"
)

context = retrieve_context(
    question
)

print("\nQUESTION:\n")
print(question)

print("\nCONTEXT:\n")
print(context[:3000])