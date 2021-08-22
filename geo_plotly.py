# import plotly.plotly as py
import plotly.graph_objs as go
import plotly.express as px
import geopandas as gpd
import json
import pandas as pd


def plot_pm_maps_over_time(pm_size):
    # plotly!
    df = pd.read_csv("data/processed/pm_with_gps.csv")
    print(df.head)
    pm_df = df[['timestamp','lat','long',pm_size]].round(decimals=3)
    print(pm_df.head)

    # layout = Layout(autosize=True,
    #                 hovermode='closest'
    #                 ,title="my map",
    #                 mapbox= dict(bearing=0,
    #                             pitch=0, zoom=10,
    #                             center=dict(lat=xx,
    #                                         lon=yy)),)

    fig = px.scatter_mapbox(pm_df, lat = "lat", lon = "long",
                            color = pm_size,
                            hover_name=pm_size,
                            animation_frame="timestamp",
                            animation_group="country",
                            =0, zmax=30
                            )
                        #  hover_data=pm_size)
    # fig = px.line(df, x='timestamp', y=df.columns,#y='pm1',
    # #               hover_data={"timestamp": "|%B %d, %Y, %-I:%M:%S %p"},
    # #               title = "All PM Measurements")
    #               # to do a custom date range:
    #             #   range_x=['2016-07-01','2016-12-31'])
    #              )
    fig.update_geos(fitbounds="locations")
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()
    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    # return graphJSON

if __name__ == "__main__":
    plot_pm_maps_over_time('pm1')