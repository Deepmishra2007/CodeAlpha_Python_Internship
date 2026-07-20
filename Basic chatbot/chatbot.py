# ------------------------------------
# Project: Basic Chatbot
# Internship: CodeAlpha Python Internship
# Developed by: Deep Mishra
# ------------------------------------
print("🤖 Welcome to Basic Chatbot!")
print("Type 'bye' to end the chat.")

while True:
    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is CodeBot.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")