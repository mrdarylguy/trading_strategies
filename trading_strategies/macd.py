import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Class takes in 4 arguments, data set, ticker name, the shorter moving average and the longer moving average
class MovingAverageCrossoverStrategy:
    def __init__(self, data, ticker, short_window, long_window):
        self.data = data
        self.ticker = ticker
        self.short_window=short_window
        self.long_window=long_window
        self.strategy = self.generate_signals()

    #Feed dataset to signal generator
    def generate_signals(self):
        signals=pd.DataFrame(index=self.data.index)
        signals['positions']=0.0
        signals['short_mavg']=self.data['Close'].rolling(window=self.short_window, min_periods=1).mean() #rolling mean
        signals['long_mavg']=self.data['Close'].rolling(window=self.long_window, min_periods=1).mean()
        signals['positions'][self.short_window:]=np.where(signals["short_mavg"][self.short_window:]
                                                       >signals["long_mavg"][self.short_window:], 
                                                       1.0, 0.0)
        signals["signal"]=signals['positions'].diff()
        signals.to_csv("results/macd/results.csv", sep=",", header=True)
        return signals
    
    def plotting(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.data["Close"], label=self.ticker+" prices")
        plt.plot(self.strategy["short_mavg"], label=str(self.short_window)+" day SMA")
        plt.plot(self.strategy["long_mavg"], label=str(self.long_window)+" day SMA")
        plt.scatter(self.strategy.loc[self.strategy.signal==1.0].index, 
                    self.strategy.short_mavg[self.strategy.signal==1.0],
                    label="Buy Signal", 
                    marker="^", 
                    color="g", 
                    s=100)
        plt.scatter(self.strategy.loc[self.strategy.signal==-1.0].index,
                    self.strategy.short_mavg[self.strategy.signal==-1.0],
                    label="Sell Signal", 
                    marker="v", 
                    color="r",
                    s=100)
        
        plt.title(str(self.ticker)+" "+str(self.short_window)+" & "+str(self.long_window)+" day MAVG")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.savefig("plots/macd/trading_signals.png")