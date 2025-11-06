#import liberary
import streamlit as st
import pandas as pd #untuk mengelolah data dalam bentuk frame tabel (dataframe)
import numpy as np # untuk memmbuat data numerik
import altair as alt # untuk membuat chart interaktif

st.header("Praktikum1 Visualisasi Data")
st.subheader("Bagian 1: Data element")
st.markdown("""
            - Santika Sintia Larasati - 0110122045
            - Saepulloh  - 0110222183
            - Muhammad Ammar - 0110122308
            """
)

import streamlit as st
st.title("Text Box")
#creating text box
name=st.text_input("Enter your Name")
st.write("Your Name is",name)
# Creating Text box with 10 as character limit 
name = st.text_input("Enter your Name", max_chars=10) 
password = st.text_input("Enter your password", type='password') 

import streamlit as st 
#creating text area
input_text=st.text_area("Enter your Review") 
#printing entered text
st.write(""" you entered: \b""", input_text)

import streamlit as st 
#create number input
st.number_input("Enter Your Number")

import streamlit as st 
#create number input
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min value is 0, \n Max value is 10")
st.write("Default value is 5, \n step size value is 2")
st.write("total value after adding number entered with step value is:", num)

import streamlit as st
st.title("Time")
st.time_input("Select Your Time")
 
import streamlit as st
import datetime
st.title("Date")
# Menampilkan input waktu
st.time_input("Select Time")
# Menampilkan input tanggal
st.date_input("Select Your Date", value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),  
max_value=datetime.date(2005, 12, 1))

import streamlit as st
st.title("Select Color")
# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

import streamlit as st
import pandas as pd
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV",type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,
        "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

import streamlit as st
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')
st.write(a)