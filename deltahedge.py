import numpy as np
prices = [49, 48.12, 47.37, 50.25, 51.75, 53.12, 53, 49.88, 48.5, 
          49.88, 50.37, 52.13, 51.88, 52.87, 54.87, 54.62, 55.87, 57.25]
delta_values = [0.522, 0.458, 0.4, 0.596, 0.693, 0.774, 0.771, 0.706, 0.674, 0.787, 0.550, 
                0.413, 0.542, 0.591, 0.768, 0.759, 0.865, 0.978, 0.990, 1, 1]

delta_values = np.array(delta_values)

class Position:
    def __init__(self, current_pos_delta, 
                 option_contracts, 
                 shares_held, 
                 cash,
                 long_short_option, 
                 ):
        self.current_pos_delta = current_pos_delta
        self.option_contracts = option_contracts
        self.shares_held = shares_held
        self.cash = cash
        self.long_short_option = long_short_option
        pass

apple = Position(0, 1000, 0, 0, 'Short')

def PnL(long_short, price, quantity):
    if long_short=="Long":
        apple.cash -= price*quantity
        pass
        
    elif long_short=='Short/Sell':
        apple.cash += price*quantity
        pass

def delta_hedge(option_contracts,
                option_delta,
                shares_held,
                price
                ):
    new_pos_delta = option_contracts*option_delta*100
    delta_hedge = new_pos_delta - apple.current_pos_delta
    long_short = "Short/Sell" if delta_hedge>0 else "Long"
    shares_held += -new_pos_delta
    holdings_value = shares_held*price

    PnL(long_short=long_short, price=price, quantity=abs(int(delta_hedge)))

    print("|Delta to hedge: ", delta_hedge, "|",
          "Shares/Tokens to" ,long_short,": " ,abs(int(delta_hedge))," |", 
          "Shares Held: ", int(shares_held), " |", 
          "Value of Holdings: $", holdings_value ," |", 
          "Cash holdings: $", apple.cash, "|")
    apple.current_pos_delta = new_pos_delta
    pass

delta_values=list(-delta_values) if apple.long_short_option == 'Short' else delta_values

for (delta, price) in zip(delta_values, prices):
    delta_hedge(option_contracts=apple.option_contracts,
                option_delta=delta,
                shares_held=apple.shares_held,
                price=price)