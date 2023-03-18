import streamlit as st
import pandas as pd
import numpy as np

st.title("CONTROL FLOW")

st.subheader("st.stop: ")
name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')