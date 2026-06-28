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

#Instantiating classes
dataHandler = HistoricalDataHandler(events, csv_dir)

while (running):
    #Get next peice of data.
    dataHandler.get_next_bar()
    #Pass the MarketEvent to the Strategy.
    #If a SignalEvent is returned pass to the Portfolio.
    #If an OrderEvent is returned pass to the ExecutionHandler.
    #Use the FillEvent to update the Portfolio.
    #Check the running variable in DataHadler.

