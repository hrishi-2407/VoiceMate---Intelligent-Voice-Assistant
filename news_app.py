
import requests
import json

def news_headlines():
    API_key = 'YOUR-API-KEY'
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey=6d31aeddf05e4e34a4950fb285e83bec'

    r = requests.get(url)
    dict1 = json.loads(r.text)

    titles = []
    for i in range(5):
        titles.append(dict1['articles'][i]['title'])

    return titles






