import streamlit as st
import pandas as pd
import numpy as np

st.title("Bar Chart")
st.subheader("Kelompok: 9")
st.markdown("""
            - Santika Sintia Larasati (0110122045)
            - Saepulloh  (0110222183)
            - Muhammad Ammar (0110122308)
""")

df = pd.DataFrame(
    np.random.randn(40,4),
    columns=["C1", "C2", "C3", "C4"]
)

st.bar_chart(df)