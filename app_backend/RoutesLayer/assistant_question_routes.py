from fastapi import APIRouter
from ValidationLayer import QuestionRequest
from ServiceLayer import QuestionProcessor

assistant_router : APIRouter = APIRouter(tags=["Q&A Endpoints"], prefix="/v1/assistant")
service : QuestionProcessor = QuestionProcessor()

@assistant_router.post("/questions")
async def submit_question(payload:QuestionRequest):
    return await service.process_question(payload)