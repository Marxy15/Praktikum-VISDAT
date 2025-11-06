import streamlit as st
st.write("Displaying an images")
st.image("E:/VISDAT/Assets/Data-Science Scope.jpg")
st.write("Image Courtesy: id.pinterest.com")

import streamlit as st
st.write("DisplayingMultiple Images")
animal_images = [
'E:/VISDAT/Assets/animal1.jpg',
'E:/VISDAT/Assets/animal2.jpg',
'E:/VISDAT/Assets/animal3.jpg',
'E:/VISDAT/Assets/animal4.jpg',
'E:/VISDAT/Assets/animal5.jpg',
]
st.image(animal_images, width=150)
st.write("Image Courtesy: Pinterest")

import streamlit as st
import base64
def add_local_background_image_(image):
    with open(image, "rb")as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: Pinterest")
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("Background Image")
add_local_background_image_('E:/VISDAT/Assets/animal2.jpg')

import streamlit as st
from PIL import Image
original_image = Image.open("E:/VISDAT/Assets/animal2.jpg")
st.title("Original Image")
st.image(original_image)
resized_image = original_image.resize((600,400))
st.title("Resized Image")
st.image(resized_image)