import pandas as pd
import numpy as np

# friendly note: units are in micrograms per cubic meter

def get_pm1_last10_avg():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")
    last_ten = df.iloc[-10:]
    pm1_last10_avg = last_ten['pm1'].mean()
    print(pm1_last10_avg)
    return pm1_last10_avg

def get_pm10_last10_avg():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")
    last_ten = df.iloc[-10:]
    pm10_last10_avg = last_ten['pm10'].mean()
    print(pm10_last10_avg)
    return pm10_last10_avg

def get_pm25_last10_avg():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")
    last_ten = df.iloc[-10:]
    pm25_last10_avg = last_ten['pm25'].mean()
    print(pm25_last10_avg)
    return pm25_last10_avg

if __name__ == "__main__":
    get_pm1_last10_avg()
    get_pm10_last10_avg()
    get_pm25_last10_avg()
