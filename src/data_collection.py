import yfinance as yf
import pandas as pd

tickers = ["SPY", "QQQ", "AAPL", "MSFT", "TSLA"]
start_date = "2024-01-01"
end_date = "2026-02-09"

for ticker in tickers:
    print(f"Downloading data for {ticker}...")
    # Download historical data for the specified ticker and date range
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    print(f"Saving data for {ticker} to CSV...")
    
    data = data.reset_index()  # Reset index to have 'Date' as a column
    data = data.droplevel(1, axis=1)  # Drop the multi-level column index

    # Save the data to a CSV file ensuring it does not include the index
    data.to_csv(f"../data/{ticker}_data.csv", index=False)

print("Data collection complete.")