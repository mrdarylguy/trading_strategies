import pandas as pd
import random
import math

prices=[]
action=[]                            #buy, sell or hold
portfolio_value = []                 #total portfolio value
holdings = []                        #units of security
capital = 100

prev_order = 0

prices = [0.24, 0.36, 0.66, 0.56, 0.93, 0.93, 0.84, 0.81, 0.91, 0.19, 0.72, 
          0.35, 0.35, 0.8, 0.48, 0.81, 0.74, 0.65, 0.08, 0.66, 0.59, 0.16, 
          0.38, 0.49, 0.66, 0.28, 0.84, 0.3, 0.14, 0.45]

for i in range(len(prices)):
    if 0.2<prices[i]<0.4:
        action.append(1)                 
    elif prices[i]>0.7:
        action.append(-1)
    else:
        action.append(0)

for i in range(len(action)):
    if action[i]==1 and prev_order!=1:                
      holdings.append(round(capital/prices[i], 2))
      prev_order=1                                    
      capital=0                       

    elif action[i]==0:                                
       holdings.append(round(holdings[-1], 2))                    
    
    elif action[i]==-1 and prev_order!=-1:           
      capital=holdings[-1]*prices[i]                
      holdings.append(0)
      prev_order = -1       

for i in range(len(holdings)): 
   if holdings[i]>0:
      portfolio_value.append(round(holdings[i]*prices[i], 2))
   else:
      portfolio_value.append(round(portfolio_value[-1], 2))                          
       

df = pd.DataFrame(list(zip(prices, action, holdings, portfolio_value)), columns=['Prices', 'Action', 'Holdings', 'Portfolio Value'])
df1=df["Prices"].values.tolist()
print(df1)