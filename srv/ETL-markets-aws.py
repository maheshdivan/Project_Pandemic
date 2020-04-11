import pandas as pd
from sqlalchemy import create_engine

# pip install alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Obtain free api key from alphavantage.co
api_key = "5GHY1AE5BGE4O8HT"
tickers = ["DJI", "^GSPC", "^FTSE", "^HSI", "^N225"]

# Be sure to update rds_connection_string with database connection info
# Alphavantage limits API usage to 5 requests per minute

rds_connection_string = "postgres:postgres@database-1.cpnwuinodiya.us-east-1.rds.amazonaws.com:5432/market_data"
engine = create_engine(f'postgresql://{rds_connection_string}')

# If index_table already exists, delete it
with engine.connect() as connection:
    result = connection.execute("DROP TABLE IF EXISTS index_table;")

# function to append each dataframe to SQL database

def writeData(data): 
    data.to_sql(name='index_table', con=engine, if_exists='append', index=False)
    data.to_csv('out.csv', index=False)
    
# Load TimeSeries object and unpack Alphavantage timeseries into dataframe
# Rename columns for easier reading and reset index value

ts = TimeSeries(key=api_key, output_format='pandas')
for ticker in tickers:
    data, metadata = ts.get_daily(symbol=ticker, outputsize='compact')
    data['ticker'] = ticker
    data = data.rename(columns={"date" : "timestamp", "1. open": "open", "2. high" : "high", "3. low": "low", "4. close" : "close", "5. volume" : "volume"})
    data['change'] = data.groupby('ticker').close.pct_change()
    data = data.reset_index()
    writeData(data)