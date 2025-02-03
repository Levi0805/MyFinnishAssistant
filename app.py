import os
from dotenv import load_dotenv
from promptlayer import PromptLayer

# Load environment variables from .env file
load_dotenv()

# Initialize PromptLayer client with your API key
promptlayer_client = PromptLayer(api_key=os.getenv("API_KEY"))

user_input = input("Welcome to MyFinnishAssistant! How can I help?\n> ")

try:
    # Grab the prompt from PromptLayer
    mychatgpt_prompt = promptlayer_client.templates.get("MyFinnishAssistant", {
        "provider": "openai",
        "input_variables": {
            "question": user_input
        }
    })

    # Using promptlayer to create a completion
    response = promptlayer_client.chat.completions.create(
        **mychatgpt_prompt['llm_kwargs'],
        pl_tags=["mychatgpt-dev"],
    )

    # Print the response message
    print(response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")