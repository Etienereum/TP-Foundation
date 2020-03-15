from binance.client import Client
import pandas as pd

PUBLIC_KEY = "CU6dngaPbO2XWAKcXXiDjrKkMiOSiOI99RHVTF7bJZF46TMQOK6ogUBZISI1khBj"

# instantiate binance client with public key
client = Client(PUBLIC_KEY, "")

# pull some klines from binance api
data =  client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# create a pandas dataframe with the klines
df = pd.DataFrame(data)

print("First five rows of that data\n")
print(df.head(5))
print("Last five rows of that data\n")
print(df.tail(5))