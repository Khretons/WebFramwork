import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("MEDIA ELEMENT")

st.subheader("Image: ")
image = Image.open('EMINEM.jpg')

st.image(image, caption='The Rap God')