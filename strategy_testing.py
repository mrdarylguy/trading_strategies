#dependencies
import yfinance as yf
import pandas as pd

#Import whichever trading stategy you want to test + backtest function
from trading_strategies import macd
import backtest1

#select assets to download, can be more than 1
assets = ["BTC-USD"]
ticker = "BTC-USD"

#date ranges of data  
end_date = "2023-11-30"
start_date = "2023-07-15"
inital_capital = 10000

# #obtain data as dictionary of dataframes => {asset: DataFrame}
#Yahoo Finance
data = {}
for asset in assets:
    data[asset]=yf.download(asset, 
                            start=start_date, 
                            end=end_date, 
                            interval="1d")
    
#Polygon
data[ticker] = pd.read_csv("price_data/polygon/*******.csv")

#Feed data to the function and generate trading signals for each time step
signal_generator=macd.MovingAverageCrossoverStrategy(data[ticker], ticker,short_window=5,long_window=20)
#signal_generator=bollinger.Bollinger(data[ticker], ticker,SMA=10,SD=2)
trading_signals = signal_generator.strategy
# print(trading_signals)
signal_generator.plotting()

# perform backtest
backtest=backtest1.Backtest("BTC 5 & 20 Day Moving Averages", #Enter label of choice of strategy
                           "macd", #Enter str(name of strategy)                             
                           data[ticker], 
                           trading_signals,
                           inital_capital)
portfolio=backtest.portfolio
print(portfolio)
backtest.plotting()