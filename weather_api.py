import requests
import json
import os
import math
from datetime import datetime
from dotenv import load_dotenv
# from bs4 import BeautifulSoup

def get_weather_json(zipCode):
    # acquire api key
    load_dotenv() 
    APIkey=os.environ['WEATHER_APIKEY']

    # make the request 
    requestString = f'http://api.openweathermap.org/data/2.5/weather?zip={zipCode},&appid={APIkey}'
    print(requestString)

    # get response in a json format for easier data extraction
    response=requests.get(requestString).json()

    # convert from Kelvin --> Celcius --> Fahrenheit
    temp_F = math.floor((response['main']['temp'] - 273.15) * 1.8 + 32)
    feels_like_temp_F = math.floor((response['main']['feels_like'] - 273.15) * 1.8 + 32)

    # convert wind speed from m/s to mph
    wind_speed_mph = round(response['wind']['speed'] * 2.2369363, 2)

    now = datetime.now()
    # returns: [timestamp, main, description, temp, feels like, humidity, wind speed]
    return [now, 
            response['weather'][0]['main'],
            response['weather'][0]['description'],
            temp_F,
            feels_like_temp_F,
            response['main']['humidity'],
            wind_speed_mph
            ]

if __name__ == "__main__":
    print(get_weather_json(98103))