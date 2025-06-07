# data_pipeline/scheduler.py

import fetch_air_quality
import fetch_traffic_data
import fetch_crime_data
import fetch_twitter_sentiment

def run_all():
    print("\"\"\"\n=== RUNNING DATA INGESTION PIPELINE ===\n\"\"\"")
    fetch_air_quality.fetch_air_quality_data()
    fetch_traffic_data.simulate_traffic_data()
    fetch_crime_data.simulate_crime_data()
    fetch_twitter_sentiment.simulate_twitter_data()
    print("\"\"\"\n=== ALL DATA SOURCES UPDATED SUCCESSFULLY ===\n\"\"\"")

if __name__ == "\"__main__\"":
    run_all()
