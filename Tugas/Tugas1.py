import streamlit as st
import pandas as pd
import numpy as np

"""
# Tugas 1 : Dataframe & Line-chart
"""

st.subheader("Holocure Collab Dataframe")

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
        "BL book + Psycho axe",
        "Elite lava bucket + Psycho axe",
        "BL book + Wammy water",
        "Wammy water + Glowstick",
        "X-potato + Elite lava bucket",
        "Cutting board + Bounce ball"
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
        "BL fujoshi",
        "Mi comet",
        "Frosen sea",
        "Snow flower sake",
        "Mikorone",
        "Absolute wall"
    ]
})

st.write(frame_data)

# Dataframe dan Line-chart merupakan data yang berbeda

st.subheader("Line chart:")

st.write("CD PROJEKT SA (CDR), 2022")
chart_data = pd.DataFrame({
    'Month' : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Terakhir' : [180.06, 168.40, 173.74, 120.98, 108.66, 95.68],
    'Tertinggi' : [208.10, 188.00, 187.14, 179.92, 125.40, 110.62],
    'Terendah' : [166.10, 150.20, 155.00, 119.78, 105.88, 86.69]
})

chart_data = chart_data.set_index('Month')
st.line_chart(chart_data)