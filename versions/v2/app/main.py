import time, uuid
from fastapi import FastAPI, HTTPException, Header
from app.schemas import ChatRequest, ChatResponse
from app.provider import CohereProvider
from  typing import Annotated

app = FastAPI(title="Chat Gateway V2")
provider = CohereProvider()


#  x_idempotency_key  = deduplicaiton id 
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, x_idempotency_key: Annotated[str | None, Header()] = None ):
    start = time.perf_counter()
    try:
        answer = provider.chat(req.message)
    except Exception as e:
        # map any provider error to a clean 502 for now
        raise HTTPException(status_code=502, detail="Upstream failed") from e

    elapsed_ms = int((time.perf_counter() - start) * 1000)
    return ChatResponse(
        request_id=x_idempotency_key or str(uuid.uuid4()),
        answer=answer,
        model=provider.name,
        elapsed_time=elapsed_ms,
    )

