
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init() # object creation

def speak(command):

    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 125)     # setting up new voice rate

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(command)
    engine.runAndWait()


def listen():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("-- Say something! --")
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            if command.lower() == 'exit':
                break
            else:
                print(command)
                speak(command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

if __name__ == '__main__':
    listen()
