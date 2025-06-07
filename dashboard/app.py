# dashboard/app.py

import streamlit as st
from components import air_quality_panel, traffic_panel, crime_panel, sentiment_panel


st.set_page_config(page_title="CityPulse: Urban Analytics", layout="wide")
st.title("📊 CityPulse: Real-Time Urban Analytics Dashboard")

st.sidebar.title("🔍 Choose Panel")
option = st.sidebar.radio("Select a view", ["Air Quality", "Traffic", "Crime", "Sentiment"])

if option == "Air Quality":
    air_quality_panel.display()
elif option == "Traffic":
    traffic_panel.display()
elif option == "Crime":
    crime_panel.display()
elif option == "Sentiment":
    sentiment_panel.display()
