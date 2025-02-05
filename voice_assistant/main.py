import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Make sure it's set in the .env file.")

# Configure Gemini API
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Ask user for a question
user_question = input("Ask me anything: ")

# Generate response
response = model.generate_content(user_question)

# Print response
print("\n🤖 Gemini's Response:")
print(response.text)
