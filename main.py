from chatbot_service import ChatbotService

def main():
    chatbot = ChatbotService()

    print("===LangChain AI chatbot ===")
    print("Type 'exit' to quit.")

    while True:
        question = input("\nYou: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break


        if not question.strip():
            continue

        try:
            answer = chatbot.ask(question)
            print(f"\nAI: {answer}")

        except Exception as ex:
            print(f"\nError: {ex}")

if __name__ == "__main__":
    main()
