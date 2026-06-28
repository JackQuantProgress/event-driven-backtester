# data.py

class HistoricCSVDataHandler(DataHandler):
    """
    HistoricCSVDataHandler is designed to read CSV files for
    each requested symbol from disk and provide an interface
    to obtain the "latest" bar in a manner identical to a live
    trading interface. 
    """

    def __init__(self, events, csv_dir):
        """
        Initialises the historic data handler by requesting
        the location of the CSV files and a list of symbols.

        It will be assumed that all files are of the form
        'symbol.csv', where symbol is a string in the list.

        Parameters:
        events - The Event Queue.
        csv_dir - Absolute directory path to the CSV files.
        continue_backtest - Used to end the while loop in main.
        data - A pandas data frame with all of the csv data.
        """
        self.events = events
        self.csv_dir = csv_dir
        self.continue_backtest = True
        self.data = None    

        self.read_and_store_data()
    
    def read_and_store_data(self):
        """
        Reads the csv file, converts it into a data frame and stores it in data.
        """
        pass

    def get_next_bar(self, symbol):
        """
        Returns next bar in the data csv file.
        (sybmbol, datetime, open, low, high, close, volume).
        """
        pass


    def update_bars(self):
        """
        Pushes the latest bar to the latest_symbol_data structure
        for all symbols in the symbol list.
        """
