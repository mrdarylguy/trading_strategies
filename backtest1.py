import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
class Backtest:
    def __init__(self,
                 label,
                 strategy_name,
                 data,
                 signals, 
                 inital_capital,   
                 ):
        
        self.label = label
        self.name = strategy_name
        self.data = data
        self.signals = signals
        self.initial_capital = inital_capital
        self.initital_holdings = inital_capital /self.data["Close"].iloc[0]
        self.capital = self.initial_capital
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
        portfolio = self.positions
        portfolio["Price"] = self.data["Close"]
        portfolio["Long Only"] = (portfolio["Price"]*self.initital_holdings)
        portfolio["Holdings"] = 0
        portfolio["Portfolio Value"] = 0
        portfolio["Portfolio Value"].iloc[0] = self.initial_capital #Portfolio values

        portfolio["Action"]=portfolio["Action"].replace(to_replace=2.0, value=1.0)
        portfolio["Action"]=portfolio["Action"].replace(to_replace=-2.0, value=-1.0)
        portfolio["Action"]=portfolio["Action"].fillna(0.0)
        # for index, row in portfolio.iterrows():
        #     self.price = row["Price"]

        #     #Forbid selling w/o owning
        #     if row["Action"] == -1.0 and self.holdings==0:
        #         portfolio.at[index, "Portfolio Value"] = self.capital
        #         portfolio.at[index, "Holdings"] = self.holdings
        #         pass

        #     #Forbid buying w zero capital 
        #     elif row["Action"] == 1.0 and self.capital==0:
        #         portfolio.at[index, "Holdings"] = self.holdings
        #         portfolio.at[index, "Portfolio Value"] = self.holdings*self.price
        #         pass

        #     # Execute Buy Order
        #     elif row["Action"] == 1.0 and self.capital>0:
        #         #Obtain units of security
        #         self.holdings = self.capital/self.price
        #         portfolio.at[index, "Holdings"] = self.holdings
        #         portfolio.at[index, "Portfolio Value"] = self.capital
        #         self.capital=0
        #         self.prev_order=1.0
        #         pass
            
            # #Excute Sell Order
            # elif row["Action"] == -1.0 and self.holdings>0:
            #     #liquidate positions
            #     self.capital = self.holdings*self.price
            #     portfolio.at[index, "Portfolio Value"] = self.capital
            #     portfolio.at[index, "Holdings"] = 0
            #     self.holdings = 0
            #     self.prev_order = -1.0
            #     pass

        #     # Hold
            # elif row["Action"] == 0:
            #     if self.holdings == 0 and self.capital>0:
            #         portfolio.at[index, "Portolio Value"] = self.capital
            #         portfolio.at[index, "Holdings"] = self.holdings 
            #         pass
            #     elif self.capital == 0 and self.holdings>0: 
            #         portfolio.at[index, "Holdings"] = self.holdings
            #         portfolio.at[index, "Portolio Value"] = self.holdings*self.price
            #         pass

        #         pass
            

        portfolio_ = {}
        for col in portfolio.columns:
            portfolio_[col] = portfolio[col].values.tolist() 
        #Convert to dictionary of lists for ease of manipulation

        for i in range(1, len(portfolio_["Action"])):
            self.price = portfolio_["Price"][i]

            #Forbid selling w/o owning 
            if portfolio_["Action"][i] == -1.0 and self.holdings == 0:
                portfolio_["Portfolio Value"][i] = self.capital
                portfolio_["Holdings"][i] = self.holdings
                pass
            
            #Forbid buying if zero capital
            elif portfolio_["Action"][i] == 1.0 and self.capital == 0:
                portfolio_["Holdings"][i] = self.holdings
                portfolio_["Portfolio Value"][i] = self.holdings * self.price
                pass

            #Execute buy order
            elif portfolio_["Action"][i] == 1.0 and self.capital>0:
                #Update holdings
                self.holdings = self.capital/self.price
                portfolio_["Holdings"][i] = self.holdings

                #At point of purchase, portfolio value = commited capital
                portfolio_["Portfolio Value"][i] = self.capital
                #idle capital = 0
                self.capital = 0
                self.prev_order = 1.0
                pass

            # Execute sell order 
            elif portfolio_["Action"][i] == -1.0 and self.holdings>0:
                #idle capital is created, equivalent to realised value
                self.capital = self.holdings*self.price
                #portfolio value = realised value 
                portfolio_["Portfolio Value"][i] = self.capital
                #Exit holdings
                self.holdings = 0
                portfolio_["Holdings"][i] = self.holdings
                self.prev_order=-1.0
                pass
                # portfolio_["Holdings"][i] = self.holdings
                # self.capital = portfolio_["Holdings"][i]*self.price #Liquidate at market price
                # portfolio_["Portfolio Value"][i] = self.capital
                # self.holdings = 0
                # self.prev_order = -1.0
                # pass

            #Hold 
            elif portfolio_["Action"][i] == 0:
                if self.capital == 0 and self.holdings>0: #Hold following a buy order
                    #Holdings remain constant
                    portfolio_["Holdings"][i] = self.holdings
                    #portfolio value = holdings * price
                    portfolio_["Portfolio Value"][i] = self.holdings*self.price 
                    pass

                if self.holdings == 0 and self.capital>0: #Following sell order
                    #Portfolio value is equivalent to cash
                    portfolio_["Portfolio Value"][i] = self.capital
                    #Holdings remain constant at zero
                    portfolio_["Holdings"][i] = self.holdings
                    pass
        
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

        portfolio.round(2).to_csv("results/"+str(self.name)+"/strategy_performance.csv", sep=",", header=True)
        return portfolio.round(2)
    
    def plotting(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.portfolio["Long Only"], label="Long Only Strategy", color='r')
        plt.plot(self.portfolio["Portfolio Value"], label="Activly Traded Strategy", color="b")
        plt.title("Relative Performance of Actively traded Strategy: "+ str(self.label))
        plt.xlabel("Date")
        plt.ylabel("Portfolio Value (USD)")
        plt.legend()
        plt.grid(True)
        plt.savefig("plots/"+str(self.name)+"/strategy_performance.png")
        pass