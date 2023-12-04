#dependencies
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as date_format
import mplfinance as mpf
import pandas as pd
from datetime import datetime

#Import whichever trading stategy you want to test + backtest function
from trading_strategies import macd
import backtest

#select assets to download, can be more than 1
assets = ["BTC-USD"]

ticker = "BTC-USD"

#date ranges of data  
end_date = "2023-12-03"
start_date = "2023-07-01"
inital_capital = 10000

# #obtain data as dictionary of dataframes => {asset: DataFrame}
data = {}
for asset in assets:
    data[asset]=yf.download(asset, 
                            start=start_date, 
                            end=end_date, 
                            interval="1d")

#Plot indicators alongside price
data[ticker]["SMA_5"]=data[ticker]["Close"].rolling(window=5).mean()
data[ticker]["SMA_20"]=data[ticker]["Close"].rolling(window=20).mean()

# #Feed data to the function and generate trading signals for each time step
strategy=macd.MovingAverageCrossoverStrategy(short_window=5,
                                              long_window=20).generate_signals(data[ticker])
# print(strategy)

# perform backtest
backtest=backtest.Backtest(data[ticker], 
                            strategy,
                            inital_capital)

portfolio=backtest.portfolio
print(portfolio)

# plt.figure(figsize=(14, 7))
# plt.plot(portfolio['total'], label="portfolio value")
# plt.title("Portfolio value over time")
# plt.xlabel("Date")
# plt.ylabel("Portfolio value (USD)")
# plt.legend()
# plt.grid(True)
# plt.show()

#plotting price signals
# plt.figure(figsize=(14, 7))
# plt.plot(data[ticker]["Close"], label="BTC prices")
# plt.plot(data[ticker]["SMA_5"], label="5 day SMA")
# plt.plot(data[ticker]["SMA_20"], label="20 day SMA")
# plt.scatter(strategy.loc[strategy.positions==1.0].index, 
#             strategy.short_mavg[strategy.positions==1.0],
#               label="Buy Signal", 
#               marker="^", 
#               color="g", 
#               s=100)

# plt.scatter(strategy.loc[strategy.positions==-1.0].index,
#             strategy.short_mavg[strategy.positions==-1.0],
#             label="Sell Signal", 
#             marker="v", 
#             color="r",
#             s=100)
# plt.title("BTC Death Cross Strategy")
# plt.xlabel("Date")
# plt.ylabel("Price (USD)")
# plt.legend()
# plt.grid(True)
# plt.show()