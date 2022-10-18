

import requests


API_KEY = "a85e873a6179972729601795cb733467"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        return response
    else:
        return 1
