import streamlit as st
import pandas as pd
import numpy as np

st.title("Columns")
st.subheader("Kelompok: 9")
st.markdown("""
            - Santika Sintia Larasati (0110122045)
            - Saepulloh  (0110222183)
            - Muhammad Ammar (0110122308)
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../../Praktikum01/Assets/animal3.jpg")
col2.write("Ini adalah kolom kedua")
col2.image("../../Praktikum01/Assets/animal2.jpg")

import streamlit as st
from PIL import Image
img = Image.open("../../Praktikum01/Assets/animal3.jpg")
st.title("Space-Out Columns")

for _ in range(2):
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)

import streamlit as st
from PIL import Image
img = Image.open("../../Praktikum01/Assets/animal3.jpg")
st.title("Padding")

col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)

