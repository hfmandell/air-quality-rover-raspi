import pandas as pd
import numpy as np
# import cartopy.crs as ccrs
import folium
from folium import plugins

from datetime import datetime
import geopandas as gpd
import seaborn as sns

from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import matplotlib.colors

from ipyleaflet import Map, Marker, AntPath, CircleMarker, LegendControl, WidgetControl
from ipywidgets import HTML, SelectionRangeSlider, Output

# https://medium.com/@ianforrest11/graphing-latitudes-and-longitudes-on-a-map-bf64d5fca391

df = pd.read_csv('data/processed/pm_with_gps.csv')
df.reset_index()
df.index = range(df.shape[0])

def get_most_recent_point():
    most_recent_lat = df['lat'].values[-1]
    most_recent_long = df['long'].values[-1]
    return [most_recent_lat, most_recent_long]

def get_first_and_last_dates():
    start_date = df['timestamp'].values[0]
    end_date = df['timestamp'].values[-1:]
    print(type(end_date))
    if type(end_date == np.ndarray):
        end_date = end_date[0]
    return [start_date, end_date]

start_date = str(get_first_and_last_dates()[0])
end_date = str(get_first_and_last_dates()[1])

start_date_dt = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
end_date_dt = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")

dates = pd.date_range(start_date_dt, end_date_dt, freq='D')

print(start_date)
print(end_date)
print(dates)

options = [(date.strftime(' %d %b %Y '), date) for date in dates]
index = (0, len(options)-1)

selection_range_slider = SelectionRangeSlider(
    options=options,
    index=index,
    description='Dates',
    orientation='horizontal' #,
    # layout={'width': '500px'}
)

selection_range_slider

m = Map(center=(get_most_recent_point()[0], get_most_recent_point()[1]), zoom=150)

for pm1, lat, long in df[["pm1", "lat", "long"]].values:
    
    # create an instance of the marker
    marker = Marker(location=(lat, long), draggable=False, title=str(pm1), alt=str(pm1), visible=False, opacity=0.5)

    # craft a pop-up message
    message =  HTML(value="%s: %d µg/m³"%("PM1", pm1))
    marker.popup = message

    # add the marker to the layer
    m.add_layer(marker)

    # change color of mark accordingly
    if pm1 < 1:
        circleColor = "#fcd0ff"
    elif pm1 <= 5:
        circleColor = "#c27bff"
    else: #pm1 > 5
        circleColor = "#502a57"

    c_marker = CircleMarker(location=(lat, long), radius=5, color=circleColor, fill_color=circleColor, fill_opacity=0.85)
    m.add_layer(c_marker)

# add a path of the lat/long measurements taken
locations = df[["lat", "long"]].values.tolist()
poly_line = AntPath(locations=locations, delay=3000, color="gray" , pulse_color="white")
m.add_layer(poly_line)

m.layout.height="550px"

# add a legend
legend = LegendControl({"safe":"#fcd0ff", "caution":"#c27bff", "danger":"#502a57"}, name="Legend", position="bottomright")
m.add_control(legend)

output_widget = Output(layout={'border': '1px solid black'})
output_control = WidgetControl(widget=output_widget, position='bottomright')
m.add_control(output_control)

m.add_control(selection_range_slider)

m.save('templates/pm1-map.html')

# if __name__ == "__main__":
#     plot_pms()

