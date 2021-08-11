import plotly
import plotly.express as px
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib import interactive
from dateutil.parser import parse
from datetime import datetime

def get_last_date():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")
    end_date = df['timestamp'].values[-1:]
    if type(end_date) == np.ndarray:
        end_date = end_date[0]
    end_date = end_date[:10]
    return end_date

# def get_first_date():
#     df = pd.read_csv("data/processed/airquality_data_to_use.csv")
#     first_date = df['timestamp'].values[0]
#     first_date  = first_date [:10]
#     return end_date

def plot_all_pm_timeseries():
    # plotly!
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")
    df = df.drop('pm1_cf', 1)
    df = df.drop('pm25_cf', 1)
    df = df.drop('pm10_cf', 1)
    fig = px.line(df, x='timestamp', y=df.columns,#y='pm1',
                  hover_data={"timestamp": "|%B %d, %Y, %-I:%M:%S %p"},
                  title = "All PM Measurements")
                  # to do a custom date range:
                #   range_x=['2016-07-01','2016-12-31'])
    # print(fig)
    fig.update_xaxes(
        #dtick="D7",
        #tickformat="%b %d\n%Y",
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1 hour", step="hour", stepmode="backward"),
                dict(count=1, label="1 day", step="day", stepmode="backward"),
                dict(count=7, label="1 week", step="day", stepmode="backward"),
                dict(count=1, label="1 month", step="month", stepmode="backward"),
                dict(count=1, label="1 year", step="year", stepmode="backward"),
                dict(count=1, label="YTD", step="all", stepmode="todate"),
                dict(step="all")
            ])
        ),
        tickformatstops = [
            dict(dtickrange=[None, 1000], value="%-I:%M:%S%p\n%b %d"),
            dict(dtickrange=[1000, 60000], value="%-I:%M:%S%p\n%b %d"),
            dict(dtickrange=[60000, 3600000], value="%-I:%M%p\n%b %d"),
            dict(dtickrange=[3600000, 86400000], value="%-I:%M%p"),
            dict(dtickrange=[86400000, 604800000], value="%b %d"),
            dict(dtickrange=[604800000, "M1"], value="%b %d"),
            dict(dtickrange=["M1", "M12"], value="%b %d\n%Y"),
            dict(dtickrange=["M12", None], value="%Y")
        ]
    )
    # fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def plot_all_pm_timeseries_orig():
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")

    #create separate columns for date objects
    df['date'] = [parse(date).date() for date in df['timestamp']]
    df['year'] = pd.to_datetime(df['date']).dt.to_period("Y")
    df['month'] = pd.to_datetime(df['date']).dt.strftime("%m")
    df['day'] = pd.to_datetime(df['date']).dt.strftime("%d")
    df['time'] = [parse(time).time() for time in df['timestamp']]
    df['hour'] = [parse(hour).time() for hour in df['timestamp']]
    df['minute'] = [parse(minute).time() for minute in df['timestamp']]

    timestamps = df['timestamp'].to_list()
    df['timestamps_dt'] = [(datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")) for date in timestamps]
    timestamps_dt = df['timestamps_dt'].tolist()
    #xs = mdates.date2num(df['timestamps_dt'].tolist())
    #x_format = mdates.DateFormatter('%Y-%m-%d\n%H:%M:%S')

    # print(df['timestamps_dt'])
    # x_axis_dates = [(date.strftime(' %b %-d %-I %p')) for date in timestamps_dt]


    # print(xs)

    colors = [(31/255, 119/255, 180/255),
              (174/255, 199/255, 232/255),
              (158/255, 218/255, 229/255)]

    # fig, ax = plt.subplots(figsize=(12, 8))
    # ax.plot(xs,
    #         df['pm1'].values,
    #         '-',
    #         color=colors[0])
    # ax.plot(xs,
    #         df['pm25'].values,
    #         '-',
    #         color=colors[1])
    # ax.plot(xs,
    #         df['pm10'].values,
    #         '-',
    #         color=colors[2])
    # ax.set(xlabel="Date of Measure", ylabel="PM Levels (μg/m³)",
    #     title="Particulate Matter \nAll Time")

    # Format the x axis
    # ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
    # ax.xaxis.set_minor_formatter(DateFormatter("%H %p"))
    #ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
    # ax.xaxis.set_major_formatter(x_format)

    # fig = plt.gcf()
    # plt.show()
    # plt.draw()
    # fig.savefig('pm_plots/all3_plot.png')

    plt.plot(df['timestamp'],df['pm1'], alpha=0.75, color='#800080',
                    linestyle='solid')
    y_pos_pm1 = df['pm1'].values[-1] - 0.5    
    plt.text(get_last_date(), y_pos_pm1, s = "PM1", fontsize=14, color='#800080')    

    plt.plot(df['timestamp'],df['pm10'], alpha=0.75, color='#0000FF',
                    linestyle='solid')
    y_pos_pm10 = df['pm10'].values[-1] + 0.5    
    plt.text(get_last_date(), y_pos_pm10, s = "PM10", fontsize=14, color='#0000FF')     

    plt.plot(df['timestamp'],df['pm25'], alpha=0.75, color='#008080',
                    linestyle='solid')
    y_pos_pm25 = df['pm25'].values[-1] - 0.5    
    plt.text(get_last_date(), y_pos_pm25,s = "PM2.5", fontsize=14, color='#008080')  

    # Title & Axes
    plt.title("Particulate Matter")
    plt.xlabel("Date", labelpad=15, fontsize=12, color="#333533")
    plt.ylabel("PM (ppm)", labelpad=15, fontsize=12, color="#333533")
    #   plt.xticks(20, fontsize=14)

    # Remove the plot frame lines. They are unnecessary chartjunk.  
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(True)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(True) 


    # Format the x axis
    # ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
    # ax.xaxis.set_minor_formatter(DateFormatter("%H %p"))
    # ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
    # ax.xaxis.set_major_formatter('%b-%d')

    # timestamps = df['timestamp'].to_list()
    # timestamps_dt = [(datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")) for date in timestamps]
    # x_axis_dates = [(date.strftime(' %b %-d %-I %p')) for date in timestamps_dt]
    # print(x_axis_dates)

    # plt.xticks(ticks = timestamps, lables = x_axis_dates)



    # helper function for the formatter
    # def listifed_formatter(x, pos=None):
    #     try:
    #         return x_axis_dates[int(x)]
    #     except IndexError:
    #         return ''

    # # make and use the formatter
    # mt = mticker.FuncFormatter(listifed_formatter)
    # ax.xaxis.set_major_formatter(mt)

    # # set the default ticker to only put ticks on the integers
    # loc = ax.xaxis.get_major_locator()
    # loc.set_params(integer=True)

    # # rotate the labels
    # [lab.set_rotation(30) for lab in ax.get_xticklabels()]

    #ax.xaxis_date()
    fig = plt.gcf()
    plt.gcf().autofmt_xdate
    plt.show()
    # plt.draw()
    # fig.savefig('pm_plots/all3_plot.png')
    


def plot_pm_timeseries(pm_size):
    df = pd.read_csv("data/processed/airquality_data_to_use.csv")

    #create separate columns for date objects
    df['date'] = [parse(date).date() for date in df['timestamp']]
    df['year'] = pd.to_datetime(df['date']).dt.to_period("Y")
    df['month'] = pd.to_datetime(df['date']).dt.strftime("%m")
    df['day'] = pd.to_datetime(df['date']).dt.strftime("%d")
    df['time'] = [parse(time).time() for time in df['timestamp']]
    df['hour'] = [parse(hour).time() for hour in df['timestamp']]
    df['minute'] = [parse(minute).time() for minute in df['timestamp']]

    if pm_size == "pm1":
        print("pm1")
        colors = (31/255, 119/255, 180/255)
    elif pm_size == "pm25":
        print("pm25")
        colors = (158/255, 218/255, 229/255)
    else:  # pm10
        print("pm10")
        colors = (174/255, 199/255, 232/255)  

    plt.plot(df['timestamp'],df[pm_size], alpha=0.75, color=colors)
    y_pos = df[pm_size].values[-1] - 0.5    
    plt.text(get_last_date(), y_pos,s = pm_size.upper(), fontsize=14, color=colors)  

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

    plt.savefig("pm_plots/" + pm_size + "_plot.png")

if __name__ == "__main__":
    #get_last_date()
    plot_all_pm_timeseries()
    # plot_pm_timeseries('pm1')
#     file_in = 'data/processed/airquality_data_to_use.csv'
#     pass