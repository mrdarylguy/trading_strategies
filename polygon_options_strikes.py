from polygon import RESTClient
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()
client = RESTClient(os.getenv("POLYGON-API-KEY"))

#List of all available option
contractNames = []
strike_prices = []

for c in client.list_options_contracts(underlying_ticker="AAPL",limit=1000):
    contractNames.append(c.ticker)

#filter for calls or puts 
OptionTicker = list(filter(lambda ticker: "C" in ticker, contractNames))
#filter for desired date YYMMDD
OptionTicker = list(filter(lambda ticker: "260116" in ticker, contractNames))

for ticker in OptionTicker:
    strike_prices.append(int(ticker[15:18]))

print(strike_prices)