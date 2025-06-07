# dashboard/air_quality_panel.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def display():
    st.header("🌫️ Air Quality Overview")
    df = pd.read_csv("data/raw/AirQualityUCI.csv")
    df['datetime'] = pd.to_datetime(df['date.utc'])
    df_pm25 = df[df['parameter'] == 'pm25']
    
    st.write("Latest air quality measurements (PM2.5):")
    st.dataframe(df_pm25[['location', 'value', 'unit', 'datetime']].sort_values('datetime', ascending=False).head(10))
    
    pm25_avg = df_pm25.groupby('location')['value'].mean().sort_values()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=pm25_avg.values, y=pm25_avg.index, ax=ax, palette='coolwarm')
    ax.set_title('Average PM2.5 by Location')
    st.pyplot(fig)
