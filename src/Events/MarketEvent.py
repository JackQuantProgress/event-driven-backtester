from .Event import Event

class MarketEvent(Event):
    """
    Handles the event of receiving a new market update with 
    OHLCV values.
    """

    def __init__(self, date, close):
        """
        Initialises the MarketEvent.
        """

        super().__init__()

        self.type = "MarketEvent"
        self.date = date
        self.close = close