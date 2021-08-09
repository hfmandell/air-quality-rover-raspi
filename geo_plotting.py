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

from ipyleaflet import Map, Marker, Polyline, Polygon, AntPath, MarkerCluster, CircleMarker, LegendControl
from ipywidgets import HTML


# https://medium.com/@ianforrest11/graphing-latitudes-and-longitudes-on-a-map-bf64d5fca391

# def get_most_recent_point():
#     df = pd.read_csv('data/processed/pm_with_gps.csv')
#     most_recent_lat = df['lat'].values[-1]
#     most_recent_long = df['long'].values[-1]
#     return [most_recent_lat, most_recent_long]


# def plot_all_pms():

#     df = pd.read_csv('data/processed/pm_with_gps.csv')
#     lats = df['lat'].to_numpy()
#     longs = df['long'].to_numpy()
#     print(lats)


#     geometry = [Point(xy) for xy in zip(df['long'], df['lat'])]
#     gdf = gpd.GeoDataFrame(df, geometry=geometry)   

#     world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#     gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)

df = pd.read_csv('data/processed/pm_with_gps.csv')

def get_most_recent_point():
    most_recent_lat = df['lat'].values[-1]
    most_recent_long = df['long'].values[-1]
    return [most_recent_lat, most_recent_long]

# folium.

m = Map(center=(get_most_recent_point()[0], get_most_recent_point()[1]), zoom=150)

for pm1, lat, long in df[["pm1", "lat", "long"]].values:
    
    # create an instance of the marker
    marker = Marker(location=(lat, long), draggable=False, title=str(pm1), alt=str(pm1), visible=False, opacity=0.5)

    # craft a pop-up message
    message =  HTML(value="%s: %d µg/m³"%("PM1", pm1))
    marker.popup = message

    # add the marker to the layer
    m.add_layer(marker)

    # circle_marker = CircleMarker()
    # circle_marker.location=(lat, long)
    # circle_marker.radius=10
    # circle_marker.color="red"
    # circle_marker.fill_color="red"
    # circle_marker.fill_opacity=0.5

    # m.add_layer(circle_marker)

# markers = []
# for pm1, lat, long in df[["pm1", "lat", "long"]].values:
#     # create an instance of the marker
#     marker = Marker(location=(lat, long), draggable=False, title=str(pm1), alt=str(pm1), color = "red")

#     # craft a pop-up message
#     message =  HTML(value="%s: %d µg/m³"%("PM1", pm1))
#     marker.popup = message

#     markers.append(marker)

#     marker_cluster = MarkerCluster(markers=markers)
#     # add the marker to the layer
#     m.add_layer(marker_cluster)

# add a path of the lat/long measurements taken
locations = df[["lat", "long"]].values.tolist()
poly_line = AntPath(locations=locations, delay=3000, color="gray" , pulse_color="white")
m.add_layer(poly_line)

m.layout.height="550px"

# add a legend
legend = LegendControl({"low":"#FAA", "medium":"#A55", "High":"#500"}, name="Legend", position="bottomright")
m.add_control(legend)

# m
m.save('templates/pm1-map.html')


# if __name__ == "__main__":
#     plot_all_pms()

