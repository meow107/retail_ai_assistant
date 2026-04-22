from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import ask_ai


router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(request: ChatRequest):
    answer = ask_ai(request.question)
    return {"answer": answer}


