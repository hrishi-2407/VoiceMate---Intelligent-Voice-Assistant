
import speech_recognition as sr
import pyttsx3
# import pywhatkit as pk
import datetime
import pyjokes
# import config
from playsound import playsound
from youtube_automation import poyt
from selenium_google import google_search
from weather_app import weather_indicator
from selenium_maps import google_maps
from news_app import news_headlines

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

# def play(command):
#     song_name = command.replace('play', '')
#     print(f'Playing {song_name} on youtube')
#     speak_command(f'Playing {song_name} on youtube')
#     pk.playonyt(command)
def play(command):
    poyt(topic=command)

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

def google_search_command(command):
    query = command.replace('what are', '')
    print('Searching.!!')
    speak_command('searching')
    info = google_search(query)
    print(info)
    speak_command(info)

def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak_command(joke)

def weather(command):
    command_list = command.split(' ')
    if command_list[-1] != 'city':
        city = command_list[-1]
    else:
        city = command_list[-2]
    conditions = weather_indicator(city)
    print(conditions)
    speak_command(conditions)

def news():
    news_list = news_headlines()
    for news in news_list:
        print(news)
        speak_command(news)
        
def listen_for_command():
    r = sr.Recognizer()
    m = sr.Microphone()
    print("-- Listening! --")
    speak_command('listening')
    while True:
        playsound("F:\speech recognition\sound\pop_up_sound.wav")
        with m as source:
            r.energy_threshold  # Initial energy threshold before adjustment
            r.adjust_for_ambient_noise(source, duration=0.8)  # Adjust for ambient noise to dynamically set the energy threshold
            r.energy_threshold  # Adjusted energy threshold

            audio = r.listen(source)
        try:
            command = (r.recognize_google(audio)).lower()
            if any(keyword in command for keyword in ['wake', 'hello', 'hi', 'hey']):
                print('Hello.!! How can I help you??')
                speak_command('Hello, How can I help you')
                # continue  # --> error
            elif 'time' in command:
                time()
            elif 'date' in command:
                date()
            elif 'joke' in command:
                jokes()
            elif any(keyword in command for keyword in ['current', 'weather', 'whether', 'temperature', 'climate', 'conditions']):
                weather(command)
            elif 'play' in command:
                play(command)
                break
            elif any(keyword in command for keyword in ['what', 'give', 'info', 'information', 'who', 'how', 'search', 'find', 'tell']):
                google_search_command(command)
            elif any(keyword in command for keyword in ['directions', 'direction', 'take', 'route', 'root']):
                google_maps(command)
                break
            elif any(keyword in command for keyword in ['news', 'breaking', 'headline', 'headlines']):
                news()
            elif 'exit' in command:
                break
            else:
                print('I didnt understand that.. Please try again.!!')
                speak_command('I didnt understand that. Please try again.')
        except sr.UnknownValueError:
            print("Could not understand audio. Say it again")
            speak_command("Could not understand audio, say it again")                                                          
        except sr.RequestError as e:
            print("Could not request results. Try again; {0}".format(e))
            speak_command("Could not request results, try again; {0}".format(e))


if __name__ == '__main__':
    listen_for_command()

