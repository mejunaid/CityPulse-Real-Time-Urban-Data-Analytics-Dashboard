# data_pipeline/fetch_crime_data.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

OUTPUT_PATH = os.path.join("data", "raw", "crime_dataset_india.csv")

def simulate_crime_data(num_records=100):
    np.random.seed(7)
    crime_types = ['Theft', 'Assault', 'Burglary', 'Vandalism', 'Fraud']
    locations = ['Connaught Place', 'Saket', 'Rohini', 'Lajpat Nagar', 'Dwarka']
    
    data = {
        'incident_id': [f"CRIME{str(i).zfill(4)}" for i in range(num_records)],
        'timestamp': [(datetime.utcnow() - timedelta(hours=np.random.randint(0, 72))).isoformat() for _ in range(num_records)],
        'location': np.random.choice(locations, num_records),
        'crime_type': np.random.choice(crime_types, num_records),
        'severity': np.random.randint(1, 5, size=num_records)
    }

    df = pd.DataFrame(data)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Simulated crime data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    simulate_crime_data()
