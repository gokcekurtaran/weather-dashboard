from django.shortcuts import render
import requests
from datetime import datetime


def home(request):
    city = request.GET.get('city')
    weather_data = None

    if city:
        api_key = "8e2df2d90dccb36cf314988083d55336"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            weather_data = {
                "city": data["name"],
                "temperature": round(data["main"]["temp"]),
                "feels_like": round(data["main"]["feels_like"]),
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "description": data["weather"][0]["description"],
                "time": datetime.now().strftime("%H:%M"),
            }

    return render(request, 'weather/home.html', {
        "weather": weather_data
    })