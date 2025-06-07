#!/bin/bash

echo "🚀 Training all models..."

# Activate virtual environment if needed
# source venv/bin/activate

echo "🌫️ Training Air Quality Model..."
python models/train_air_quality_model.py

echo "🚦 Training Traffic Prediction Model..."
python models/train_traffic_model.py

echo "🔒 Training Crime Classification Model..."
python models/train_crime_model.py

echo "💡 Training Sentiment Classification Model..."
python models/train_sentiment_model.py

echo "✅ All models trained and saved."
