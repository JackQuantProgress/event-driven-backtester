import math
from Events.OrderEvent import OrderEvent

class Portfolio(object):
    """
    Analyses position, signals and risks to decide whether to make a trade or not.
    """
    def __init__(self):
        self.total = 1000

        self.cash = 1000

        self.position_size = 0.1

        self.stop_loss = 0.1

        self.current_position = 0
          # 0 = flat
          #-1 = short
          #1 = long
        self.shares = 0

        self.entry_value = None

    def handle_signal_event(self, event):
        #flat and buy
        if self.current_position == 0 and event.signal_type == "BUY":
            return self.calculate_position_size(event.current_price)
        #long and sell
        elif self.current_position == 1 and event.signal_type == "SELL":
            return self.create_order_event(self.shares)
        else:
            return None

    def calculate_position_size(self, share_price):

        budget = (self.cash * self.position_size)
        shares = math.floor(budget / share_price)

        return self.create_order_event(shares)

    def create_order_event(self, shares):
        #check position
        if self.current_position == 1:
            return OrderEvent(shares, "SELL")
        elif self.current_position == 0:
            return OrderEvent(shares, "BUY")
        else:
            raise NotImplementedError("shorting is not implemented yet")

    def check_stop_loss(self):
        #checks on each market event whether or not the stop loss has be crossed
        #if it has returns OrderEvent(sell)
        raise NotImplementedError("please implement check_stop_loss()")

    #post fill
    def handle_fill_event(self):
        raise NotImplementedError("please implement handle_fill_event()")

    def calculate_portfolio_value(self):
        raise NotImplementedError("please implement calculate_portfolio_value()")

    def record_history(self):
        raise NotImplementedError("please implement record_history()")
