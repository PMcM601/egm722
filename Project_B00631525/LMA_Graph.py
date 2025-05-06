import geopandas as gpd
import pandas as pd
import plotly.express as px

# Load shapefiles
lmas = gpd.read_file('Datasets/LocalManagementArea.shp')
overflows = gpd.read_file('Datasets/EGM722_StormOverflows.shp')
wwtws = gpd.read_file('Datasets/EGM722_TreatedDisc.shp')



