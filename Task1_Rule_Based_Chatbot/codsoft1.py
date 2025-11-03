import datetime

def chatbot():
    print("chatbot: Hey there! I'm chatbot. Type 'exit' anytime to stop chatting.\n")

    while True:
        user = input("You: ").lower().strip()

        if user in ["hi", "hello", "hey"]:
            print("chatbot Bot: Hi! Nice to meet you...!!")
        elif "how are you" in user:
            print("chatbot: I'm functioning perfectly!")
        elif " what is your name" in user:
            print("chatbot: I'm SmartTalk, your friendly mini chatbot")
        elif "date" in user:
            today = datetime.date.today().strftime("%B %d, %Y")
            print(f"chatbot: Today’s date is {today}.")
        elif "who made you" in user or "created" in user:
            print("chatbot: I was built by a Python learner-Slesha, experimenting with AI!")
        elif "bye" in user or "quit" in user or "exit" in user:
            print("chatbot: Goodbye! Have a great day")
            break
        elif "weather" in user:
            print("chatbot: Hmm, I can't check the weather yet, but I hope it's sunny where you are!")
        elif "thankyou" in user:
            print("chatbot: You’re most welcome")
        else:
            print("chatbot: I'm sorry,I didn’t get that....can you try saying it another way?")

# Run the chatbot
chatbot()
