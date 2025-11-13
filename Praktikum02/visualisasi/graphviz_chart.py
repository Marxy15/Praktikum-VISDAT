import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

st.title("Graphviz Chart")
st.subheader("Kelompok: 9")
st.markdown("""
            - Santika Sintia Larasati (0110122045)
            - Saepulloh  (0110222183)
            - Muhammad Ammar (0110122308)
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Result Forecasting"
        "New Data" -> "Model"
    }
""")

import streamlit as st
import graphviz as graphviz
st.title('Graphviz')
# Create a grabhlib graph object
graph = graphviz.Digraph()
graph.edge('Training Data', 'ML Algorithm')
graph.edge('ML Algorithm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')
st.graphviz_chart(graph)