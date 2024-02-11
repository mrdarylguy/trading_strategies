from optionlab.support import getPoP
import yfinance as yf
import numpy as np

ticker = "AAPL"
data = yf.download(ticker, 
                   start="2022-12-23", 
                   end="2023-12-23")["Adj Close"].tolist()

daily_returns = []
for i in range(1, len(data)):
    daily_pnl = round((data[i]-data[i-1])/data[i], 3)
    daily_returns.append(daily_pnl)

daily_vol = np.std(daily_returns)
annual_vol = daily_vol * np.sqrt(252)
stock_price = 193
interest_rate = 0.039
days_to_expiry = 33

pop=getPoP([[194.33, 
             205.67]],
           "black-scholes",
           stockprice=stock_price,
           volatility=annual_vol,
           interestrate=interest_rate,
           time2maturity=days_to_expiry/365)

print("Probablity of profit: "+"%.3f"%pop)