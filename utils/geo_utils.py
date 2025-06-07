# utils/geo_utils.py

import folium
from folium.plugins import MarkerCluster
import pandas as pd

def plot_map(df, lat_col='latitude', lon_col='longitude', popup_col=None, map_title="Map"):
    """
    Create a folium map with points from the dataframe.
    """
    center_lat = df[lat_col].mean()
    center_lon = df[lon_col].mean()

    m = folium.Map(location=[center_lat, center_lon], zoom_start=12, control_scale=True)
    marker_cluster = MarkerCluster().add_to(m)

    for _, row in df.iterrows():
        popup_text = row[popup_col] if popup_col else ""
        folium.Marker(
            location=[row[lat_col], row[lon_col]],
            popup=popup_text,
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(marker_cluster)

    return m

def add_heatmap(df, lat_col='latitude', lon_col='longitude', weight_col=None):
    """
    Add a heatmap layer to folium map based on coordinates and optional weight.
    """
    from folium.plugins import HeatMap

    base_map = folium.Map(location=[df[lat_col].mean(), df[lon_col].mean()], zoom_start=11)
    heat_data = [
        [row[lat_col], row[lon_col], row[weight_col] if weight_col else 1]
        for _, row in df.iterrows()
    ]
    HeatMap(heat_data).add_to(base_map)
    return base_map

def filter_by_radius(df, center_lat, center_lon, radius_km, lat_col='latitude', lon_col='longitude'):
    """
    Filter rows within a given radius (km) from a central point using Haversine formula.
    """
    from geopy.distance import geodesic

    def within_radius(row):
        point = (row[lat_col], row[lon_col])
        return geodesic((center_lat, center_lon), point).km <= radius_km

    return df[df.apply(within_radius, axis=1)]
