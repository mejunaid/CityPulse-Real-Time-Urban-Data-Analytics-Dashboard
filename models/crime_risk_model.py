# models/crime_risk_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

def train_crime_model():
    df = pd.read_csv('../data/raw/crime_dataset_india.csv')
    df = pd.get_dummies(df, columns=['location', 'crime_type'], drop_first=True)

    X = df.drop(['incident_id', 'timestamp', 'severity'], axis=1)
    y = df['severity']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

    joblib.dump(model, '../models/saved/crime_model.pkl')

if __name__ == '__main__':
    os.makedirs('../models/saved', exist_ok=True)
    train_crime_model()
