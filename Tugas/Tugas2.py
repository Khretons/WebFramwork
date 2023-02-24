import streamlit as st
import numpy as np
import pandas as pd

"""
# Tugas 2 : Chart, Widgets & Layout
"""

st.subheader("Chart")

st.write("Line chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.subheader("Widgets")

st.write("Slider")
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.subheader("Layout")

st.write("Sidebar")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'What is your gender?',
    ('Male', 'Female', 'Fish')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'What is your age?',
    0, 100
)