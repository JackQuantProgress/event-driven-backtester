from Events.FillEvent import FillEvent

class ExecutionHandler(object):
    """
    Handles interaction with the brokerage.
    """
    def __init__(self):
        self.date = None
        self.quantity = None
        self.direction = None
        self.fill_price = None

    def handle_order_event(self, event):
        self.quantity = event.quantity
        self.direction = event.direction
        self.fill_price = event.share_price * self.quantity
        self.date = event.date

        return FillEvent(self.date, self.quantity, self.direction, self.fill_price)

