import re
import plotly
import plotly.express as px
from flask import Flask, render_template, request
from datetime import datetime


# import other python files & functions
from plot_pm_data import *
from pm_stats_to_display import *
from weather_api import *
import geo_plotting


app = Flask(__name__)

@app.route("/")
def home():
    pm1_to_display = get_pm1_last10_avg()
    pm10_to_display = get_pm10_last10_avg()
    pm25_to_display = get_pm25_last10_avg()
    
    zipCode = 98103
    weather = get_weather_json(zipCode)
    print(weather)
    weather_time = weather[0]
    weather_description = weather[2]
    temperature_to_send = weather[3]
    feels_like = weather[4]
    humidity_to_send = weather[5]
    wind_speed = weather[6]
    return render_template('index.html',
                            pm1LastTenAvg = pm1_to_display,
                            pm10LastTenAvg = pm10_to_display,
                            pm25LastTenAvg = pm25_to_display,
                            weatherTime = weather_time,
                            temperature = temperature_to_send,
                            feelsLike = feels_like,
                            humidity = humidity_to_send,
                            description = weather_description,
                            windSpeed = wind_speed)

@app.route("/pm1")
def pm1():
    geo_plotting
    return render_template('pm1-map.html')

@app.route("/pm10")
def pm10():
    return render_template('pm10.html')

@app.route("/pm25")
def pm25():
    return render_template('pm25.html')
