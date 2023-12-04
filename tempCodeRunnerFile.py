backtest=backtest.Backtest(data[ticker], 
                            strategy,
                            1000)
# print(backtest.positions)
portfolio=backtest.portfolio
print(portfolio)