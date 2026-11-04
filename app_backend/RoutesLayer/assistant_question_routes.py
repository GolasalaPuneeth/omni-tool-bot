from fastapi import APIRouter
from ValidationLayer import QuestionRequest


assistant_router : APIRouter = APIRouter(tags=["Q&A Endpoints"], prefix="/v1/assistant")

@assistant_router.post("/questions")
async def submit_question(payload:QuestionRequest):
    return payload