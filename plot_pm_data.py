import plotly
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
from dateutil.parser import parse
#interactive(True)

df = pd.read_csv("data/processed/airquality_data_to_use.csv")

#create separate columns for date objects
df['date'] = [parse(date).date() for date in df['timestamp']]
df['year'] = pd.to_datetime(df['date']).dt.to_period("Y")
df['month'] = pd.to_datetime(df['date']).dt.strftime("%m")
df['day'] = pd.to_datetime(df['date']).dt.strftime("%d")
df['time'] = [parse(time).time() for time in df['timestamp']]
df['hour'] = [parse(hour).time() for hour in df['timestamp']]
df['minute'] = [parse(minute).time() for minute in df['timestamp']]
#df['minute'] = df['time'][3:5]

x = np.array(df['timestamp'])

print(df)

plt.plot(df['timestamp'],df['pm1'], alpha=0.75)
plt.plot(df['timestamp'],df['pm10'], alpha=0.75)
plt.plot(df['timestamp'],df['pm25'], alpha=0.75)

plt.show()