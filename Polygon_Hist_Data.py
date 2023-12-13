import requests
import pandas as pd

from datetime import date, datetime, timedelta
from dateutil.tz import tzlocal
import time

def pull_1m_data(ticker, 
                 day,
                 multiplier,
                 timespan,
                 limit,
                 sort,
                 ):
    polygon_api_key = "***********************" #Input your own API Key
    polygon_rest_baseurl = "https://api.polygon.io/v2/"

    #Pull Crypto data
    ticker = "X:"+ ticker
    start_time = datetime.combine(day, datetime.min.time())
    end_time = start_time+timedelta(days=1)
    start_time = int(start_time.timestamp()*1000)
    end_time = int(end_time.timestamp()*1000)-1
    
    request_url = f"{polygon_rest_baseurl}aggs/ticker"+\
                  f"/{ticker}/range/{multiplier}/{timespan}/{start_time}/{end_time}?"+\
                  f"adjusted=true&sort={limit}&limit={limit}&"+\
                  f"apiKey={polygon_api_key}"
    
    data = requests.get(request_url).json()

    if "results" in data:
        return data["results"]
    else:
        raise Exception("API Call failed")
    

def timestamp_convert(x):
    dtUTC = datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S')
    local_time = dtUTC + timedelta(hours=8)
    return local_time


day = date(year=2023, month=11, day=30)
bars = []
days_of_data = 2
ticker = "BTCUSD"

for i in range(days_of_data):
    bars += pull_1m_data(ticker, 
            day,
            1,
            "minute",
            40000,
            "asc"
            )
    
    day -= timedelta(days=1)
    # Input mandatory time delay as free version allows max 5 API call/minute
    # time.sleep(10)

df = pd.DataFrame(bars)
df["date"] = pd.to_datetime(df['t'], unit="ms")
df = df[["date", "o", "h", "c", "l","v"]]
df.columns = ["time", "open", "high", "low", "close", "volume"]
df['time'] = df["time"].apply(timestamp_convert)
df = df.sort_values("time")
df.to_csv(f"price_data/polygon/{ticker}.csv", sep=",", header=True)