import math
import pandas
from yahoo_fin import stock_info as si

def getStockPrice(tickerSym):
    priceLookup = si.get_live_price(tickerSym)
    floatPrice = round(float(priceLookup), 2)
    return str(floatPrice)

def getDaily(tickerSym):
    # TODO Add optional start and end dates with default values
    data = si.get_data(tickerSym)
    return data

def getWeekly(tickerSym):
    # TODO Add optional start and end dates with default values
    data = si.get_data(tickerSym, interval = '1wk')
    return data

def getMonthly(tickerSym):
    # TODO Add optional start and end dates with default values
    data = si.get_data(tickerSym, interval = '1mo')
    return data

# TODO Get dividends
# TODO Get earnings
# TODO Get market status
# TODO Get quote table

class Ticker: 
    def __init__(self, sym):
        self.symbol = sym
        try:    
            self.price = getStockPrice(self.symbol)
        except:
            self.price = "Unable to find price, check your input"
        self.daily = getDaily(self.symbol)
        self.weekly = getWeekly(self.symbol)
        self.monthly = getMonthly(self.symbol)
        
