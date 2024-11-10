import sys
sys.path.insert(0, "c:\\users\\abhip\\appdata\\local\\programs\\python\\python310\\lib\\site-packages")
import SpeechRecognition 
import streamlit
import pyttsx3
import webbrowser

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_time():
    now=datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def listen():
    with sr.Microphone() as source:
        print("Listening")
        recognizer.adjust_for_ambient_noise(source)

        try:
            command=recognizer.recognize_google(audio)
            print(f"You said : {command}")
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that..")
            return ""
        except sr.RequestError:
            print("Not able to get the results now. Check your internet connection.")
            return ""
    return command.lower

def assistant():
    speak("Hello, hwo can I help you today?")

    while True:
        command=listen()
        if 'What is the time now' in command:
            current_time=get_time()
            speak(f"The current time is {get_time} ")
        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye! Have a great day!")
            break 
        else:
            print("I didn't understand that")

if __name__ == "__main__":
    assistant()