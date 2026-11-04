from ValidationLayer import QuestionRequest
from AgentLayer import QuestionClassifier

classifier: QuestionClassifier = QuestionClassifier()

class QuestionProcessor:
    async def process_question(self,data:QuestionRequest):
        return await classifier.classify_question(data.question)