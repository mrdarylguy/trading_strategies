import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Bollinger:
    def __init__(self, data, ticker, SMA, SD,):
        self.data = data
        self.ticker = ticker
        self.day_SMA = SMA
        self.num_SD = SD
        self.strategy = self.generate_signals()
        pass

    def generate_signals(self):
        signals=pd.DataFrame(index=self.data.index)
        signals["price"] = self.data["Close"]
        signals[str(self.day_SMA)+' day SMA']=self.data['Close'].rolling(self.day_SMA).mean() #rolling mean
        signals[str(self.num_SD)+" x SD"] = self.num_SD * self.data['Close'].rolling(self.num_SD).std()
        signals["upper Band"] = signals[str(self.day_SMA)+' day SMA'] + signals[str(self.num_SD)+" x SD"]
        signals["lower Band"] = signals[str(self.day_SMA)+' day SMA'] - signals[str(self.num_SD)+" x SD"]
        signals.dropna(inplace=True)
        def action(price, lower_band, upper_band):
            if price<lower_band:
                return 1.0 
            elif price>upper_band:
                return -1.0
            else: 
                return 0 
        signals["signal"] = np.vectorize(action)(signals["price"], signals["lower Band"], signals["upper Band"])
        signals.to_csv("results/bollinger/trading_signals.csv", sep=",", header=True)
        return signals.fillna(0)
        pass

    def plotting(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.strategy["price"], label="Price")
        plt.plot(self.strategy["upper Band"], label="Upper Band")
        plt.plot(self.strategy["lower Band"], label="Lower")
        plt.scatter(self.strategy.loc[self.strategy.signal==1.0].index, 
                    self.strategy.price[self.strategy.signal==1.0],
                    label="Buy Signal", 
                    marker="^", 
                    color="g", 
                    s=100)

        plt.scatter(self.strategy.loc[self.strategy.signal==-1.0].index,
                    self.strategy.price[self.strategy.signal==-1.0],
                    label="Sell Signal", 
                    marker="v", 
                    color="r",
                    s=100)
        plt.title(str(self.ticker)+": Bollinger Bands at "+str(self.num_SD)+" Standard Deviations")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.savefig("plots/bollinger/trading_signals.png")
        pass