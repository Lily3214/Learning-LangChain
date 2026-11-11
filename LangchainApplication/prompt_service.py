
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)


class PromptService:

    def create_prompt(self):
        return ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a helpful AI assistant. "
                "Answer questions clearly and naturally. "
                "Use conversation history when relevant."
            ),

            MessagesPlaceholder(variable_name="history"),

            (
                "human",
                "{question}"
            )
        ])
