from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
import mplfinance
import matplotlib.pyplot as plt
import numpy as np
import math

apikey = 'Vh6eKEztfDTPuzf1oscfSVhley5oJYQX8SoXhOsgpW93DC97Wi5mlsAliGInEk4D'
secret = 'utTivLaLCGGeYeN3jcT0xnjLQVbMkEEz2SAFjkj2T5e7b5lBRsSIeLkOHOmmc5f2'
client = Client(apikey, secret)
tickers = pd.DataFrame(client.get_all_tickers())
tickers.set_index("symbol", inplace=True)

#Ticker
ticker = "SOLUSDC"

#Latest Price
current_price = float(tickers.loc[ticker]["price"])

#Market depth
depth = client.get_order_book(symbol=ticker)
bids = pd.DataFrame(depth["bids"], columns=["bid price", "bid volume"]).astype(float).round(2).iloc[::-1]
asks = pd.DataFrame(depth["asks"], columns=["ask price", "ask volume"]).astype(float).round(2)

#timestamp
timestamp=depth["lastUpdateId"]


#Order book display limit
dist_from_center = 0.05
lowest_displayed = math.floor(current_price*(1-dist_from_center))
highest_displayed = math.ceil(current_price*(1+dist_from_center))

plt.title(f"Binance order book for {ticker}; timestamp: {timestamp}")
bid_plot = plt.bar(bids["bid price"], bids["bid volume"], color="green")
ask_plot = plt.bar(asks["ask price"], asks["ask volume"], color="red")
plt.xticks(np.arange(lowest_displayed, 
                     highest_displayed, 
                     1
                     ))
plt.xlim(lowest_displayed, highest_displayed)
plt.xticks(rotation=45)
plt.ylim(0, 150) #arbitrarily chosen upper ylimit
mid_price_plot = plt.axvline(x = current_price, color = 'b', label = 'center price')
plt.grid(True)
plt.legend(handles = [bid_plot, ask_plot, mid_price_plot],
           labels = ["bids", "asks", "mid_price"],
           loc='upper right', prop={"size":10})
plt.show()