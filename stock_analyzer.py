print("Starting download...")

import yfinance as yf
import pandas as pd;
import matplotlib.pyplot as plt

ticker = "TSLA"
data = yf.download(ticker, start="2020-01-01", end="2024-01-01")

data.to_csv("stock_data.csv")

data["Daily Return"] = data["Close"].pct_change()

plt.figure(figsize=(10,5))
plt.plot(data["Close"])
plt.title(f"{ticker} Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.savefig("closing_price.png")
plt.close()

plt.figure(figsize=(10,5))
plt.plot(data["Daily Return"])
plt.title(f"{ticker} Daily Returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.savefig("daily_returns.png")
plt.close()

print("Done! CSV and charts saved.")
