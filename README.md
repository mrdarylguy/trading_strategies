# Systematic Trading Strategies

This repo contains code that develops trading signals and backtests against them historical data for any ticker symbol of the user's choice.

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
