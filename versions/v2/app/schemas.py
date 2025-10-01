from pydantic import BaseModel
from pydantic import Field

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)

class ChatResponse(BaseModel):
    request_id: str
    answer: str
    model: str
    elapsed_time: int

