
from langchain_core.output_parsers import StrOutputParser

from ollama_service import OllamaService
from prompt_service import PromptService
from conversation_service import ConversationService

class ChatbotService:

    def __init__(self):
        self.ollama = OllamaService()
        self.prompt_service = PromptService()

        # NEW: Create conversation memory
        self.conversation = ConversationService()

        # Langchain pipeline
        self.chain = (
            self.prompt_service.create_prompt()
            | self.ollama.get_model()
            | StrOutputParser()
        )

    def ask(self, question: str) -> str:

        # Step 1: Read previous messages
        history = self.conversation.get_messages()

        # Step 2: Send history and new question
        response = self.chain.invoke({
            "history": history,
            "question": question
        })

        # Step 3: Save the new conversation
        self.conversation.add_exchange(
            question,
            response
            )

        return response

    def clear_memory(self):
        self.conversation.clear_history()
