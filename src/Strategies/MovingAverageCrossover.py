from .Strategy import Strategy
from Events.SignalEvent import SignalEvent

class MovingAverageCrossover(Strategy):
    def __init__(self, short_window, long_window):
        """
        Attributes:
        short_window - the shorter length of the period for averages.
        long_window - the longer length of the period for averages.
        sign - the sign of the previous difference between averages.
        prices - cache for the close prices from the bars.

        Methods:
        evaluate_averages - computes the averages over 2 different periods and when they cross calls the create_signal_event method
        create_signal_event - creates a signal event using the sign from the averages
        """

        self.short_window = short_window
        self.long_window = long_window

        self.sign = None

        self.prices = []

    def evaluate_averages(self, marketEvent):
        #add to cache
        self.prices.append(marketEvent.close)

        #skip if not enough data
        if len(self.prices) < self.long_window:
            return None

        #remove to keep the length of the cache the same
        self.prices.pop(0)

        #short average
        temp = 0
        for i in range(self.short_window):
            temp += self.prices[len(self.prices)-1-i]
        short = temp/self.short_window

        #long average
        temp = 0
        for x in self.prices:
            temp += x
        long = temp/self.long_window

        #compute new sign
        if (short - long) < 0:
            new_sign = -1
        elif (short - long) > 0:
            new_sign = +1

        #sets the initial sign
        if self.sign == None:
            self.sign = new_sign
            return None

        #if the sign changes the averages have crossed meaning an event should be created and added to the queue
        if (new_sign) != (self.sign):
            self.sign = new_sign
            print("averages crossed!!!!")
            return self.create_signal_event(marketEvent)

        else:
            return None

    def create_signal_event(self, marketEvent):
        date = marketEvent.date
        #decide on long or short
        if self.sign == 1:
            return SignalEvent("BUY", date, marketEvent.close)
        else:
            return SignalEvent("SELL", date, marketEvent.close)
