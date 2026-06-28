from .Event import Event

class MarketEvent(Event):
    """
    Handles the event of receiving a new market update with 
    OHLCV values.
    """

    def __init__(self, timestamp, close):
        """
        Initialises the MarketEvent.
        """

        super().__init__()

        self.type = "MarketEvent"
        self.timestamp = timestamp
        self.close = close