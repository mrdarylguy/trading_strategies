from polygon import RESTClient
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from polygon_API_key import polygon_API_key

client = RESTClient(polygon_API_key)

#List of all available option
contractNames = []
for c in client.list_options_contracts(underlying_ticker="AAPL",
                                       limit=1000):
    contractNames.append(c.ticker)

OptionTicker=contractNames[200]
intradayOptionData = client.get_aggs(ticker=OptionTicker,
                                     multiplier=1,
                                     timespan = 'day',
                                     from_ = "2000-01-01",
                                     to = "2100-01-01")

df = pd.DataFrame(intradayOptionData)
df["Date"] = df['timestamp'].apply(
    lambda x: pd.to_datetime(x*1000000))
df = df.set_index("Date")
df.to_csv(f"price_data/polygon/{OptionTicker}.csv", sep=",", header=True)

plt.figure(figsize=(14, 7))
plt.plot(df["close"], label="Long Only Strategy", color='r')
plt.title(f"Closing prices of: {OptionTicker}")
plt.xlabel("Date")
plt.ylabel("Option Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

