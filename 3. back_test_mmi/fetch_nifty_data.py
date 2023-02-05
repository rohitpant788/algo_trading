import requests, csv, yfinance, pytz, json
from datetime import datetime

NIFTY_FEAR_GREED_CSV_FILENAME = 'datasets/nifty-fear-greed-2012-2023.csv'

nifty = yfinance.Ticker("^NSEI")
START_DATE = '2012-03-12'
df = yfinance.download("^NSEI", start=START_DATE)

fear_greed_values = {}

FEAR_GREED_CSV_FILENAME = 'datasets/mmi.csv'

with open(FEAR_GREED_CSV_FILENAME,) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)  # Skip the first row
    for line in csv_reader:
        fear_greed_values[str(datetime.strptime(line[0], "%d/%m/%Y").strftime('%Y-%m-%d'))]=line[1]

with open(NIFTY_FEAR_GREED_CSV_FILENAME, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date,Open,High,Low,Close,Adj Close,Volume,Fear Greed'])
    for index, row in df.iterrows():
        try:
            writer.writerow([index.date(), row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume'], fear_greed_values[str(index.date())]])
        except Exception as e:
            print("missing {}".format(e))
            # skip rows with missing data points
            pass