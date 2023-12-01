import pandas as pd
class Backtest:
    def __init__(self,
                 data,
                 signals, 
                 inital_capital,   
                 ):
        self.data = data
        self.signals = signals
        self.initial_capital = inital_capital
        self.initital_holdings = inital_capital/self.data["Close"][0]
        self.positions = self.generate_signals()
        self.portfolio = self.backtest_portfolio()

    def generate_signals(self):
        positions = self.signals
        positions=pd.DataFrame(index=self.signals.index) #Empty dataframe and populate it with timestamp indexing
        positions['action'] = self.signals['signal']
        return positions

    def backtest_portfolio(self):
        portfolio = self.positions.diff()
        portfolio["price"] = self.data["Close"]
        portfolio["Long Only"] = portfolio["price"]*self.initital_holdings
        # portfolio["Long Only"] = 
        # pos_diff=self.positions.diff() #calculate difference btw each element
        # portfolio['holdings']=(self.positions.multiply(self.data["Close"], axis=0)).sum(axis=1)
        # portfolio["cash"]=self.initial_capital-(pos_diff.multiply(self.data["Close"],axis=0)).sum(axis=0).cumsum()
        # portfolio['total'] = portfolio['cash']+portfolio["holdings"]
        # portfolio['returns']=portfolio["total"].pct_change(fill_method=None)
        return portfolio
            