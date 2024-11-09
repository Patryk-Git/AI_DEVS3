from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()


class Model:

    def __init__(self, model: str = "gpt-3.5-turbo"):
        """
        Initializes the Model class by loading the API key from environment variables
        and setting up the OpenAI client and model.
        """
        self.api_key = os.getenv("OPEN_AI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        self.model = model

    def chat(self, system_message: str, user_message: str) -> str:
        """
        Generates a response from the OpenAI model based on the provided system and user messages.

        Args:
            system_message (str): The system message to set the context for the conversation.
            user_message (str): The user's message to which the model should respond.

        Returns:
            str: The content of the model's response.
        """
        completions = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
        )
        return completions.choices[0].message.content
