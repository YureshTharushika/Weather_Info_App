
import os
from dotenv import load_dotenv
import requests
import tzlocal
from datetime import datetime


load_dotenv()
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
GOOGLE_BASE_URL = "https://maps.googleapis.com/maps/api/place/"


def get_weather(city):
    url = f"{WEATHER_BASE_URL}?appid={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        return response
    else:
        return 1


# def get_place_image(lat, lon, city):
#     # placeurl = f"{GOOGLE_BASE_URL}nearbysearch/json?location={lat}%2C{lon}&radius=1500&type=city&keyword={city}&key={GOOGLE_API_KEY}"
#     # placeresponse = requests.get(placeurl)
#     # placedata = placeresponse.json()
#     # photo_reference = placedata["results"]
#     # print(placeresponse)
#     # photourl = f"{GOOGLE_BASE_URL}photo/?maxwidth=400&photo_reference={photo_reference}&key={GOOGLE_API_KEY}"
#     # photoresponse = requests.get(photourl)

#     gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
#     places_result = gmaps.places_nearby(
#         location=f"{lat},{lon}", radius=1500, type=city)
#     print(places_result)
#     return "places_result"


def get_time(dt):
    unix_timestamp = float(dt)
    local_timezone = tzlocal.get_localzone()
    local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
    return local_time.strftime("%H:%M:%S")
