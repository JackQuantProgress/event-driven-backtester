from .Event import Event

class SignalEvent(Event):
    """
    Handles the event of sending a Signal from a Strategy object.
    This is received by a Portfolio object and acted upon.
    """
    
    def __init__(self, signal_type, date, current_price):
        """
        Initialises the SignalEvent.

        Parameters:
        symbol - The ticker symbol, eg: SPY.
        datetime - The timestamp at which the signal was generated.
        signal_type - 'LONG' or 'SHORT'.
        """
        self.type = "SignalEvent"
        self.date = date
        self.signal_type = signal_type
        self.current_price = current_price