import speech_recognition as sr
import pyttsx3
import os
import subprocess  # Import subprocess module for silent process termination

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Friday: {text}")  # Print the response to the console
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        speak("I'm listening, sir.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech service is unavailable.")
            return ""

def execute_command(command):
    # Opening Applications
    if "open chrome" in command:
        speak("Opening Google Chrome.")
        os.system("start chrome")
    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("start notepad")

    # Closing Applications Silently (No success message printed)
    elif "close chrome" in command:
        speak("Closing Chrome.")
        subprocess.run(["taskkill", "/f", "/im", "chrome.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif "close notepad" in command:
        speak("Closing Notepad.")
        subprocess.run(["taskkill", "/f", "/im", "notepad.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # System shutdown
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")

    # Exit program
    elif "exit" in command or "quit" in command:
        speak("Goodbye, sir.")
        exit()

    # Respond to casual questions
    elif "what's up" in command or "how are you" in command:
        speak("I'm doing fantastic! How can I help you today?")
    
    elif "what would you do for me" in command:
        speak("I can open and close applications, answer questions, set reminders, and even shut down your system! What would you like me to do?")

    # New Casual Questions and Answers
    elif "what's your name" in command:
        speak("I am your personal assistant, designed to make your life easier and more efficient.")

    elif "tell me a joke" in command:
        speak("Why did the scarecrow win an award? Because he was outstanding in his field!")

    elif "which colour do you like" in command:
        speak("I think blue is a nice color! It’s calm and serene, just like how I aim to be when assisting you.")

    elif "how old are you" in command:
        speak("I don't have an age, but I was created recently to serve you with the best experience possible.")

    elif "can you help me with coding" in command:
        speak("Absolutely! I can help you debug, write, or explain code in several programming languages like Python, JavaScript, and more.")

    elif "what is your favorite food" in command:
        speak("I don’t need food, but I hear pizza is a favorite among many!")

    elif "what is the weather like" in command:
        speak("I currently don’t have access to weather data, but you can check by searching online or using a weather app.")

    elif "do you have feelings" in command:
        speak("I don’t have feelings, but I’m programmed to respond in a way that makes you feel like I’m your companion!")

    elif "who created you" in command:
        speak("I was created by a brilliant team of developers, designed to make your life easier.")

    else:
        speak("Command not recognized. Could you please repeat it or try a different one?")

if __name__ == "__main__":
    while True:
        command = listen_command()
        if command:
            execute_command(command)
