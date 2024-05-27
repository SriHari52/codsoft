import random

class SimpleChatbot:
    def __init__(self):
        # Define common greetings and farewells
        self.greetings = ["Hi there!", "Hello!", "Hey!"]
        self.farewells = ["Goodbye! Have a great day!", "See you later!", "Take care!"]

    def get_response(self, user_input):
        # Convert user input to lowercase for easier comparison
        user_input = user_input.lower()

        # Define rules and corresponding response functions
        rules = {
            "hello": self.respond_to_greeting,
            "how are you": self.respond_to_inquiry,
            "bye": self.respond_to_farewell,
        }

        # Iterate through rules to find a matching pattern
        for pattern, response_func in rules.items():
            if pattern in user_input:
                return response_func()

        # If no predefined rule matches, provide a default response
        return self.generate_default_response()

    def respond_to_greeting(self):
        # Select a random greeting from the list
        return random.choice(self.greetings)

    def respond_to_inquiry(self):
        # Respond to inquiry about the bot's status
        return "I'm just a computer program, but I'm functioning well. Thanks for asking!"

    def respond_to_farewell(self):
        # Select a random farewell from the list
        return random.choice(self.farewells)

    def generate_default_response(self):
        # Provide a default response when no specific rule matches
        return "I'm sorry, I didn't quite catch that. Could you please rephrase or ask another question?"

def main():
    # Initialize the chatbot
    chatbot = SimpleChatbot()

    # Display initial message to the user
    print("Welcome to the Simple Chatbot!")
    print("Feel free to start chatting. Type 'bye' to exit.")

    # Main loop for interacting with the chatbot
    while True:
        try:
            # Get user input
            user_input = input("You: ")

            # Check if user wants to exit
            if user_input.lower() == 'bye':
                print(chatbot.get_response(user_input))
                break
            else:
                # Provide response based on user input
                print("Bot:", chatbot.get_response(user_input))
        except KeyboardInterrupt:
            # Handle keyboard interruption gracefully
            print("\nGoodbye! Exiting...")
            break
        except Exception as e:
            # Handle unexpected errors
            print("Oops! Something went wrong:", e)

if __name__ == "__main__":
    # Start the chatbot
    main()
