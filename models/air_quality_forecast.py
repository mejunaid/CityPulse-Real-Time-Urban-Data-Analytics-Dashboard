# models/air_quality_forecast.py

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import os

def train_arima_model():
    df = pd.read_csv('../data/raw/delhi_aqi.csv')
    df['datetime'] = pd.to_datetime(df['date.utc'])
    df = df[df['parameter'] == 'pm25'].sort_values('datetime')

    df.set_index('datetime', inplace=True)
    ts = df['value'].resample('H').mean().ffill()

    model = ARIMA(ts, order=(2,1,2))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=24)

    plt.figure(figsize=(10, 4))
    ts[-48:].plot(label='Historical')
    forecast.plot(label='Forecast', color='red')
    plt.legend()
    plt.title('PM2.5 Forecast for Next 24 Hours')
    plt.show()

    print(forecast)

if __name__ == '__main__':
    train_arima_model()
