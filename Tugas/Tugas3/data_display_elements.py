import streamlit as st 
import pandas as pd
import numpy as np

st.title("DATA DISPLAY ELEMENT")

st.subheader("Dataframe: ")
df = pd.DataFrame(
   np.random.randn(20, 10),
   columns=('col %d' % i for i in range(10)))

st.dataframe(df)  # Same as st.write(df)