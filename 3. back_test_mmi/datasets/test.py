
import pandas_datareader.data as web

# Get the Nifty data
data = web.DataReader('^NSEI', data_source='yahoo')
print(data)