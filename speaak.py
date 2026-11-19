import win32com.client
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Speak("This is the first sentence.")
time.sleep(1)

speaker.Speak("This is the second sentence.")
time.sleep(1)

speaker.Speak("This is the third sentence.")