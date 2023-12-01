import pandas as pd
import numpy as np
import pandas as pd

#Class takes in 2 arguments, the shorter moving average and the longer moving average
class MovingAverageCrossoverStrategy:
    def __init__(self, short_window, long_window):
        self.short_window=short_window
        self.long_window=long_window

    #Feed dataset to signal generator
    def generate_signals(self, data):
        signals=pd.DataFrame(index=data.index)
        signals['signal']=0.0
        signals['short_mavg']=data['Close'].rolling(window=self.short_window, min_periods=1).mean() #rolling mean
        signals['long_mavg']=data['Close'].rolling(window=self.long_window, min_periods=1).mean()
        signals['signal'][self.short_window:]=np.where(signals["short_mavg"][self.short_window:]
                                                       >signals["long_mavg"][self.short_window:], 
                                                       1.0, 0.0)
        signals["positions"]=signals['signal'].diff()
        return signals