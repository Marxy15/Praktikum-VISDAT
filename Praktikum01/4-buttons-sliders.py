import streamlit as st
import pandas as pd # untuk mengelolah data dalam bentuk frame tabel (dataframe)
import numpy as np # untuk memmbuat data numerik

st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1: Data element")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)

import streamlit as st
st.title('Creatin a Button')
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

import streamlit as st
st.title('Creating Radio Buttons')
gender = st.radio(
"Select your Gender",
('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")
import streamlit as st
st.title('Creating Chekboxes')
st.write('Select your Hobies:')
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')
import streamlit as st
st.title('Creating Dropdown')
hobby = st.selectbox('Choose your hobby: ',
('Books', 'Movies', 'Sports'))
import streamlit as st
st.title('Multi-Select')
hobbies = st.multiselect(
'What are you Hobbies',
['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Playing'])
import streamlit as st
st.title("Download Button")
down_btn = st.download_button(
label="Download Image",
data=open("E:/VISDAT/Assets/animal2.jpg", "rb"),
file_name="animal2.jpg",
mime="image/jpg"
)
import streamlit as st
import time
st.title('Progress Bar')
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')
import streamlit as st
import time
st.title('Spinner')
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')