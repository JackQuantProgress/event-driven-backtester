import yfinance as yf
import pandas as pd
import os
import * from HistoricalDataHandler
print(os.getcwd())

start = "2020-01-01"
end = "2021-01-01"

def getData(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df.to_csv("data/SPY.csv")

#getData("SPY", start, end)

events = []
csv_dir = "data/SPY.csv"
running = True

dataHandler = HistoricalDataHandler(events, csv_dir)

while (running):

