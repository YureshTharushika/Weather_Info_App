
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(url)
    print(API_KEY)
    if response.status_code == 200:
        return response
    else:
        return 1
