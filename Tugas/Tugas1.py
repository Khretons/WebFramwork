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

# I didn't use all of the data from the Dataframe
st.subheader("Line chart:")

st.write("Number of Weapon's Collab")
chart_data = pd.DataFrame({
    'Weapon' : ['ENs curse', 'Cutting Board', 'X-potato', 'CEOs Tears', 'Idol Song', 'BL Book', 'Wammy Water', 'Fan Beam', 'Holo Bomb'],
    'Collab Total' : [2, 2, 2, 1, 2, 2, 2, 2, 2],
    'Most Used' : [1, 1, 7, 10, 5, 4, 6, 2, 3],
})

chart_data = chart_data.set_index('Weapon')
st.line_chart(chart_data)
