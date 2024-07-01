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

    topic = "Tennis"
    conversation_length = 5

    conversation = Conversation(
        chatbot_args=chatbot_args,
        topic=topic,
        conversation_length=conversation_length
    )

    conversation.start_conversation()

if __name__ == "__main__":
    main()
