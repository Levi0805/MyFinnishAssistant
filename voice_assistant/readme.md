# 🗣️ MyFinnishAssistant - AI Voice & Text Assistant

MyFinnishAssistant is an AI-powered voice and text assistant that can:
- 🎤 Recognize speech and provide AI-generated responses.
- ✍️ Answer typed questions using the Gemini AI model.
- 📸 Describe uploaded images using AI.
- 🔊 Convert text responses to speech.

---

## 🚀 Features
1. **Text Mode** - Type a question and get an AI-generated response.
2. **Voice Mode** - Speak a question, and the assistant will respond with text and speech.
3. **Image Mode** - Upload an image and get a detailed description.
4. **Exit Option** - Quit the program anytime.

---

## 📥 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/MyFinnishAssistant.git
cd MyFinnishAssistant/voice_assistant

2️⃣ Install Dependencies
- pip install python-dotenv
- pip install google-generativeai
- pip install sounddevice numpy vosk pyttsx3
- python voice.py
- pip install pillow

3️⃣ Download Vosk Speech Model
MyFinnishAssistant/
│── voice_assistant/
│   ├── main.py
│   ├── vosk-model-small-en-us-0.15/
│   ├── .env
│   ├── requirements.txt

4️⃣ Set Up API Key
GEMINI_API_KEY=your_google_generative_ai_key

🏃‍♂️ Running the Assistant
python main.py

📜 License
This project is licensed under the MIT License

## MyChatProject 
Description

- MyChatProject is a Django-based web application designed to support a chat functionality.
- The project follows the - standard Django structure and includes a chat app to handle messaging-related features.

## Folder Structure
voice_assistant/
│
├── mychatproject/
│   ├── chat/
│   │   ├── templates/       # Contains HTML templates
│   │   ├── __init__.py      # Marks chat as a Python package
│   │   ├── admin.py         # Admin panel configurations
│   │   ├── apps.py          # Chat app configuration
│   │   ├── forms.py         # Django forms for chat-related inputs
│   │   ├── models.py        # Database models for chat app
│   │   ├── tests.py         # Unit tests for the chat app
│   │   ├── urls.py          # URL routing for chat-related views
│   │   ├── views.py         # Views handling chat logic
│   │
│   ├── mychatproject/
│   │   ├── __pycache__/     # Compiled Python files
│   │   ├── __init__.py      # Marks mychatproject as a Python package
│   │   ├── asgi.py          # ASGI configuration
│   │   ├── settings.py      # Django settings
│   │   ├── urls.py          # Main URL configurations
│   │   ├── wsgi.py          # WSGI configuration
│
├── db.sqlite3               # SQLite database file
├── manage.py                # Django project management script
├── vosk-model-small-en/      # Directory for speech recognition model
├── .env                      # Environment variables file

# Navigate to the project directory:
- cd  mychatproject
# Apply migrations:
- python manage.py migrate
# Run the development server:
- python manage.py runserver

## Usage

- Open http://127.0.0.1:8000/ in a web browser to access   the chat application.


💡 Future Improvements
🔍 Add PDF summarization feature.
🎭 Support multiple languages.
📊 Improve speech recognition accuracy.
🔍 Add chat History feature
🔍 Add emotional sentiments 


👨‍💻 Authors

Developed by [Rachna Kumar, Levi, Hua Chen].





