import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime 
import pyjokes
import os
import time


def sptext():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, the speech service is unavailable.")
            return None
#converting text to speech


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':


        while True:
            data1=sptext()

            if data1 is None:
            # If no valid input was received, continue listening
                time.sleep(1)
                continue

            if "your name" in data1:
                name = "my name is alina"
                speechtx(name)

            elif "old are you" in data1:
                age="i am 2 years old"
                speechtx(age)

            elif "time"in data1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(current_time)
                print(current_time)

            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "google" in data1:
                webbrowser.open("https://www.google.com/")

            elif "chatgpt" in data1:
                webbrowser.open("https://chatgpt.com/")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral") 
                print(joke_1)
                speechtx(joke_1)

            elif "play song" in data1:
                webbrowser.open("https://youtu.be/Feoea8FQTI0")

            elif "exit" in data1:
                speechtx("thankyou")
                break
            time.sleep(5)