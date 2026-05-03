"""
Part 3: Generate a line graph of TSLA daily closing prices.
"""
import matplotlib.pyplot as plt

with open("TSLA_close.txt", "r") as f:
    prices = [float(line.strip()) for line in f if line.strip()]

n    = len(prices)
days = list(range(1, n + 1))

plt.figure(figsize=(10, 5))
plt.plot(days, prices, marker="o", markersize=4, linewidth=1.5, color="steelblue")
plt.title("TSLA Closing Price")
plt.xlabel("Trading Day (January 2023)")
plt.ylabel("Closing Price ($)")
plt.xticks(days)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("TSLA_closing_price.png", dpi=150)
plt.show()
print("Graph saved as TSLA_closing_price.png")
