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
print(df2)

#df = pd.DataFrame({
#    "lat": np.random.randn(1000) / 50 + 3.3638927,
#    "lon": np.random.randn(1000) / 50 + -76.5255511,
#    #"color": np.random.rand(1000, 4).tolist()
#    "color": '[200, 30, 200, 160]',
#})
st.map(df2)