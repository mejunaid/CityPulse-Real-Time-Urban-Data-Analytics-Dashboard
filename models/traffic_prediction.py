# models/traffic_prediction.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os

def train_traffic_model():
    df = pd.read_csv('../data/raw/traffic.csv')
    df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
    df = pd.get_dummies(df, columns=['location'], drop_first=True)

    X = df.drop(['traffic_density', 'timestamp'], axis=1)
    y = df['traffic_density']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    print(f"RMSE: {mean_squared_error(y_test, preds, squared=False):.2f}")
    joblib.dump(model, '../models/saved/traffic_model.pkl')

if __name__ == '__main__':
    os.makedirs('../models/saved', exist_ok=True)
    train_traffic_model()
