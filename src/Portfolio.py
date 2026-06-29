import math
from Events.OrderEvent import OrderEvent

class Portfolio(object):
    """
    Analyses position, signals and risks to decide whether to make a trade or not.
    """
    def __init__(self):
        self.total = 100000

        self.cash = 100000

        self.position_size = 0.1

        self.stop_loss = 0.1

        self.current_position = 0
          # 0 = flat
          #-1 = short
          #1 = long
        self.shares = 0

        self.entry_value = None

        self.current_share_price = None

        self.trades = [] #trade profit

    def handle_signal_event(self, event):
        #flat and buy
        if self.current_position == 0 and event.signal_type == "BUY":
            return self.calculate_position_size(event)
        #long and sell
        elif self.current_position == 1 and event.signal_type == "SELL":
            return self.create_order_event(self.shares, event.current_price, event.date)
        else:
            return None

    def calculate_position_size(self, event):

        budget = (self.cash * self.position_size)
        shares = math.floor(budget / event.current_price)

        return self.create_order_event(shares, event.current_price, event.date)

    def create_order_event(self, shares, share_price, date):
        #check position
        if self.current_position == 1:
            return OrderEvent(shares, "SELL", share_price, date)
        elif self.current_position == 0:
            return OrderEvent(shares, "BUY", share_price, date)
        else:
            raise NotImplementedError("shorting is not implemented yet")

    def check_stop_loss(self, event):#MarketEvent
        self.current_share_price = event.close
        if self.current_position == 1:
            stop_loss_value = (self.entry_value * (1-self.stop_loss))
            if event.close < stop_loss_value:
                return OrderEvent(self.shares, "SELL", event.close, event.date)
            else:
                return None

    #post fill
    def handle_fill_event(self, event):
        print("trade confirmed")
        if event.direction == "BUY":
            self.shares += event.quantity
            self.cash -= event.fill_price
            self.current_position = 1
            self.entry_value = event.fill_price/event.quantity
            self.stop_loss
        
        elif event.direction == "SELL":
            self.trades.append({"profit = " + str((event.fill_price - (self.entry_value * self.shares)))})
            self.shares -= event.quantity
            self.cash += event.fill_price
            self.current_position = 0
            

    def calculate_portfolio_value(self):
        return (self.cash + (self.shares * self.current_share_price))

    def record_history(self):
        return self.trades
