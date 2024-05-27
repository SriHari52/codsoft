import random

class CodsoftChatbot:
    def __init__(self):
        self.greetings = ["Hi there!", "Hello!", "Hey!"]
        self.farewells = ["Goodbye! Have a great day!", "See you later!", "Take care!"]
        self.suggested_questions = {
            "What's the weather like today?": ["It's sunny today!", "Looks like rain later.", "Cloudy with a chance of showers."],
            "Have you seen any good movies lately?": ["Yes, I recently watched a great movie!", "Not lately, but I've heard good things about some new releases."],
            "What are your hobbies?": ["I enjoy coding, reading, and learning new things!", "I like to relax by watching movies and going for walks."]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        rules = {
            "hello": self.respond_to_greeting,
            "how are you": self.respond_to_inquiry,
            "bye": self.respond_to_farewell,
        }

        for pattern, response_func in rules.items():
            if pattern in user_input:
                return response_func()

        for suggested_question, responses in self.suggested_questions.items():
            if suggested_question.lower() in user_input:
                return random.choice(responses)

        return self.generate_default_response()

    def respond_to_greeting(self):
        return random.choice(self.greetings)

    def respond_to_inquiry(self):
        return "I'm just a computer program, but I'm functioning well. Thanks for asking!"

    def respond_to_farewell(self):
        return random.choice(self.farewells)

    def generate_default_response(self):
        response = "I'm sorry, I didn't quite catch that. Could you please rephrase or ask another question?"
        response += " If you're not sure what to ask, how about trying one of these: '{}'?".format("', '".join(self.suggested_questions.keys()))
        return response

def main():
    chatbot = CodsoftChatbot()
    print("Welcome to Codsoft Chatbot!")
    print("Feel free to start chatting. Type 'bye' to exit.")

    while True:
        try:
            user_input = input("You: ")

            if user_input.lower() == 'bye':
                print("Codsoft:", chatbot.get_response(user_input))
                break
            else:
                print("Codsoft:", chatbot.get_response(user_input))
        except KeyboardInterrupt:
            print("\nGoodbye! Exiting...")
            break
        except Exception as e:
            print("Oops! Something went wrong:", e)

if __name__ == "__main__":
    main()
    
