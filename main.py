
import speech_recognition as sr
import webbrowser
import win32com.client
import datetime
from urllib.parse import quote_plus


# Initialize voice assistant
recognizer = sr.Recognizer()

# Initialize Windows SAPI5 speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")


# Function to speak
def speak(text):
    print("Assistant:", text)

    try:
        speaker.Speak(str(text))
    except Exception as e:
        print("Speech error:", e)


# Function to listen
def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now!")

            recognizer.adjust_for_ambient_noise(
                source, duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=7
            )

        text = recognizer.recognize_google(audio)
        print("You said:", text)

        return text.lower().strip()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.WaitTimeoutError:
        speak("No voice detected. Listening again...")
        return ""

    except sr.RequestError as e:
        print("Internet connection error:", e)
        speak("Internet connection error.")
        return ""

    except Exception as e:
        print("Microphone error:", e)
        speak("Microphone error.")
        return ""


# Welcome message
speak("Hello! How may I assist you?")
speak("I am ready to listen.")


# Main program
while True:

    command = listen()

    if not command:
        continue

    # Web Search
    if command.startswith("search "):

        query = command.replace("search ", "", 1).strip()

        if query:
            speak("Searching Google for " + query)

            search_url = (
                "https://www.google.com/search?q="
                + quote_plus(query)
            )

            webbrowser.open(search_url)

        else:
            speak("Please tell me what you want to search.")

    # Exit commands
    elif (
        any(word in command.split()
            for word in ["stop", "exit", "goodbye"])
        or "good bye" in command
    ):
        speak("Goodbye! Have a nice day.")
        break

    # Greeting
    elif any(
        word in command.split()
        for word in ["hello", "hi", "hay", "hii"]
    ):
        speak("Hello! Nice to meet you.")

    # Asking name
    elif "name" in command.split():
        speak("My name is your personal voice assistant.")

    # Asking how are you
    elif "how are you" in command or "how r u" in command:
        speak("I am fine. Thank you for asking.")

    # Asking what can you do
    elif "what can you do" in command:
        speak(
            "I can listen to your voice and answer simple questions."
        )

    # Asking for time
    elif "time" in command.split():
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    # Asking for date
    elif "date" in command.split():
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    # Unknown command
    else:
        speak(
            "Sorry, I don't know that command yet. "
            "Please try another command."
        )
