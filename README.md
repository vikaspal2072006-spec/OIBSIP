# OIBSIP
# 🎙️ Python Voice Assistant

## 📌 Project Overview

The Python Voice Assistant is a simple voice-controlled application developed using Python. It listens to user commands through a microphone, processes speech using speech recognition, and responds using voice output.

The assistant can perform basic tasks such as greeting users, answering simple questions, providing the current date and time, and searching for information on Google.

## ✨ Features

- **Voice Input:** Accepts voice commands through a microphone.
- **Voice Output:** Responds to users using Windows Speech API (SAPI5).
- **Greeting:** Responds to greetings such as Hello and Hi.
- **Name Identification:** Answers questions about its name.
- **How Are You:** Responds to basic conversational questions.
- **Date and Time:** Provides the current date and time.
- **Google Search:** Searches for information on Google using voice commands.
- **Exit Command:** Stops the assistant when the user says Stop, Exit, or Goodbye.
- **Error Handling:** Handles microphone, speech recognition, and internet connection errors.

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- PyWin32 (Windows SAPI5)
- Webbrowser
- DateTime
- URL Parsing

## 📂 Project Structure

```text
OIBSIP/
│
├── main.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vikaspal2072006-spec/OIBSIP.git
```

### 2. Navigate to the Project Folder

```bash
cd OIBSIP
```

### 3. Install Required Libraries

```bash
pip install SpeechRecognition pywin32
```

### 4. Install PyAudio

SpeechRecognition requires PyAudio for microphone input.

```bash
pip install PyAudio
```

### 5. Run the Application

```bash
python main.py
```

## 🎯 Available Voice Commands

| Voice Command | Assistant Response |
|---|---|
| Hello | Greets the user |
| What is your name? | Tells its name |
| How are you? | Responds to the user |
| What can you do? | Explains its features |
| What time is it? | Announces current time |
| What is today's date? | Announces current date |
| Search Python tutorials | Opens Google search |
| Stop / Exit / Goodbye | Closes the assistant |

## 💻 Requirements

- Python 3.x
- Windows Operating System
- Working microphone
- Internet connection for Google Speech Recognition and Google Search
- Speakers or headphones

## 📚 Learning Outcomes

Through this project, I learned about:

- Speech recognition using Python.
- Converting speech into text.
- Implementing voice responses using Windows SAPI5.
- Handling user commands.
- Working with Python libraries.
- Opening web searches programmatically.
- Handling errors and exceptions.

## 👨‍💻 Author

**Vikas Pal**

Python Voice Assistant Project

Developed as part of the **Oasis Infobyte Internship (OIBSIP)**.

---

⭐ If you find this project useful, feel free to explore the repository!