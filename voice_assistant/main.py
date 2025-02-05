import google.generativeai as genai
import os
import sounddevice as sd
import vosk
import queue
import json
import pyttsx3
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

# Initialize text-to-speech
engine = pyttsx3.init()

# Initialize speech recognition
q = queue.Queue()
model_vosk = vosk.Model(lang="en-us")

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
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("\n🎤 Speak now...")
        rec = vosk.KaldiRecognizer(model_vosk, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result["text"]
                if text:
                    print(f"🗣️ You said: {text}")
                    return text
                else:
                    print("❌ Could not understand the audio")
                    return None

# Main loop for continuous conversation
while True:
    user_input = listen()  # Get voice input
    if user_input:
        if user_input.lower() in ["exit", "quit", "stop"]:
            print("👋 Exiting...")
            speak("Goodbye!")
            break  # Exit loop

        # Get Gemini AI response
        response = model.generate_content(user_input)
        answer = response.text
        print("\n🤖 Gemini's Response:")
        print(answer)
        
        # Speak the response
        speak(answer)
