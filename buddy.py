
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    command = r.recognize_google(audio)

def audio_transcribe():
    try:
        print(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

import pyttsx3

def text_to_audio(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

audio_transcribe()
text_to_audio(command)

