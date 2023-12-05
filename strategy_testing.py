#dependencies
import yfinance as yf

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
strategy=macd.MovingAverageCrossoverStrategy(data[ticker], 
                                             ticker,
                                             short_window=5,
                                             long_window=20).strategy

macd.MovingAverageCrossoverStrategy(data[ticker], 
                                            ticker,
                                            short_window=5,
                                            long_window=20).plotting()

# perform backtest
backtest=backtest.Backtest(data[ticker], 
                            strategy,
                            inital_capital)

portfolio=backtest.portfolio
backtest.plotting()