from chatbot_service import ChatbotService

def main():
    chatbot = ChatbotService()

    print("===LangChain AI chatbot ===")
    print("Type 'exit' to quit.")
    print("Type 'clear' to reset conversation history.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if question.lower() == "clear":
            chatbot.clear_memory()
            print("Conversation history cleared!")
            continue

        if not question:
            continue

        try:
            answer = chatbot.ask(question)
            print(f"\nAI: {answer}")

        except Exception as ex:
            print(f"\nError: {ex}")

if __name__ == "__main__":
    main()
