import speech_recognition as sr
import webbrowser
import pyttsx3  # used for text to speech converter

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text="No Text Given"):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak('Initializing Jarvis....')
    # Listen for the word "Jarvis"
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                """
                timeout waits the given amount of seconds until an error appears
                phrase_time_limit waits for the amount of seconds before converting
                """
                audio = recognizer.listen(source)  
                print("Recognizing...")
            word = recognizer.recognize_google(audio)
          
            print(word)
            if("jarvis" in word.lower()):
                speak("Ya")
                print("Jarvis Active")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    command_audio = recognizer.listen(source)  
                    print("Recognizing...")
                    command_text = recognizer.recognize_google(command_audio)
                    print(command_text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand audio")
        except sr.RequestError:
            print("Could not request results, check your internet connection")
