# data_pipeline/fetch_traffic_data.py

import pandas as pd
import numpy as np
from datetime import datetime
import os

OUTPUT_PATH = os.path.join("data", "raw", "traffic.csv")

def simulate_traffic_data(num_records=100):
    """
    Simulates traffic data for demonstration purposes.
    Replace this with real API data when available.
    """
    np.random.seed(42)
    locations = ['Connaught Place', 'Saket', 'Rohini', 'Lajpat Nagar', 'Dwarka']
    data = {
        'timestamp': [datetime.utcnow().isoformat()] * num_records,
        'location': np.random.choice(locations, num_records),
        'traffic_density': np.random.randint(20, 100, size=num_records),
        'avg_speed_kmph': np.random.randint(10, 60, size=num_records)
    }
    df = pd.DataFrame(data)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Simulated traffic data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    simulate_traffic_data()
