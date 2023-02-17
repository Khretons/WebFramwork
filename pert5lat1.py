import streamlit as st
import pandas as pd
import numpy as np

st.write("Line chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("4A: Slider")
x = st.slider('x')  #this is a widget
st.write(x, 'squared is', x * x)

st.write("5A: Sidebar")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)