from ValidationLayer import QuestionRequest
from AgentLayer import QuestionClassifier
from AppUtils import get_time_spacy

classifier: QuestionClassifier = QuestionClassifier()

class QuestionProcessor:
    async def process_question(self,data:QuestionRequest):
        res = await classifier.classify_question(data.question)
        if res == "time":
            return get_time_spacy(data.question)
        return 'Miss match'