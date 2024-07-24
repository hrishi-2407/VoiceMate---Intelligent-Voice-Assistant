import requests

def weather_indicator(city):

    API_key = 'YOUR-API-KEY'
    url = f'https://api.weatherapi.com/v1/current.json?key={API_key}&q={city}'

    r = requests.get(url)
    dict1 = r.json()

    temperature = dict1['current']['temp_c']
    weather = dict1['current']['condition']['text']

    stats = f'The current temperature of {city} is {temperature} degree and the weather is {weather}'
    return stats



