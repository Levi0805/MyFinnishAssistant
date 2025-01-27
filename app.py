import os
from dotenv import load_dotenv
import openai
from promptlayer import PromptLayer

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from the environment
promptlayer_api_key = os.getenv("PROMPTLAYER_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Validate API keys
if not promptlayer_api_key:
    raise ValueError("PromptLayer API key not found. Please set PROMPTLAYER_API_KEY in your .env file.")
if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")

# Initialize PromptLayer client
promptlayer_client = PromptLayer(api_key=promptlayer_api_key)

# Set OpenAI API key
openai.api_key = openai_api_key

# Greet the user and collect input
user_input = input("Welcome to MyFinnishAssistant! How can I help?\n> ")

# Fetch the PromptLayer template and handle errors
try:
    mychatgpt_prompt = promptlayer_client.templates.get("MyFinnishAssistant", {
        "provider": "openai",
        "input_variables": {
            "question": user_input
        }
    })
except Exception as e:
    print(f"Error fetching template: {e}")
    exit(1)

# Make the OpenAI request with PromptLayer tagging
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ensure you specify a model
        messages=mychatgpt_prompt['llm_kwargs']['messages'],  # Pass messages from the template
        pl_tags=["mychatgpt-dev"]  # Add PromptLayer tags
    )

    # Print the assistant's response
    print("\nAssistant Response:")
    print(response['choices'][0]['message']['content'])
except Exception as e:
    print(f"Error generating response: {e}")
    exit(1)

