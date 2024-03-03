import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime
import yfinance as yf

ticker_symbol = 'KCP.BO'  # This can be changed to any desired ticker
model = load_model(f"D:\GitHub\Portfolio-and-Stock-Price-Prediction\Algorithm\Prediction-LSTM\models\{ticker_symbol}.keras")
start_date = datetime(2024, 1, 1)  # Change to your desired start date
end_date = datetime.now()  # Change to your desired end date
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
look_back = 1
num_iter = 60
prices = stock_data['Close']
predictions = []

def create_dataset(dataset, look_back=1):
    X = []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
    return np.array(X)

for i in range(num_iter):
    prices_reshaped = prices.values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_prices = scaler.fit_transform(prices_reshaped)
    X_test = create_dataset(scaled_prices, look_back)
    X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))
    prediction = model.predict(X_test)
    prediction = scaler.inverse_transform(prediction)
    prediction = (sum(prediction)/len(prediction))[0]
    predictions.append(prediction)
    end_date = end_date + timedelta(days=1)
    row = pd.Series([prediction], index=[end_date])
    prices = prices._append(row)
    print(len(predictions))

print(predictions)

plt.plot(predictions)
plt.show()