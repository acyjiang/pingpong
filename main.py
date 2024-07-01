import os
from dotenv import load_dotenv
from bots.Chatbot import Chatbot

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


def main():
    model = "llama3-8b-8192"

    args = {
        'api_key': GROQ_API_KEY,
        'model': model,
        'seed': None,
    }

    chatbot = Chatbot(args)

    question1 = "Explain the importance of fast language models"
    response = chatbot.generate_response(question1)

    print(response)

    question2 = "With that in mind, why is Groq a good tool?"
    response = chatbot.generate_response(question2)

    print(response)


if __name__ == "__main__":
    main()
