import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.subheader("Kelompok: 9")
st.markdown("""
            - Santika Sintia Larasati (0110122045)
            - Saepulloh  (0110222183)
            - Muhammad Ammar (0110122308)
""")

df=pd.DataFrame(
    np.random.randn(50,2)/[10,10]+[15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)