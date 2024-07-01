from groq import Groq

class Chatbot:
    def __init__(self, args):
        self.initialize_client(api_key=args["api_key"])
        self.model = args["model"]

    def initialize_client(self, api_key):
        self.client = Groq(
            api_key=api_key,
        )
        self.messages = []

    def plant_seed(self, seed):
        if len(self.messages) > 0:
            raise Exception("Should only be called when Chatbot is initialized")
        
        self.messages.append({
            "role": "system",
            "content": seed,
        })

    def append_input_to_conversation(self, input):
        self.messages.append({
            "role": "user",
            "content": input,
        })

    def append_output_to_conversation(self, output):
        self.messages.append({
            "role": "assistant",
            "content": output,
        })

    def generate_output(self, input):
        self.append_input_to_conversation(input)

        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model=self.model,
        )
        output = chat_completion.choices[0].message.content
        self.append_output_to_conversation(output)

        return output
    
