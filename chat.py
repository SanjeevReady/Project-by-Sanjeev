# Random Chatbot for College

import random

class CollegeChatbot:
    def __init__(self):
        self.greetings = ["Hello! How can I assist you today?", "Hi there! What do you need help with?", "Greetings! What can I do for you?"]
        self.courses = ["Computer Science", "Business Administration", "Psychology", "Biology", "Mathematics"]
        self.advice = ["Stay organized and manage your time well.", "Don't hesitate to ask for help when you need it.", "Join study groups to enhance your learning experience."]

    def greet(self):
        return random.choice(self.greetings)

    def get_courses(self):
        return random.choice(self.courses)

    def get_advice(self):
        return random.choice(self.advice)

    def chat(self):
        print(self.greet())
        while True:
            user_input = input("You: ")
            if "course" in user_input.lower():
                print("Bot:", self.get_courses())
            elif "advice" in user_input.lower():
                print("Bot:", self.get_advice())
            elif "exit" in user_input.lower():
                print("Bot: Goodbye! Have a great day!")
                break
            else:
                print("Bot: I'm sorry, I didn't understand that. Please ask about courses or advice.")

if __name__ == "__main__":
    chatbot = CollegeChatbot()
    chatbot.chat()
