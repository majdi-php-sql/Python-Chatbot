from app.chatbot import get_answer  # I imported the get_answer function from the chatbot module

def chat():
    """
    I wrote this function to initiate a simple command-line interface for the chatbot.
    """
    print("Hello! Ask me about any product.")  # I provided a welcome message to the user
    while True:
        user_input = input("You: ")  # I prompted the user for input
        if user_input.lower() in ["exit", "quit"]:  # I checked if the user wants to exit the chat
            break  # I broke the loop to end the chat
        response = get_answer(user_input)  # I processed the user's question to get a response
        print(f"Bot: {response}")  # I printed the chatbot's response

if __name__ == "__main__":
    chat()  # I called the chat function to start the chatbot
