
from langchain_core.chat_history import InMemoryChatMessageHistory


class ConversationService:

    def __init__(self):
        # Create an empty conversation history
        self.history = InMemoryChatMessageHistory()

    def get_messages(self):
        # Return all saved messages
        return self.history.messages

    def add_exchange(self, question: str, answer: str):
        # Save the user's question
        self.history.add_user_message(question)

        # Save the AI's answer
        self.history.add_ai_message(answer)

    def clear_history(self):
        # Delete all messages in this session
        self.history.clear()
