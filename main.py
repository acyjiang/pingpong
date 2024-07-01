import os
from dotenv import load_dotenv
from bots.Chatbot import Chatbot
from conversation import Conversation

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


def main():
    model = "llama3-8b-8192"

    chatbot_args = {
        'api_key': GROQ_API_KEY,
        'model': model,
    }

    # chatbot = Chatbot(chatbot_args)

    # question1 = "Explain the importance of fast language models"
    # response = chatbot.generate_output(question1)

    # print(response)

    # question2 = "With that in mind, why is Groq a good tool?"
    # response = chatbot.generate_output(question2)

    # print(response)

    topic = "Trump"
    conversation_length = 5

    conversation = Conversation(
        chatbot_args=chatbot_args,
        topic=topic,
        conversation_length=conversation_length
    )

    conversation.start_conversation()

if __name__ == "__main__":
    main()
