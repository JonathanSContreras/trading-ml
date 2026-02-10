import yfinance as yf
import pandas as pd

tickers = ["SPY", "QQQ", "AAPL", "MSFT", "TSLA"]
start_date = "2024-01-01"
end_date = "2025-02-09"

for ticker in tickers:
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    print(f"Saving data for {ticker} to CSV...")
    data.to_csv(f"../data/{ticker}_data.csv")