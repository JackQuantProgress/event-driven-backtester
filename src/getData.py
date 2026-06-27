import yfinance as yf
import pandas as pd

def getData(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df.to_csv("data/SPY.csv")

start = "2020-01-01"
end = "2021-01-01"

getData("SPY", start, end)