import streamlit as st
import pandas as pd
import numpy as np

st.title("INPUT WIDGETS")

st.subheader("checkbox: ")
agree = st.checkbox('Are you a fish?')

if agree:
    st.write('Hhmmm... Interesting')