import speech_recognition as sr
import webbrowser
import pyttsx3# used for text to speech converter
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text="No Text Given"):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak('initializing jarvis....')
    # Listen for the word "Jarvis"
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                print("You said: ", text)
            except sr.UnknownValueError:
                print("Sorry, I could not understand audio")

