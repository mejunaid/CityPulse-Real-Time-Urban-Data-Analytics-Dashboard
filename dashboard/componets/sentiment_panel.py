# dashboard/sentiment_panel.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def display():
    st.header("💬 Twitter Sentiment Overview")
    df = pd.read_csv("data/raw/India.csv")
    
    st.write("Recent Tweets:")
    st.dataframe(df[['location', 'tweet_text', 'sentiment']].head(10))

    fig, ax = plt.subplots(figsize=(6,4))
    sns.countplot(x='sentiment', data=df, palette='pastel', ax=ax)
    ax.set_title("Sentiment Distribution")
    st.pyplot(fig)
