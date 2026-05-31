from app.rag.rag_service import (
    answer_with_rag
)

answer = answer_with_rag(
    "Can police seize my vehicle?"
)

print(answer)