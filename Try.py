import speech_recognition as sr
import pyttsx3
import os
import time

# Initialize the speech recognition and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        return None  # Return None instead of speaking
    except sr.RequestError:
        speak("Service unavailable.")
        return None

def ayanokoji_response(command):
    # Define responses based on input
    if "open" in command:
        app_name = command.split("open", 1)[1].strip()
        if app_name:
            speak(f"Opening {app_name}.")
            os.system(f'start {app_name}')
        else:
            speak("Application name not recognized.")
    elif "what do you think" in command:
        speak("I analyze all options carefully before forming an opinion.")
    elif "help" in command:
        speak("What assistance do you require?")
    else:
        speak("I understand.")

# Flag to track if the last response was an unknown command
last_response_unknown = False

while True:
    command = listen()
    if command:
        if "stop" in command or "exit" in command:
            speak("Stopping the assistant.")
            break
        ayanokoji_response(command)
        last_response_unknown = False  # Reset the flag on a valid command
    else:
        if not last_response_unknown:
            speak("I didn't catch that.")
            last_response_unknown = True  # Set the flag after speaking
    time.sleep(1)
