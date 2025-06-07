# dashboard/traffic_panel.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def display():
    st.header("🚗 Traffic Overview")
    df = pd.read_csv("data/raw/traffic.csv")
    
    st.write("Recent Traffic Data:")
    st.dataframe(df.head(10))
    
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x='location', y='traffic_density', data=df, ax=ax, palette='YlOrRd')
    ax.set_title('Traffic Density by Location')
    st.pyplot(fig)
