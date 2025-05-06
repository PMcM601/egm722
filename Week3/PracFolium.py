import pandas as pd
import geopandas as gpd
import folium

wards = gpd.read_file('data_files/NI_Wards.shp')

wards.head()

m = wards.explore('Population', cmap='viridis')

m # show the map