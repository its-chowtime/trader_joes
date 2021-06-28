import os
import pandas as pd
import numpy as np
import yfinance as yf
import re
import sys
import csv



# listTickers = "SPY"
# startDate = "2021-01-01"
# endDate = "2021-06-24"
# groupby = 'ticker'



def create_stock_list():
    print("Enter the stocks you want to track; separate by ' ': (ex. 'SPY QQQ TSLA') ")
    stocklist = input()
    return stocklist



def pull_stock_data(listTickers, start, end, interval):
    data = yf.download (tickers=listTickers, start=start, end=end, interval=interval, group_by="tickers")
    df = pd.DataFrame(data)
    print(df.head(5))
    return df

#pull_stock_data()


def enter_dates(): # 
    startDate = input("Enter start date: ")
    endDate = input("Enter end date: ")
    return startDate,endDate



def run_function():
    listTickers = create_stock_list()
    start,end = enter_dates()
    interval = input("Interval: ")
    pull_stock_data(listTickers, start, end, interval)

run_function()