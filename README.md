# Systematic Trading Strategies

This repo contains code that: 

* Develops trading signals and backtests against them historical data for any ticker symbol of the user's choice.
* Profit probability of European Option Spreads for a chosen date of expiry.
* Analyzes the instantaneous order book for Exchange traded Asset (eg Binance) 

  # Systematic Trading 

![image](https://github.com/mrdarylguy/trading_strategies/assets/42925677/598671ed-ac28-43a4-a649-257c8d76e22d)


It contrasts the strategy performance against a traditional "Long Only" strategy across the same time horzon.

Currently include strategies from the strategies below: 
* The Death Cross / Golden Cross (50 and 200 day moving averages)
* Bollinger Bands 

Currently includes data from the following API:
* Polygon.io
* Yahoo Finance
* Binance

Currently includes scripts to pull the following instruments: 
* Equities
* Crypto
* Options



Current structure of the repo is as follows ⬇️

| Control Flow | Description |
| --- | --- |
| Generate historical data| ```Polygon_Hist_Data.py``` generates a CSV file into ```price_data/polygon/```|
| Select strategy | Function calls for each signal generator are found in ```CodeForStrategies.txt``` |
| Generate Signals | Trading signals are generated in the form of 1: Buy, -1: Sell, 0: Hold, and a CSV file is generated in ```/results/.../trading_signals.csv```. |
| Backtesting | The signal generation function returns a dataframe of 1, -1, 0, which is passed to the ```backtest.py``` function, which returns another csv in ```/results/.../strategy_performance.csv```. |
| Post review |CSV files of portfolio values against time and each indicators are stored in ```/results/``` enabling investigation into underperformance|
| Plotting | A plot of the relative performance is generated in .png format in ```plots/.../****.png```. | 

 # Profit probability of Option Spreads
 Navaigate to the file ```options_lab.py```. 

| Input  | Description |
| --- | --- |
| start, end | start and end dates for a 1 year historical price data |
| stock_price | current price of chosen security |
| interest_rate | the current risk free rate of return |
| days_to_expiry | business days til option expiration |
| lower_bound, upper_bound | set the price range to calculate |
| pricing_model | default is "black_scholes" |

# Order Book skew
 Navaigate to the file ```binance_data.py```. 
| Input  | Description |
| --- | --- |
| ticker | ticker symbol of the security |
| dist_from_centre | confine analysis to within X percentage of the mid-price of the order book|


![image](https://github.com/mrdarylguy/trading_strategies/assets/42925677/9c19064f-18de-40f6-8161-08186234e5f1)

 




 
 
 
