from datetime import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Predict:
    def __init__(self, ticker_id, parameter):
        global date, time
        news_tables = {}
        finviz_url = 'https://finviz.com/quote.ashx?t='
        url = finviz_url + ticker_id
        req = Request(url=url, headers={'user-agent': 'my-app'})
        response = urlopen(req)
        html = BeautifulSoup(response, 'html')
        news_table = html.find(id='news-table')
        news_tables[ticker_id] = news_table
        web_data = news_tables[ticker_id]
        web_data_rows = web_data.findAll('tr')
        parse = []
        for ticker, news_table in news_tables.items():
            for row in news_table.findAll('tr'):
                web_title = row.a.get_text()
                web_date_data = row.td.text.split(' ')
                if len(web_date_data) == 1:
                    time = web_date_data[0]
                else:
                    date = web_date_data[0]
                    time = web_date_data[1]
                parse.append([ticker, date, time, web_title])
        web_df = pd.DataFrame(parse, columns=['ticker', 'date', 'time', 'title'])
        vader = SentimentIntensityAnalyzer()
        lam_fun = lambda title: vader.polarity_scores(title)['compound']
        web_df['compound'] = web_df['title'].apply(lam_fun)
        mean_final = web_df['compound'].mean()
        start_date = dt.datetime(2000, 1, 1)
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        end_date = f"{year}, {month}, {day}"
        past_days = int(30)
        data = web.DataReader(ticker_id, "yahoo", start_date, end_date)
        scalar = MinMaxScaler(feature_range=(0,1))
        scaled_data = scalar.fit_transform(data[parameter].values.reshape(-1,1))
        x_train = []
        y_train = []
        for x in range(past_days, len(scaled_data)):
                x_train.append(scaled_data[x-past_days:x, 0])
                y_train.append(scaled_data[x, 0])
        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        training_model = Sequential()
        training_model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        training_model.add(Dropout(0.2))
        training_model.add(LSTM(units=50, return_sequences=True))
        training_model.add(Dropout(0.2))
        training_model.add(LSTM(units=50))
        training_model.add(Dropout(0.2))
        training_model.add(Dense(units=1))
        training_model.compile(optimizer = 'adam', loss = 'mean_squared_error')
        training_model.fit(x_train, y_train, epochs=30, batch_size=32)
        test_data = web.DataReader(ticker_id, 'yahoo', start_date, end_date)
        actual_prices = test_data['Close'].values
        total_dataset = pd.concat((data['Close'], test_data[parameter]), axis=0)
        model_input = total_dataset[len(total_dataset) - len(test_data) - past_days:].values
        model_inputs = model_input.reshape(-1, 1)
        model_input = scalar.transform(model_inputs)
        x_test = []
        for x in range(past_days, len(model_input)):
                x_test.append(model_input[x-past_days:x, 0])
        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        predicted_prices = training_model.predict(x_test)
        predicted_prices = scalar.inverse_transform(predicted_prices)
        plt.plot(actual_prices, color='black', label=f'Actual {ticker_id} Price')
        plt.plot(predicted_prices, color='green', label=f'Predicted {ticker_id} Price')
        plt.title(f'{ticker_id} Share Price')
        plt.xlabel('Time')
        plt.ylabel(f'{ticker_id} Share Price')
        plt.legend()
        plt.show()
        quote = web.DataReader(ticker_id, 'yahoo', start_date, end_date)
        df_scalar = MinMaxScaler(feature_range=(0,1))
        df_scaled_data = df_scalar.fit_transform(data[parameter].values.reshape(-1,1))
        df_x_test = [df_scaled_data]
        df_x_test = np.array(x_test)
        df_x_test = np.reshape(df_x_test, (df_x_test.shape[0], df_x_test.shape[1], 1))
        predict = training_model.predict(df_x_test)
        predict = df_scalar.inverse_transform(predict)
        count = int(0)
        length = len(predict)
        dataframe_list = []
        while count < length:
                initial = predict[count][0]
                count = count + 1
                dataframe_list.append(initial)
        df = pd.DataFrame(dataframe_list, columns=['price'])
        top = df['price'].nlargest(n=40).mean()
        a = float(top)
        b= float(mean_final)
        c = float(a * b)
        final_price_to_display = a + c
        final_round = round(final_price_to_display, 2)
        print(final_round)
        
Predict("TSLA", "Open")