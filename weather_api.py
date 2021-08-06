import requests
import json
import os
from dotenv import load_dotenv

#def get_weather_json(zipCode):
def get_weather_json():
    zipCode=98103
    countryCode='us'
    load_dotenv() 
    APIkey=os.environ['WEATHER_APIKEY']

    requestString = f'http://api.openweathermap.org/data/2.5/weather?zip={zipCode},&appid={APIkey}'
    print(requestString)

    response=requests.get(requestString)
    print(response)

    # returns in json format
    return response

""" example output
 {
     "coord": {"lon": -122.08,"lat": 37.39},
     "weather": [
       {
         "id": 800,
         "main": "Clear",
         "description": "clear sky",
         "icon": "01d"
       }
     ],
     "base": "stations",
     "main": {
       "temp": 282.55,
       "feels_like": 281.86,
       "temp_min": 280.37,
       "temp_max": 284.26,
       "pressure": 1023,
       "humidity": 100
     },
     "visibility": 16093,
     "wind": {
       "speed": 1.5,
       "deg": 350
     },
     "clouds": {
       "all": 1
     },
     "dt": 1560350645,
     "sys": {
       "type": 1,
       "id": 5122,
       "message": 0.0139,
       "country": "US",
       "sunrise": 1560343627,
       "sunset": 1560396563
     },
     "timezone": -25200,
     "id": 420006353,
     "name": "Mountain View",
     "cod": 200
     }
"""

"""
coord
    coord.lon City geo location, longitude
    coord.lat City geo location, latitude
weather (more info Weather condition codes)
    weather.id Weather condition id
    weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
    weather.description Weather condition within the group. You can get the output in your language. Learn more
    weather.icon Weather icon id
base Internal parameter
main
    main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    main.feels_like Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    main.pressure Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
    main.humidity Humidity, %
    main.temp_min Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    main.temp_max Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
    main.sea_level Atmospheric pressure on the sea level, hPa
    main.grnd_level Atmospheric pressure on the ground level, hPa
wind
    wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
    wind.deg Wind direction, degrees (meteorological)
    wind.gust Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
clouds
    clouds.all Cloudiness, %
rain
    rain.1h Rain volume for the last 1 hour, mm
    rain.3h Rain volume for the last 3 hours, mm
snow
    snow.1h Snow volume for the last 1 hour, mm
    snow.3h Snow volume for the last 3 hours, mm
dt Time of data calculation, unix, UTC
sys
    sys.type Internal parameter
    sys.id Internal parameter
    sys.message Internal parameter
    sys.country Country code (GB, JP etc.)
    sys.sunrise Sunrise time, unix, UTC
    sys.sunset Sunset time, unix, UTC
timezone Shift in seconds from UTC
id City ID
name City name
cod Internal parameter
"""

if __name__ == "__main__":
    raw_file_in = 'data/processed/airquality_data_to_use.csv'
    main(raw_file_in)