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
        self.initital_holdings = inital_capital /self.data["Close"].iloc[0]

        self.capital = self.initial_capital  #initialize capital and 
        self.holdings = 0

        self.prev_order = 0
        self.positions = self.generate_signals()
        self.portfolio = self.backtest_portfolio()

    def generate_signals(self):
        positions = self.signals
        positions=pd.DataFrame(index=self.signals.index) #Empty dataframe and populate it with timestamp indexing
        positions['Action'] = self.signals['signal']
        return positions

    def backtest_portfolio(self):
        portfolio = self.positions.diff()
        portfolio["Price"] = self.data["Close"]
        portfolio["Long Only"] = (portfolio["Price"]*self.initital_holdings)
        portfolio["Holdings"] = 0
        portfolio["Portfolio Value"] = 0
        portfolio["Portfolio Value"].iloc[0] = self.initial_capital #Portfolio values

        portfolio_ = {}
        for col in portfolio.columns:
            portfolio_[col] = portfolio[col].values.tolist() 
        #Convert to dictionary of lists for ease of manipulation
        
        for i in range(1, len(portfolio_["Action"])):
            # Execute buy order
            if portfolio_["Action"][i] == 1.0 and self.prev_order!= 1.0:
                # Obtain units of security
                portfolio_["Holdings"][i] = round(self.initial_capital/portfolio_["Price"][i], 2)
                # Obtain portfolio value  = holdings * current price
                portfolio_["Portfolio Value"][i] = round(portfolio_["Holdings"][i]*portfolio_["Price"][i], 2)
                self.prev_order = 1.0
                self.capital = 0 

            # Execute sell order 
            elif portfolio_["Action"][i] == -1.0 and self.prev_order != -1.0:
                self.capital = portfolio_["Holdings"][i-1]*portfolio_["Price"][i]
                portfolio_["Portfolio Value"][i] = self.capital
                portfolio_["Holdings"][i] = 0
                self.prev_order = -1.0

            elif portfolio_["Action"][i] == 0: 
                # Hold
                portfolio_["Holdings"][i] = portfolio_["Holdings"][i-1]
                portfolio_["Portfolio Value"][i] = portfolio_["Holdings"][i]*portfolio_["Price"][i]

        
        #Convert back to dictionary
        portfolio = pd.DataFrame(list(zip(portfolio_["Action"], 
                                      portfolio_["Price"],
                                      portfolio_["Long Only"],
                                      portfolio_["Holdings"],
                                      portfolio_["Portfolio Value"])), 

                                      columns=["Action", 
                                               "Price", 
                                               "Long Only", 
                                               "Holdings", 
                                               "Portfolio Value"],
                                               
                                               index=self.signals.index)
        
        return portfolio.round(2)
            