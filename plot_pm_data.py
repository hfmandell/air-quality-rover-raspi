import plotly
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import interactive
from dateutil.parser import parse
#interactive(True)

def plot_all_pm_timeseries():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")

    #create separate columns for date objects
    df['date'] = [parse(date).date() for date in df['timestamp']]
    df['year'] = pd.to_datetime(df['date']).dt.to_period("Y")
    df['month'] = pd.to_datetime(df['date']).dt.strftime("%m")
    df['day'] = pd.to_datetime(df['date']).dt.strftime("%d")
    df['time'] = [parse(time).time() for time in df['timestamp']]
    df['hour'] = [parse(hour).time() for hour in df['timestamp']]
    df['minute'] = [parse(minute).time() for minute in df['timestamp']]

    x = np.array(df['timestamp'])

    print(df)

    colors = [(31/255, 119/255, 180/255),
              (174/255, 199/255, 232/255),
              (158/255, 218/255, 229/255)]

    plt.plot(df['timestamp'],df['pm1'], alpha=0.75, color=colors[0])
    y_pos_pm1 = df['pm1'].values[-1] - 0.5    
    plt.text('2021-07-29', y_pos_pm1, s = "PM1", fontsize=14, color=colors[0])    

    plt.plot(df['timestamp'],df['pm10'], alpha=0.75, color=colors[1])
    y_pos_pm10 = df['pm10'].values[-1] - 0.5    
    plt.text('2021-07-29', y_pos_pm10, s = "PM10", fontsize=14, color=colors[1])     

    plt.plot(df['timestamp'],df['pm25'], alpha=0.75, color=colors[2])
    y_pos_pm25 = df['pm25'].values[-1] - 0.5    
    plt.text('2021-07-29', y_pos_pm25,s = "PM25", fontsize=14, color=colors[2])  

    # Title & Axes
    plt.title("Particulate Matter")
    plt.xlabel("Date", labelpad=15, fontsize=12, color="#333533")
    plt.ylabel("PM (ppm)", labelpad=15, fontsize=12, color="#333533")
    #   plt.xticks(20, fontsize=14)

    # Remove the plot frame lines. They are unnecessary chartjunk.  
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False) 
    
    # Ensure that the axis ticks only show up on the bottom and left of the plot.    
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()

    #ax.xaxis_date()

    plt.show()


def plot_pm1_timeseries():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")

    #create separate columns for date objects
    df['date'] = [parse(date).date() for date in df['timestamp']]
    df['year'] = pd.to_datetime(df['date']).dt.to_period("Y")
    df['month'] = pd.to_datetime(df['date']).dt.strftime("%m")
    df['day'] = pd.to_datetime(df['date']).dt.strftime("%d")
    df['time'] = [parse(time).time() for time in df['timestamp']]
    df['hour'] = [parse(hour).time() for hour in df['timestamp']]
    df['minute'] = [parse(minute).time() for minute in df['timestamp']]

    x = np.array(df['timestamp'])

    print(df)

    colors = (31/255, 119/255, 180/255)

    plt.plot(df['timestamp'],df['pm1'], alpha=0.75, color=colors)
    y_pos_pm1 = df['pm1'].values[-1] - 0.5    
    plt.text('2021-07-29', y_pos_pm1, s = "PM1", fontsize=14, color=colors)     

    # Title & Axes
    plt.title("Particulate Matter")
    plt.xlabel("Date", labelpad=15, fontsize=12, color="#333533")
    plt.ylabel("PM (ppm)", labelpad=15, fontsize=12, color="#333533")
    #   plt.xticks(20, fontsize=14)

    # Remove the plot frame lines. They are unnecessary chartjunk.  
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False) 
    
    # Ensure that the axis ticks only show up on the bottom and left of the plot.    
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()

    ax.xaxis_date()

    plt.show()

def plot_pm10_timeseries():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")

    #create separate columns for date objects
    df['date'] = [parse(date).date() for date in df['timestamp']]
    df['year'] = pd.to_datetime(df['date']).dt.to_period("Y")
    df['month'] = pd.to_datetime(df['date']).dt.strftime("%m")
    df['day'] = pd.to_datetime(df['date']).dt.strftime("%d")
    df['time'] = [parse(time).time() for time in df['timestamp']]
    df['hour'] = [parse(hour).time() for hour in df['timestamp']]
    df['minute'] = [parse(minute).time() for minute in df['timestamp']]

    x = np.array(df['timestamp'])

    print(df)

    colors = (174/255, 199/255, 232/255)  

    plt.plot(df['timestamp'],df['pm10'], alpha=0.75, color=colors)
    y_pos_pm10 = df['pm10'].values[-1] - 0.5    
    plt.text('2021-07-29', y_pos_pm10, s = "PM10", fontsize=14, color=colors)     
 

    # Title & Axes
    plt.title("Particulate Matter")
    plt.xlabel("Date", labelpad=15, fontsize=12, color="#333533")
    plt.ylabel("PM (ppm)", labelpad=15, fontsize=12, color="#333533")
    #   plt.xticks(20, fontsize=14)

    # Remove the plot frame lines. They are unnecessary chartjunk.  
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False) 
    
    # Ensure that the axis ticks only show up on the bottom and left of the plot.    
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()

    ax.xaxis_date()

    plt.show()

def plot_pm25_timeseries():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")

    #create separate columns for date objects
    df['date'] = [parse(date).date() for date in df['timestamp']]
    df['year'] = pd.to_datetime(df['date']).dt.to_period("Y")
    df['month'] = pd.to_datetime(df['date']).dt.strftime("%m")
    df['day'] = pd.to_datetime(df['date']).dt.strftime("%d")
    df['time'] = [parse(time).time() for time in df['timestamp']]
    df['hour'] = [parse(hour).time() for hour in df['timestamp']]
    df['minute'] = [parse(minute).time() for minute in df['timestamp']]

    x = np.array(df['timestamp'])

    print(df)

    colors = (158/255, 218/255, 229/255)

    plt.plot(df['timestamp'],df['pm25'], alpha=0.75, color=colors)
    y_pos_pm25 = df['pm25'].values[-1] - 0.5    
    plt.text('2021-07-29', y_pos_pm25,s = "PM25", fontsize=14, color=colors)  

    # Title & Axes
    plt.title("Particulate Matter")
    plt.xlabel("Date", labelpad=15, fontsize=12, color="#333533")
    plt.ylabel("PM (ppm)", labelpad=15, fontsize=12, color="#333533")
    #   plt.xticks(20, fontsize=14)

    # Remove the plot frame lines. They are unnecessary chartjunk.  
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False) 
    
    # Ensure that the axis ticks only show up on the bottom and left of the plot.    
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()

    ax.xaxis_date()

    plt.show()

if __name__ == "__main__":
    plot_all_pm_timeseries()
#     file_in = 'data/processed/airquality_data_to_use.csv'
#     pass