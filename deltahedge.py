prices = [49, 48.12, 47.37, 50.25, 51.75, 53.12, 53, 51.87, 53, 49.88, 48.5, 50.37, 52.13, 51.88, 52.87, 54.87, 54.62, 55.87, 57.25]
delta_values = [0.522, 0.458, 0.4, 0.596, 0.693, 0.774, 0.771, 0.706, 0.674, 0.787, 0.550, 0.413, 0.542, 0.591, 0.768, 0.759, 0.865, 0.978, 0.990, 1, 1]

class Position:
    def __init__(self, current_pos_delta, option_contracts, shares_held):
        self.current_pos_delta = current_pos_delta
        self.option_contracts = option_contracts
        self.shares_held = shares_held
        pass

apple = Position(0, 1000, 0)


def delta_hedge(option_contracts,
                option_delta,
                shares_held
                ):
    new_pos_delta = option_contracts*option_delta*100
    delta_hedge = new_pos_delta - apple.current_pos_delta
    long_short = "Short/Sell" if delta_hedge<0 else "Long"
    shares_held += new_pos_delta

    print("|delta to hedge: ", delta_hedge, "|",
          "Shares/Tokens to" ,long_short,": " ,abs(int(delta_hedge))," |", 
          "Shares Held: ", int(shares_held), " |")
    apple.current_pos_delta = new_pos_delta
    pass

for delta in delta_values[:3]:
    delta_hedge(option_contracts=apple.option_contracts,
                option_delta=delta,
                shares_held=apple.shares_held)