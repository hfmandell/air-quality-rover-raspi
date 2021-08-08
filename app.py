import re
import plotly
import plotly.express as px
from flask import Flask, render_template, request
from datetime import datetime


# import other python files & functions
from plot_pm_data import *
from pm_stats_to_display import *
from weather_api import *


app = Flask(__name__)

@app.route("/")
def home():
    pm1_to_display = get_pm1_last10_avg()
    pm10_to_display = get_pm10_last10_avg()
    pm25_to_display = get_pm25_last10_avg()
    return render_template('index.html',
                            pm1LastTenAvg = pm1_to_display,
                            pm10LastTenAvg = pm10_to_display,
                            pm25LastTenAvg = pm25_to_display)

@app.route("/pm1")
def pm1():
    return render_template('pm1.html')

@app.route("/pm10")
def pm10():
    return render_template('pm10.html')

@app.route("/pm25")
def pm25():
    return render_template('pm25.html')
