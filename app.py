import os
from dotenv import load_dotenv
import openai
from openai import OpenAI
from promptlayer import PromptLayer

load_dotenv()
promptlayer_client = PromptLayer(api_key=os.getenv(pl_client))

OpenAI = promptlayer_client.openai.OpenAI
client = OpenAI()
user_input = input("Welcome to MyFinnishAssistant! How can I help?\n> ")

# Grab the prompt from PromptLayer
mychatgpt_prompt = promptlayer_client.templates.get("MyFinnishAssitant", {
    "provider": "openai",
    "input_variables": {
        "question": user_input
    }
})

# Run the OpenAI req
response = client.chat.completions.create(
    **mychatgpt_prompt['llm_kwargs'],
    pl_tags=["mychatgpt-dev"],
)

print(response.choices[0].message.content)
