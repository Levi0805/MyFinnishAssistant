import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

# Set Google Cloud AI Platform credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_CREDENTIALS_JSON")
project_id = os.getenv("PROJECT_ID")

# Validate environment variables
if not project_id:
    raise ValueError("Project ID not found. Please set PROJECT_ID in your .env file.")

# Function to Generate Response
def get_gemini_response(user_input):
    try:
        # Initialize the GenAI Client
        client = genai.Client(
            vertexai=True,
            project=project_id,
            location="us-central1",
        )

        # Model and User Prompt
        model = "gemini-2.0-flash-001"
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=user_input)
                ]
            )
        ]

        # Configuration for Response Generation
        generate_content_config = types.GenerateContentConfig(
            temperature=1,
            top_p=0.95,
            max_output_tokens=8192,
            response_modalities=["TEXT"],
            safety_settings=[
                types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
                types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"),
                types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"),
                types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
            ],
        )

        # Generate and Stream the Response
        print("\nAssistant Response:")
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            print(chunk.text, end="")
        print()  # For a clean new line
        
    except Exception as e:
        print(f"Error generating response: {e}")
        exit(1)

# Main App Loop
if __name__ == "__main__":
    print("Welcome to MyFinnishAssistant! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        get_gemini_response(user_input)


