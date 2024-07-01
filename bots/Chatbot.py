from groq import Groq

class Chatbot:
    def __init__(self, args):
        self.initialize_client(api_key=args["api_key"])

        self.messages = []
        self.plant_seed(seed=args["seed"])

        self.model = args["model"]

    def initialize_client(self, api_key):
        self.client = Groq(
            api_key=api_key,
        )

    def plant_seed(self, seed):
        if len(self.messages) > 0:
            raise Exception("Should only be called when Chatbot is initialized")
        
        if seed:
            self.messages.append({
                "role": "user",
                "content": seed,
            })

    def append_message_to_conversation(self, message):
        self.messages.append({
            "role": "user",
            "content": message,
        })

    def generate_response(self, input):
        self.append_message_to_conversation(input)

        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model=self.model,
        )

        return chat_completion.choices[0].message.content
    
