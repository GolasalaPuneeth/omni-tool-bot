from pydantic import BaseModel

class QuestionRequest(BaseModel):
    device_id:str
    question:str