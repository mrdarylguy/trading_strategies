import yfinance as yf

assets = ["BTC-USD"]
data = {}
ticker = "BTC-USD"
start_date = "2023-07-01"
end_date = "2023-12-03"
interval="1d"
ticker='BTC-USD'

class DataSet: 
    def __init__(self, 
                 assets, 
                 data, 
                 ticker,
                 start_date,
                 end_date,):
        
        self.assets = assets
        self.data = data
        self.start_date = start_date
        self.end_date = end_date
        self.ticker = ticker
        self.interval = interval

    def dataset_loader(self):
        for asset in assets:
            data[asset]=yf.download(asset, 
                                    start=self.start_date, 
                                    end=self.end_date, 
                                    interval=self.interval)
            return data
        
print(DataSet.dataset_loader)
    