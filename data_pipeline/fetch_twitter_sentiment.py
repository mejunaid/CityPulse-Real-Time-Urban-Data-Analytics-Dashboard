# data_pipeline/fetch_twitter_sentiment.py

import pandas as pd
import numpy as np
from datetime import datetime
import os

OUTPUT_PATH = os.path.join("data", "raw", "India.csv")

def simulate_twitter_data(num_records=100):
    np.random.seed(21)
    locations = ['Connaught Place', 'Saket', 'Rohini', 'Lajpat Nagar', 'Dwarka']
    sentiments = ['positive', 'neutral', 'negative']
    sample_texts = [
        "Traffic is horrible right now.",
        "Loving the weather today!",
        "Police presence is high near the market.",
        "AQI is terrible again!",
        "This city feels alive tonight."
    ]

    data = {
        'timestamp': [datetime.utcnow().isoformat()] * num_records,
        'location': np.random.choice(locations, num_records),
        'tweet_text': np.random.choice(sample_texts, num_records),
        'sentiment': np.random.choice(sentiments, num_records, p=[0.3, 0.4, 0.3])
    }

    df = pd.DataFrame(data)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Simulated Twitter sentiment data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    simulate_twitter_data()
