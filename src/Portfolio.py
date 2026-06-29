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
