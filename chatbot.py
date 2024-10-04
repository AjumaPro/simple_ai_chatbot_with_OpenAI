from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

#client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"
def chat_with_gpt(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message['content'].strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", completion)
