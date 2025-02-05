## Prerequirement
- .env file alwaye replace GEMINI_API_KEY your personal key
- pip install python-dotenv
- pip install google-generativeai
- pip install sounddevice numpy vosk pyttsx3
- python voice.py
- pip install pillow


## How its work
✅ Offline Speech Recognition → Uses vosk (works without an internet connection)
✅ Accurate AI Responses → Uses Gemini AI for generating answers
✅ Text-to-Speech → Uses pyttsx3 for speaking responses

## 🎯 How This output 
- When you run the script, it asks:
- "Speak a question" (Option 1) → Uses voice input + Gemini AI
- "Upload an image" (Option 2) → Asks for an image file and describes it
- If you choose an image, it:
- Loads the image
- Asks Gemini AI to describe it
- Prints & speaks the description



