import google.generativeai as genai
import os
import sounddevice as sd
import vosk
import queue
import json
import pyttsx3
from dotenv import load_dotenv
from PIL import Image
import sys  # Import sys for clean exit

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

# Initialize text-to-speech
engine = pyttsx3.init()

# Initialize speech recognition (moved inside try block)
q = queue.Queue()
try:  # Wrap vosk initialization
    model_vosk = vosk.Model(lang="en-us")
except Exception as e:
    print(f"❌ Error initializing Vosk model: {e}")
    model_vosk = None  # Important: Set to None if initialization fails
    sys.exit(1)  # Exit with error code if model fails to load


# Callback function to capture audio
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to capture voice input
def listen():
    if model_vosk is None:  # Check if model loaded successfully
        print("Vosk model not initialized. Cannot listen.")
        return None

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("\n🎤 Speak now...")
        rec = vosk.KaldiRecognizer(model_vosk, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text")  # Use .get() to avoid KeyError
                if text:
                    print(f"🗣️ You said: {text}")
                    return text
                # Removed the "could not understand" and return None. Let Gemini handle.
            # Add a timeout to the queue.get() to prevent indefinite blocking
            try:
                data = q.get(timeout=0.1)  # Check every 100ms
            except queue.Empty:
                pass  # No data, continue listening

# Function to process and describe an image (no changes needed)
def describe_image(image_path):
    try:
        img = Image.open(image_path)
        print("📸 Image uploaded successfully!")

        response = model.generate_content(["Describe this image in detail:", img])
        description = response.text

        print("\n🖼️ Gemini's Image Description:")
        print(description)

        speak(description)
    except Exception as e:
        print(f"❌ Error processing image: {e}")

# Main program flow (with improved exit handling)
while True: # Loop for multiple interactions
    print("\n🛠️ Choose an option:")
    print("1. Type a question (Text Response)")
    print("2. Speak a question (Voice Response)")
    print("3. Upload an image (Image Description)")
    print("4. Exit")  # Add an explicit exit option

    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "1":
        user_input = input("\n✍️ Type your question: ")
        if user_input.lower() in ["exit", "quit", "stop"]:
            break  # Exit the loop
        else:
            response = model.generate_content(user_input)
            answer = response.text
            print("\n🤖 Gemini's Response:")
            print(answer)

    elif choice == "2":
        speak("How can I assist you?")
        print("\n🤖 Assistant: How can I assist you?")

        user_input = listen()
        if user_input:
            if user_input.lower() in ["exit", "quit", "stop"]:
                break  # Exit the loop
            else:
                response = model.generate_content(user_input)
                answer = response.text
                print("\n🤖 Gemini's Response:")
                print(answer)

                speak(answer)
        else:
            print("❌ No speech input detected.")

    elif choice == "3":
        image_path = input("\n📁 Enter the image file path: ")
        describe_image(image_path)

    elif choice == "4":
        break  # Exit the loop

    else:
        print("❌ Invalid choice.")


# Clean up (outside the loop, after it breaks)
if model_vosk:  # Check if model was initialized
    del model_vosk
    print("Vosk model freed.")
print("👋 Exiting...")
sys.exit(0)