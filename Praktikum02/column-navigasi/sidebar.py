import streamlit as st
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0, 10)