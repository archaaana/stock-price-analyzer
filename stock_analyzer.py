print("Starting download...")

import yfinance as yf
import pandas as pd;
import matplotlib.pyplot as plt

# 1. Download stock data
ticker = "TSLA"
data = yf.download(ticker, start="2020-01-01", end="2024-01-01")

# 2. Save to CSV
data.to_csv("stock_data.csv")

# 3. Calculate daily returns
data["Daily Return"] = data["Close"].pct_change()

# 4. Plot closing price
plt.figure(figsize=(10,5))
plt.plot(data["Close"])
plt.title(f"{ticker} Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.savefig("closing_price.png")
plt.close()

# 5. Plot daily return
plt.figure(figsize=(10,5))
plt.plot(data["Daily Return"])
plt.title(f"{ticker} Daily Returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.savefig("daily_returns.png")
plt.close()

print("Done! CSV and charts saved.")
