

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import get_time, get_weather

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/weather", response_class=HTMLResponse)
def city_weather(request: Request, city: str):

    response = get_weather(city)

    if not response == 1:
        data = response.json()
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        humidity = data["main"]["humidity"]
        windspeed = data["wind"]["speed"]
        clouds = data["clouds"]["all"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        time = get_time(data["dt"])
        # photo = get_place_image(lat, lon, city)

        # f = open('Image.jpg', 'wb')

        # for chunk in photo:
        #     if chunk:
        #         f.write(chunk)
        # f.close()
    else:
        data = "An error occurred"

    return templates.TemplateResponse("result.html", {"request": request, "temperature": round(temperature-273.15, 2), "weather": weather.capitalize(), "humidity": humidity, "windspeed": windspeed, "clouds": clouds, "time": time, "icon": icon, "city": city.capitalize()})
