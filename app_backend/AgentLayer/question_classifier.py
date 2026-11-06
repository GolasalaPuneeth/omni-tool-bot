from pydantic_ai import Agent
from ValidationLayer import QueryEvaluation
from dotenv import load_dotenv

load_dotenv()

class QuestionClassifier:
    default_agent: Agent = Agent('typesafe:jev-latest', output_type=QueryEvaluation)

    def __init__(self, agent: Agent | None = None):
        self.agent = agent or self.default_agent

    async def classify_question(self, q: str) :
        result = await self.agent.run(q)
        result = result.output
        return result.category