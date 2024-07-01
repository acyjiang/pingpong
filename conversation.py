from bots.Chatbot import Chatbot

class Conversation:
    def __init__(self, chatbot_args, topic, conversation_length):
        self.initialize_chatbots(chatbot_args, topic)
        self.conversation_length = conversation_length

    def generate_chatbot_seed(self, topic, position):
        position_string = "first" if position == 1 else "second"
        seed =  f'You are a chatbot talking to another chatbot, who is given the same premise as you, about the following topic: \"{topic}\". \
                You will engage in a casual conversation with the other chatbot as if you are a human. You will be taking turns talking. Your replies will not be lengthy. \
                You will be the {position_string} to speak.'
        return seed

    def initialize_chatbots(self, chatbot_args, topic):
        seed1 = self.generate_chatbot_seed(topic, position=1)
        self.chatbot1 = Chatbot(chatbot_args)
        self.chatbot1.plant_seed(seed1)

        seed2 = self.generate_chatbot_seed(topic, position=2)
        self.chatbot2 = Chatbot(chatbot_args)
        self.chatbot2.plant_seed(seed2)

    def start_conversation(self):
        response = "Can you start off the conversation?"

        for _ in range(self.conversation_length):
            response = self.chatbot1.generate_output(response)

            print("#### CHATBOT 1 ####", response)
            print()

            response = self.chatbot2.generate_output(response)

            print("#### CHATBOT 2 ####", response)
            print()
