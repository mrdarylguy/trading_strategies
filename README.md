# trading_strategies

This repo contains code that develops trading signals and backtests against them historical data for any ticker symbol of the user's choice.

![Screenshot 2023-12-01 at 11 37 13 PM](https://github.com/mrdarylguy/trading_strategies/assets/42925677/962b8de3-b7cc-441a-a2da-7eea35125529)

It also contrasts the strategy performance against a traditional "Long Only" strategy across the same time horzon.

Currently include strategies from the strategies below: 
* The Death Cross / Golden Cross (50 and 200 day moving averages) 

Currently includes API from the following sources:
* Yahoo Finance

Current structure of the repo is as follows ⬇️

Driver code is: ```strategy_testing.py```, which draws upon dependencies ```backtest.py``` and whichever chosen strategy located within ```~/strategies/```
