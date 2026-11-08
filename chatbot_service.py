
from langchain_core.output_parsers import StrOutputParser

from ollama_service import OllamaService
from prompt_service import PromptService


class ChatbotService:

    def __init__(self):
        self.ollama = OllamaService()
        self.prompt_service = PromptService()

        self.chain = (
            self.prompt_service.create_prompt()
            | self.ollama.get_model()
            | StrOutputParser()
        )

    def ask(self, question: str) -> str:
        response = self.chain.invoke({
            "question": question
        })

        return response
