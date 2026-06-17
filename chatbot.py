print("=================================")
print("   Welcome to AI Chatbot ")
print("=================================")

while True:

    user = input("You: ").lower()

    if user in ["hello", "hi", "assalam o alaikum"]:
        print("Bot: Hello! Welcome to the AI Chatbot. How may I assist you today?")

    elif user == "how are you":
        print("Bot: Thank you for asking. I am functioning perfectly and ready to assist you.")

    elif user == "your name":
        print("Bot: I am an AI Chatbot developed to assist and interact with users.")

    elif user == "help":
        print("Bot: You can type greetings, ask my name, ask how I am, or type 'bye' to exit.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Thank you for using AI Chatbot. Have a great day. Goodbye!")
        break

    else:
        print("Bot: I apologize, but I do not understand that command. Please try again.")