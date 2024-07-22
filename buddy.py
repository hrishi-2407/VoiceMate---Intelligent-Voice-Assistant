
import speech_recognition as sr
import pyttsx3
import pywhatkit as pk
import datetime
import wikipedia
import pyjokes
from playsound import playsound

engine = pyttsx3.init() # engine is an object created using pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
# Voice ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0, 
# Name: Microsoft Zira Desktop - English (United States)

def speak_command(command):
    engine.say(command)
    engine.runAndWait()

def play(command):
    song_name = command.replace('play', '')
    print(f'Playing {song_name} on youtube')
    speak_command(f'Playing {song_name} on youtube')
    pk.playonyt(song_name)

def google_search(command):
    pk.search(command)
    print(f'Searching.. {command}')
    speak_command(f'Searching.. {command}')

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

def wiki_info(command):
    query = command.replace('give me some information about', '')
    print(f'Retrieving information about {query} from wikipedia')
    speak_command(f'retrieving information about {query} from wikipedia')
    try:
        info = wikipedia.summary(query, sentences=2)
        print(info)
        speak_command(info)
    except wikipedia.exceptions.PageError:
        print(f"Sorry, couldn't find information about {query} on Wikipedia.")
        speak_command(f"Sorry, couldn't find information about {query} on Wikipedia.")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Wikipedia found multiple results for {query}. Here are a few possible options:")
        speak_command(f"Wikipedia found multiple results for {query}. Here are a few possible options:")
        for option in e.options[:3]:  # Display up to 3 options
            print(option)
            speak_command(option)

def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak_command(joke)

def listen_for_command():
    r = sr.Recognizer()
    while True:
        print("-- Listening! --")
        playsound("F:\speech recognition\pop_up_sound.wav")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            audio = r.listen(source)
        try:
            command = (r.recognize_google(audio)).lower()
            if 'wake' in command or 'hello' in command:
                print('Hello.!! How can I help you??')
                speak_command('Hello, How can I help you')
                # continue  # --> error
            elif 'play' in command:
                play(command)
                break
            elif 'how' in command:
                google_search(command)
            elif 'time' in command:
                time()
                # break
            elif 'date' in command:
                date()
                # break
            elif 'give' in command:
                wiki_info(command)
                # break
            elif 'joke' in command:
                jokes()
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

