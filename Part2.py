"""
Part 2: Compute the mean and standard deviation of TSLA daily closing prices.
"""
import statistics

with open("TSLA_close.txt", "r") as f:
    prices = [float(line.strip()) for line in f if line.strip()]

mean_price  = statistics.mean(prices)
stdev_price = statistics.stdev(prices)

print(f"Stock: TSLA")
print(f"Number of trading days: {len(prices)}")
print(f"Mean closing price:     ${mean_price:.4f}")
print(f"Std dev closing price:  ${stdev_price:.4f}")
