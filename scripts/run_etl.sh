#!/bin/bash

echo "🚀 Starting ETL Pipeline..."

# Activate virtual environment if needed
# source venv/bin/activate

echo "🔄 Running Air Quality ETL..."
python data_pipeline/air_quality_etl.py

echo "🚗 Running Traffic Data ETL..."
python data_pipeline/traffic_etl.py

echo "🕵️‍♂️ Running Crime Data ETL..."
python data_pipeline/crime_etl.py

echo "💬 Running Twitter Sentiment ETL..."
python data_pipeline/twitter_etl.py

echo "✅ All ETL jobs completed."
