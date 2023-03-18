import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("STATUS ELEMENT")

st.subheader("Progress Bar: ")
st.write("Wait for a bit OK?")

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

st.snow()