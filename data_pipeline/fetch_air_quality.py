# data_pipeline/fetch_air_quality.py

import requests
import pandas as pd
from datetime import datetime
import os

OUTPUT_PATH = os.path.join("data", "raw", "delhi_aqi.csv")

def fetch_air_quality_data(city="Delhi", country="IN", limit=1000):
    url = "https://api.openaq.org/v2/measurements"
    params = {
        "city": city,
        "country": country,
        "limit": limit,
        "sort": "desc",
        "order_by": "datetime"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code} - {response.text}")

    data = response.json().get("results", [])
    if not data:
        print("No data returned from API.")
        return

    df = pd.json_normalize(data)
    df['fetched_at'] = datetime.utcnow().isoformat()
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(df)} rows to {OUTPUT_PATH}")

if __name__ == "__main__":
    fetch_air_quality_data()
