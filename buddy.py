
import speech_recognition as sr
import pyttsx3
import pywhatkit as pk
import datetime

engine = pyttsx3.init() # engine is an object created using pyttsx3.init()

def speak_command(command):

    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 175)     # setting up new voice rate

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    # Voice ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0, 
    # Name: Microsoft Zira Desktop - English (United States) 

    engine.say(command)
    engine.runAndWait()

def play(command):
    song_name = command.replace('play', '')
    print(f'Playing {song_name} on youtube')
    speak_command(f'Playing {song_name} on youtube')
    pk.playonyt(song_name)

def time():
    current_time = datetime.datetime.now().strftime('%I:%M')
    print(f'The current time is {current_time}')
    speak_command((f'The current time is {current_time}'))

def date():
    todays_date = datetime.datetime.now().strftime('%d %B')
    day = todays_date.split()[0]
    month = todays_date.split()[1]
    dict = {1:'st', 2:'nd', 3:'rd'}
    last_digit = day[-1]
    suffix = dict.get(last_digit, 'th')
    print(f'Today is {day}{suffix} of {month}')
    speak_command((f'Today is {day}{suffix} of {month}'))

def listen_for_command():
    r = sr.Recognizer()
    while True:
        print("-- Listening! --")
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            command = (r.recognize_google(audio)).lower()
            if 'wake' in command or 'hello' in command or 'hi' in command:
                print('Hello.!! How can I help you??')
                speak_command('Hello, How can I help you')
                continue
            elif 'play' in command:
                play(command)
                break
            elif 'time' in command:
                time()
                break
            elif 'date' in command:
                date()
                break
            elif 'exit' in command:
                break
            else:
                print('I didnt understand that.. Please try again.!!')
                speak_command('I didnt understand that. Please try again.')
        except sr.UnknownValueError:
            print("Could not understand audio\nSay it again")
            speak_command("Could not understand audio, say it again")                                                          
        except sr.RequestError as e:
            print("Could not request results\nTry again; {0}".format(e))
            speak_command("Could not request results, try again; {0}".format(e))


if __name__ == '__main__':
    listen_for_command()

