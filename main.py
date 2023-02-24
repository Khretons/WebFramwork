import streamlit as st
import pandas as pd
import numpy as np

"""
# App
"""

st.subheader("Manual Dataframe")

frame_data = pd.DataFrame({
    'Weapons': [
        "EN's curse + Cutting board",
        "X-potato + Idol song",
        "Plug type Asacoco + Holo bomb",
        "Fan beam + Plug Type Asacoco",
        "CEO's tears + Spider cooking",
        "Elite lava bucket + Spider cooking",
        "EN's curse + Spider cooking",
        "Idol song + Glowstick",
        "Fan beam + CEO's tears",
        "BL book + Psycho axe"
        ],
    'Collab': [
        "Bone bros.",
        "Rap dog",
        "Breathe-in type Asacoco",
        "Dragon fire",
        "Broken dreams",
        "Elite Cooking",
        "Eldritch horror",
        "Idol concert",
        "Stream of tears",
        "BL fujoshi"
    ]
})

st.write(frame_data)


st.subheader("Line chart:")

st.write("CD PROJEKT SA (CDR), 2022")
chart_data = pd.DataFrame({
    'Month' : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Terakhir' : [180.06, 168.40, 173.74, 120.98, 108.66, 95.68, 90.81, 84.12, 100.20, 127.10, 130.98, 129.64],
    'Tertinggi' : [208.10, 188.00, 187.14, 179.92, 125.40, 110.62, 105.92, 96.69, 108.50, 128.60, 153.50, 143.00],
    'Terendah' : [166.10, 150.20, 155.00, 119.78, 105.88, 86.69, 86.60, 80.86, 76.83, 96.61, 126.24, 122.58]
})

chart_data = chart_data.set_index('Month')
st.line_chart(chart_data)


#Reference: https://discuss.streamlit.io/t/date-at-x-axis-of-line-chart/853/3