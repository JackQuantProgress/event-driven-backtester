
class MarketEvent(Event):
    """
    Handles the event of receiving a new market update with 
    OHLCV values.
    """

    def __init__(self):
        """
        Initialises the MarketEvent.
        """
        self.type = 'MARKET'