from nltk.sentiment.vader import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd
import csv

class Collection:
    def __init__(self):
        pass
    def sentiment_score(self, df):
        imported_data = list(df)
        imported_data_list = []
        for item in list(range(0, len(imported_data))):
            imported_data_list.append(imported_data[item][0])
        for x, y in enumerate(imported_data_list):
            vader = SentimentIntensityAnalyzer()
            score = vader.polarity_scores(y)
            final = score['compound']
            z = float(final)

    def collect_news(self, ticker_ID):
        ticker = str(ticker_ID.get())
        news_tables = {}
        finviz_url = 'https://finviz.com/quote.ashx?t='
        ticker = str(ticker_ID)
        url = finviz_url + ticker
        req = Request(url=url, headers={'user-agent': 'my-app'})
        response = urlopen(req)
        html = BeautifulSoup(response, 'html')
        news_table = html.find(id='news-table')
        news_tables[ticker] = news_table
        web_data = news_tables[ticker]
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
                parse.append([web_title])
        web_df = pd.DataFrame(parse, columns=['title'])