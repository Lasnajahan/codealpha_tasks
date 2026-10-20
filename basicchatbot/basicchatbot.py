
def chatbot():
    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Chatbot: You can say hello, ask how I am, or say bye.")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey", "hel10"]:
            print("Chatbot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()

