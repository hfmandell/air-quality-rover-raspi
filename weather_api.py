import requests
import json
import os
import math
from datetime import datetime
from dotenv import load_dotenv
# from bs4 import BeautifulSoup

def get_weather_json(zipCode):
    # acquire api keys for aqi and weather
    load_dotenv() 
    # AQIAPIkey = os.environ['AIRQUALITY_APIKEY']
    APIkey=os.environ['WEATHER_APIKEY']

    # make the request 
    # aqi_requestString = f'https://api.waqi.info/feed/seattle?token={AQIAPIkey}'
    requestString = f'http://api.openweathermap.org/data/2.5/weather?zip={zipCode},&appid={APIkey}'


    # get response in a json format for easier data extraction
    # aqi_response=requests.get(aqi_requestString).json()
    response=requests.get(requestString).json()

    # get AQI stat
    # aqi = aqi_response['data']['aqi']

    # move onto weather data:
    # convert from Kelvin --> Celcius --> Fahrenheit
    temp_F = math.floor((response['main']['temp'] - 273.15) * 1.8 + 32)
    feels_like_temp_F = math.floor((response['main']['feels_like'] - 273.15) * 1.8 + 32)

    # convert wind speed from m/s to mph
    wind_speed_mph = round(response['wind']['speed'] * 2.2369363, 2)

    # convert the timestamp to an easily readible string for the home page
    now = datetime.now()

    month_num = now.month
    datetime_month = datetime.strptime(str(month_num), "%m")
    month_name = datetime_month.strftime("%B")

    day = now.day
    year = now.year
    hour = now.hour

    suffix = "AM"
    if hour > 12:
        hour = hour - 12
        suffix = "PM"

    minute = now.minute
    if minute < 10:
        minute = "0" + str(minute)

    time = f'{month_name} {day}, {year},  {hour}:{minute} {suffix}'

    # returns: [timestamp, main, description, temp, feels like, humidity, wind speed]
    return [time, 
            response['weather'][0]['main'],
            response['weather'][0]['description'],
            temp_F,
            feels_like_temp_F,
            response['main']['humidity'],
            wind_speed_mph #,
            # aqi
            ]

if __name__ == "__main__":
    print(get_weather_json(91711))