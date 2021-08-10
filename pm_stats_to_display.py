import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import geo_plotting

# friendly note: units are in micrograms per cubic meter
def get_first_and_last_dates():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")
    start_date = df['timestamp'].values[0]
    end_date = df['timestamp'].values[-1:]
    if type(end_date == np.ndarray):
        end_date = end_date[0]
    return [start_date, end_date]

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

def pm_last_hr_avg(pm_size):
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")

    last_date = get_first_and_last_dates()[1]
    last_date_dt = datetime.strptime(last_date[:-7], "%Y-%m-%d %H:%M:%S")
    last_hour_date_time = last_date_dt - timedelta(hours = 1)

    df['timestamp_dt'] = df['timestamp'].apply(lambda x: datetime.strptime(x[:-7], "%Y-%m-%d %H:%M:%S"))
    
    mask = (df['timestamp_dt'] > last_hour_date_time) & (df['timestamp_dt'] <= df['timestamp_dt'])
    df_last_hr = pd.DataFrame()
    df_last_hr = df[mask]

    avg_pm_last_hr = df_last_hr[pm_size].mean().round(2)
    return avg_pm_last_hr
    
def pm_last_day_avg(pm_size):
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")

    last_date = get_first_and_last_dates()[1]
    last_date_dt = datetime.strptime(last_date[:-7], "%Y-%m-%d %H:%M:%S")
    last_day_date_time = last_date_dt - timedelta(days = 1)

    df['timestamp_dt'] = df['timestamp'].apply(lambda x: datetime.strptime(x[:-7], "%Y-%m-%d %H:%M:%S"))
    
    mask = (df['timestamp_dt'] > last_day_date_time) & (df['timestamp_dt'] <= df['timestamp_dt'])
    df_last_day = pd.DataFrame()
    df_last_day = df[mask]

    avg_pm_last_day = df_last_day[pm_size].mean().round(2)
    return avg_pm_last_day

def pm_last_week_avg(pm_size):
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")

    last_date = get_first_and_last_dates()[1]
    last_date_dt = datetime.strptime(last_date[:-7], "%Y-%m-%d %H:%M:%S")
    last_week_date_time = last_date_dt - timedelta(weeks = 1)

    df['timestamp_dt'] = df['timestamp'].apply(lambda x: datetime.strptime(x[:-7], "%Y-%m-%d %H:%M:%S"))
    
    mask = (df['timestamp_dt'] > last_week_date_time) & (df['timestamp_dt'] <= df['timestamp_dt'])
    df_last_week = pd.DataFrame()
    df_last_week = df[mask]

    avg_pm_last_week = df_last_week[pm_size].mean().round(2)
    return avg_pm_last_week

def pm_all_time_avg(pm_size):
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")
    avg_pm_all_time = df[pm_size].mean().round(2)
    return avg_pm_all_time


if __name__ == "__main__":
    pm_all_time_avg('pm1')
