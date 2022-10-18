import string
from fastapi import FastAPI

from api import get_weather

app = FastAPI()


@app.get("/")
def home():
    return {"Data": "Test"}


@app.get("/weather/{city}")
def city_weather(city: str):

    response = get_weather(city)
    if not response == 1:
        data = response.json()
    else:
        data = "An error occurred"

    return data
