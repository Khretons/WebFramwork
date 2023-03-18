import streamlit as st
import pandas as pd
import numpy as np


st.subheader("st.write: ")
st.write('6 x 9 =', 54)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

st.subheader("st.magic: ")
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x