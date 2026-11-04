from pydantic_ai import Agent
from ValidationLayer import QueryEvaluation


class QuestionClassifier:
    default_agent: Agent = Agent('typesafe:jev-latest', output_type=QueryEvaluation)

    def __init__(self, agent: Agent | None = None):
        self.agent = agent or self.default_agent

    async def classify_question(self, q: str) -> QueryEvaluation:
        result = await self.agent.run(q)
        return result