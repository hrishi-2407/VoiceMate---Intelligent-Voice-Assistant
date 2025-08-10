
import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
from config import SOUND_FILE_PATH
import simpleaudio as sa
from youtube_automation import poyt
from selenium_google import google_search
from weather_app import weather_indicator
from selenium_maps import google_maps
from news_app import news_headlines
# import wikipedia
# import webbrowser
import time
import os

# Initialize TTS engine with error handling
try:
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    
    voices = engine.getProperty('voices')
    if voices and len(voices) > 1:
        engine.setProperty('voice', voices[1].id)  # Female voice
    else:
        print("Warning: Female voice not available, using default")
except Exception as e:
    print(f"TTS initialization error: {e}")
    engine = None  #changing index, changes voices. 1 for female
# Voice ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0, 
# Name: Microsoft Zira Desktop - English (United States)
def speak_command(command):
    """Text-to-speech with error handling"""
    if engine:
        try:
            engine.say(command)
            engine.runAndWait()
        except Exception as e:
            print(f"TTS Error: {e}")
    else:
        print(f"[TTS DISABLED] Would say: {command}")

def play_notification_sound():
    """Play notification sound with robust error handling"""
    try:
        if not os.path.exists(SOUND_FILE_PATH):
            print(f"Sound file not found: {SOUND_FILE_PATH}")
            return False
        
        if not SOUND_FILE_PATH.lower().endswith('.wav'):
            print("Sound file must be WAV format")
            return False
            
        wave_obj = sa.WaveObject.from_wave_file(SOUND_FILE_PATH)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        return True
        
    except Exception as e:
        print(f"Sound notification error: {e}")
        return False
def play(command):
    poyt(topic=command)

def time_now():
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
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("-- Listening! --")
    speak_command('listening')

    try:
        with microphone as source:
            print("Calibrating microphone...")
            recognizer.energy_threshold  # Initial energy threshold before adjustment
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise to dynamically set the energy threshold
            recognizer.energy_threshold  # Adjusted energy threshold
        i = 0
        while i < 5:
            with microphone as source:
                print("SPEAK NOW =============")
                audio = recognizer.listen(source)
                time.sleep(1)

            try:
                test_command = recognizer.recognize_google(audio) #type: ignore
                print(f"Heard: {test_command}")
                command = test_command.lower()

            except sr.UnknownValueError:
                print("Could not understand audio. Say it again.")
                speak_command("Could not understand audio, say it again.")
                continue
            except sr.RequestError as e:
                print(f"Could not request results: {e}")
                speak_command("Could not request results, try again.")
                continue

            if any(keyword in command for keyword in ['wake', 'hello', 'hi', 'hey']):
                print('Hello.!! How can I help you??')
                speak_command('Hello, How can I help you')
                # continue  # --> error
            elif 'time' in command:
                time_now()
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


    except Exception as e:
        print(f"Microphone error: {e}")
        speak_command("Microphone error occurred.")

if __name__ == '__main__':
    listen_for_command()
