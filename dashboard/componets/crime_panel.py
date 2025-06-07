# dashboard/crime_panel.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def display():
    st.header("🚓 Crime Report Overview")
    df = pd.read_csv("data/raw/crime_dataset_india.csv")

    st.dataframe(df.head(10))
    
    st.subheader("Crime Type Frequency")
    fig1, ax1 = plt.subplots()
    sns.countplot(x='crime_type', data=df, ax=ax1, palette='Set2')
    st.pyplot(fig1)

    st.subheader("Crime by Location")
    fig2, ax2 = plt.subplots()
    sns.countplot(x='location', hue='crime_type', data=df, ax=ax2)
    st.pyplot(fig2)
