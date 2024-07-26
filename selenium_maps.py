from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyttsx3
import speech_recognition as sr
from playsound import playsound
import time

engine = pyttsx3.init()

engine.setProperty('rate', 150)    

voices = engine.getProperty('voices')    
engine.setProperty('voice', voices[1].id)  

def speak_command(command):
    engine.say(command)
    engine.runAndWait()

def listen_for_command():
    r = sr.Recognizer()
    m = sr.Microphone()
    print("-- Listening! --")
    speak_command('listening')
    max_try = 2
    start = 0
    while start < max_try:
        playsound("F:\speech recognition\sound\pop_up_sound.wav")
        with m as source:
            r.adjust_for_ambient_noise(source, duration=0.8)  # Adjust for ambient noise to dynamically set the energy threshold
            audio = r.listen(source)
        try:
            command = (r.recognize_google(audio)).lower()
            return command
        except sr.UnknownValueError:
            print("Could not understand audio. Say it again")
            speak_command("Could not understand audio, say it again") 

        start += 1

    print('Maximum speech input limit exceeded.. Try again later')
    speak_command('Maximum speech input limit exceeded. Try again later')
    return None

def google_maps(query):

    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    wait = WebDriverWait(driver, 5)

    # Find the search bar and enter your search query
    search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
    search_box.send_keys(query + Keys.ENTER)

    # Wait for search results to load
    wait.until(EC.presence_of_element_located((By.ID, 'search')))

    try:
        # Wait for the directions button and click it
        directions_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="exp0"]/div[1]/a/div/div[1]')))
        if directions_button:
            directions_button.click()
        else:
            print('Could you please repeat your destination??')
            speak_command('Could you please repeat your destination')

            destination = listen_for_command()
            if destination:
                query = f'directions to {destination} on google maps'
                driver.get("https://www.google.com/")

                # Find the search bar and enter your search query
                search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
                search_box.send_keys(query + Keys.ENTER)

                try: 
                    directions_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="exp0"]/div[1]/a/div/div[1]')))
                    directions_button.click()
                except:
                    print('Could not find search results for the query')
                    speak_command('Could not find search results for the query')
    except:
        print('Could not find search results for the query')
        speak_command('Could not find search results for the query')

    while True:
        time.sleep(1)

# google_maps('directions to j w marriott on google map')





