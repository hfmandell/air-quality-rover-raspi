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
                            windSpeed = wind_speed
                            )

@app.route("/pm1")
def pm1():
    pm_size = 'pm1'
    most_recent_pm = most_recent_pm_reading(pm_size)
    last_hour = pm_last_hr_avg(pm_size)
    last_day = pm_last_day_avg(pm_size)
    last_week = pm_last_week_avg(pm_size)
    all_time = pm_all_time_avg(pm_size)
    return render_template('pm1.html',
                            mostRecent = most_recent_pm,
                            lastHour=last_hour, lastDay=last_day, lastWeek=last_week, allTime= all_time)

@app.route("/pm1-map.html")
def pm1_map():
    geo_plotting.plot_pm_and_gps("pm1")
    return render_template('pm1-map.html')

@app.route("/pm25")
def pm25():
    pm_size = 'pm25'
    most_recent_pm = most_recent_pm_reading(pm_size)
    last_hour = pm_last_hr_avg(pm_size)
    last_day = pm_last_day_avg(pm_size)
    last_week = pm_last_week_avg(pm_size)
    all_time = pm_all_time_avg(pm_size)
    return render_template('pm25.html',
                            mostRecent = most_recent_pm,
                            lastHour=last_hour, lastDay=last_day, lastWeek=last_week, allTime= all_time)

@app.route("/pm25-map.html")
def pm25_map():
    geo_plotting.plot_pm_and_gps("pm25")
    return render_template('pm25-map.html')

@app.route("/pm10")
def pm10():
    pm_size = 'pm10'
    most_recent_pm = most_recent_pm_reading(pm_size)
    last_hour = pm_last_hr_avg(pm_size)
    last_day = pm_last_day_avg(pm_size)
    last_week = pm_last_week_avg(pm_size)
    all_time = pm_all_time_avg(pm_size)
    return render_template('pm10.html',
                            mostRecent = most_recent_pm,
                            lastHour=last_hour, lastDay=last_day, lastWeek=last_week, allTime= all_time)

@app.route("/pm10-map.html")
def pm10_map():
    geo_plotting.plot_pm_and_gps("pm10")
    return render_template('pm10-map.html')

@app.route("/what_is_pm")
def what_is_pm():
    return render_template('/what_is_pm.html')

@app.route("/env_justice")
def env_justice():
    return render_template('/env_justice.html')

@app.route("/future_applications")
def future_applications():
    return render_template('/future_applications.html')

