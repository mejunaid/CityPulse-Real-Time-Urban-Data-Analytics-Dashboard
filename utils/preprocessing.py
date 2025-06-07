# utils/preprocessing.py

import pandas as pd
import numpy as np

def clean_air_quality_data(df):
    df = df.copy()
    df['datetime'] = pd.to_datetime(df['date.utc'], errors='coerce')
    df = df.dropna(subset=['datetime', 'value'])
    df['location'] = df['location'].str.strip().str.title()
    df['parameter'] = df['parameter'].str.lower()
    df = df[df['value'] >= 0]  # remove negative pollution values
    return df

def preprocess_traffic_data(df):
    df = df.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp', 'traffic_density'])
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['location'] = df['location'].str.strip().str.title()
    df = df[df['traffic_density'] >= 0]
    return df

def preprocess_crime_data(df):
    df = df.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp', 'crime_type', 'severity'])
    df['crime_type'] = df['crime_type'].str.strip().str.title()
    df['location'] = df['location'].str.strip().str.title()
    df['severity'] = df['severity'].astype(int)
    return df

def preprocess_twitter_data(df):
    df = df.copy()
    df = df.dropna(subset=['tweet_text', 'sentiment'])
    df['tweet_text'] = df['tweet_text'].str.strip().str.lower()
    df['sentiment'] = df['sentiment'].str.lower()
    df = df[df['sentiment'].isin(['positive', 'neutral', 'negative'])]
    return df
