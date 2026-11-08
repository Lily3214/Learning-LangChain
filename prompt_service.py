from langchain_core.prompts import ChatPromptTemplate

class PromptService:
    def create_prompt(self):
        return ChatPromptTemplate.from_messages([
            (
                "system",
                "you are a helpful API programming."
                "Explain technical concepts."),
                (
                    "human",
                    "{question}")
            ])
