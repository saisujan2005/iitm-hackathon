from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_gateway_service import ask_ai
from app.ai.agent import answer

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    question: str

@router.post("/")
def chat(data: ChatRequest):

    answer = ask_ai(data.question)

    return {
        "question": data.question,
        "answer": answer
    }