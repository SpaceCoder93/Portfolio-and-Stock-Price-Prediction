import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf

# Load stock data
ticker_symbol = 'KCP.BO'
start_date = datetime(1985, 1, 1)
end_date = datetime(2024, 2, 12)
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
prices = stock_data['Close'].values.reshape(-1, 1)

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_prices = scaler.fit_transform(prices)

# Split data into training and testing sets
train_size = int(len(scaled_prices) * 0.80)
train = scaled_prices[0:train_size, :]

# Function to create dataset
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 1
X_train, Y_train = create_dataset(train, look_back)
X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))

# Build the LSTM model
model = Sequential()
model.add(LSTM(20, input_shape=(1, look_back)))
model.add(Dropout(0.2))
model.add(Dense(1))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X_train, Y_train, epochs=100, batch_size=1, verbose=2)

# Save the model
model.save(f"models/{ticker_symbol}.keras")