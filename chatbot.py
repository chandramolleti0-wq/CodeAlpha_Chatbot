def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Greetings
        if user_input == "hello":
            print("Chatbot: Hi there!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: I am a Python chatbot.")

        # Calculator Feature
        elif "+" in user_input:
            numbers = user_input.split("+")
            result = int(numbers[0]) + int(numbers[1])
            print("Result:", result)

        elif "-" in user_input:
            numbers = user_input.split("-")
            result = int(numbers[0]) - int(numbers[1])
            print("Result:", result)

        elif "*" in user_input:
            numbers = user_input.split("*")
            result = int(numbers[0]) * int(numbers[1])
            print("Result:", result)

        elif "/" in user_input:
            numbers = user_input.split("/")
            result = int(numbers[0]) / int(numbers[1])
            print("Result:", result)

        # Exit
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

# Run chatbot
chatbot()
