from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["ai"])

class ChatInput(BaseModel):
    text: str

@router.post("/parse")
def parse_text(data: ChatInput):
    # Placeholder — integrate OpenAI or Llama here
    return {
        "intent": "sale",
        "parsed": {"message": data.text}
    }
