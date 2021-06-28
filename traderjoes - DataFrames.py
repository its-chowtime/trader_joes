import os
import pandas as pd
import numpy as np
import yfinance as yf
import re
import sys
import csv

df = pd.read_csv("PPD_Data.csv")
print(df.tail())

print(df['Last Action'].head())


# listTickers = "SPY"
# startDate = "2021-01-01"
# endDate = "2021-06-24"
# groupby = 'ticker'



def create_stock_list():
    print("Enter the stocks you want to track; separate by ' ': (ex. 'SPY QQQ TSLA' ")
    listTickers = input()
    return listTickers



def pull_stock_data():
    data = yf.download (tickers="SPY", start="2021-01-01", end="2021-06-24", group_by="tickers")
    df = pd.DataFrame(data)
    print(df.head(5))
    return df

#pull_stock_data()


def enter_dates(): # 
    startDate = input()
    endDate = input()
    return startDate,endDate



def run_function(listTickers,startDate,endDate,groupby):
    list1 = []
    listTickers()
    enter_dates()
    pull_stock_data(listTickers,startDate,endDate,groupby)

def main():
    try:
        print('yes')
        end = sys.argv[0]
        print(end)
    except:
        print('nope')

main()