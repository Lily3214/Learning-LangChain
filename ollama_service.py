
from langchain_ollama import ChatOllama


class OllamaService:

    def __init__(self, model_name="llama3.2"):
        self.model = ChatOllama(
            model=model_name,
            base_url="http://localhost:11434",
            temperature=0
        )

    def get_model(self):
        return self.model
