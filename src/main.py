from Data.HistoricDataHandler import HistoricDataHandler
from Strategies.MovingAverageCrossover import MovingAverageCrossover
from Events.MarketEvent import MarketEvent
from Portfolio import Portfolio
from ExecutionHandler import ExecutionHandler

import yfinance as yf
import pandas as pd
import os
print(os.getcwd())

start = "2010-01-01"
end = "2025-01-01"

def getData(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df = df.reset_index()
    df.to_csv("data/SPY.csv")

getData("SPY", start, end)

events = []
csv_dir = "data/SPY.csv"
running = True

#Instantiating classes
dataHandler = HistoricDataHandler(events, csv_dir)
strategy = MovingAverageCrossover(20, 50)
portfolio = Portfolio()
execution_handler = ExecutionHandler()

#defining handlers
def handle_market_event(event):
    global events
    #call strategy
    res1 = portfolio.check_stop_loss(event)
    if res1 != None:
        print("STOP LOSS")
        events += [res1]

    res2 = strategy.evaluate_averages(event)
    #if event is returned add it to the queue
    if res2 != None:
        events += [res2]

def handle_fill_event(event):
    global events

    res = portfolio.handle_fill_event(event)

    if res!= None:
        pass
def handle_order_event(event):
    global events

    res = execution_handler.handle_order_event(event)

    if res != None:
        print("FillEvent", res.direction, res.fill_price, res.quantity)
        events += [res]
    else:
        print("no fill event")


def handle_signal_event(event):
    global events

    res = portfolio.handle_signal_event(event)

    if res != None:
        events += [res]


handlers = {
            "MarketEvent" : handle_market_event,
            "FillEvent" : handle_fill_event,
            "OrderEvent" : handle_order_event,
            "SignalEvent" : handle_signal_event
        }

while True:
    # Update the bars (specific backtest code, as opposed to live trading)
    #print("creating bar...")
    bar = dataHandler.get_next_bar()
    #print("done")

    if dataHandler.continue_backtest == False: #end loop
        break

    #create MarketEvent
    #print("creating MarketEvent...")
    events += [MarketEvent(bar["Date"], float(bar["Close"]))]
    #print("done")

    while len(events) > 0:
        #print("handling event...")

        event = events.pop(0)
        event_type = event.type

        handlers[event_type](event)
print("start cash = 100000   end cash = ", portfolio.calculate_portfolio_value())
