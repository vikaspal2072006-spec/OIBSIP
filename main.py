
import speech_recognition as sr
import pyttsx3
import webbrowser
from urllib.parse import quote_plus




# Initialize voice assistant
recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)


# Function to speak
def speak(text):
    print("Assistant:", text)

    engine.stop()
    engine.say(str(text))
    engine.runAndWait()


# Function to listen
def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now!")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=7
            )

        text = recognizer.recognize_google(audio)
        print("You said:", text)

        return text.lower().strip()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""

    except sr.WaitTimeoutError:
        print("No voice detected. Listening again...")
        return ""

    except sr.RequestError as e:
        print("Internet connection error:", e)
        return ""

    except Exception as e:
        print("Microphone error:", e)
        return ""


# Welcome message
speak("Hello! How may I assist you?")


# Main program
while True:

    command = listen()

    if not command:
        continue

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello! Nice to meet you.")

    # Asking name
    elif "name" in command:
        speak("My name is your personal voice assistant.")

    # Asking how are you
    elif "how are you" in command or "how r u" in command:
        speak("I am fine. Thank you for asking.")

    # Asking what can you do
    elif "what can you do" in command:
        speak("I can listen to your voice and answer simple questions.")

    # Asking for time
    elif "time" in command:
        import datetime
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    # Asking for date
    elif "date" in command:
        import datetime
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    # Web search
    elif command.startswith("search "):
        query = command.replace("search","",1).strip()

        if query:
            speak("Searching Google for "+query)
            search_url = "https://www.google.com/search?q="+quote_plus(query)
            webbrowser.open(search_url)
        else:
            speak("please tell me what you want to search .")
    # Exit commands
    elif any(word in command for word in ["stop", "exit", "goodbye", "good bye"]):
        speak("Goodbye! Have a nice day.")
        break

    # Unknown command
    else:
        speak("Sorry, I don't know that command yet. Please try another command.")
        
