# models/sentiment_analysis_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

def train_sentiment_model():
    df = pd.read_csv('../data/raw/India.csv')

    X = df['tweet_text']
    y = df['sentiment']

    vectorizer = TfidfVectorizer(stop_words='english')
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

    os.makedirs('../models/saved', exist_ok=True)
    joblib.dump(model, '../models/saved/sentiment_model.pkl')
    joblib.dump(vectorizer, '../models/saved/sentiment_vectorizer.pkl')

if __name__ == '__main__':
    train_sentiment_model()
