import re
import plotly
import plotly.express as px
from flask import Flask, render_template, request
from datetime import datetime
from weather_api import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/pm1")
def pm1():
    return render_template('pm1.html')

@app.route("/pm10")
def pm1():
    return render_template('pm10.html')

@app.route("/pm25")
def pm1():
    return render_template('pm25.html')
