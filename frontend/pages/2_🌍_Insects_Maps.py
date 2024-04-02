import streamlit as st
import pandas as pd
import numpy as np
import controller as ct

st.set_page_config(layout="wide", page_title="Insects Map")

st.write("## Insects Map")
st.write(
    ":butterfly: All insect finds recorded on the platform are located on this map. :mag:"
)

df2 = pd.DataFrame(ct.readRowsInferencia())
df2 = df2.drop (0, axis = 1)
df2 = df2.rename(columns={1: 'lat', 2: 'lon', 3: 'color'})

st.map(df2)

#data = {
#    'latitude': [34.0522, 37.7749, 40.7128],
#    'longitude': [-118.2437, -122.4194, -74.0060],
#    'color': ['red', 'green', 'blue'],
#    'size': [10, 20, 15]
#}
#df = pd.DataFrame(data)
# Display the map with colored and sized markers
#st.map(df, size="size", color="color")