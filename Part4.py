"""
Part 4: Compute the maximum possible profit for TSLA in January 2023.
"""

def buy_and_sell(stock_price):
    max_profit_val  = 0
    current_max_val = 0
    best_sell_idx   = len(stock_price) - 1
    buy_idx         = -1
    sell_idx        = -1

    for i, price in enumerate(reversed(stock_price)):
        actual_i = len(stock_price) - 1 - i
        if price > current_max_val:
            current_max_val = price
            best_sell_idx   = actual_i
        potential_profit = current_max_val - price
        if potential_profit > max_profit_val:
            max_profit_val = potential_profit
            buy_idx        = actual_i
            sell_idx       = best_sell_idx

    return max_profit_val, buy_idx, sell_idx

with open("TSLA_close.txt", "r") as f:
    prices = [float(line.strip()) for line in f if line.strip()]

max_profit, buy_idx, sell_idx = buy_and_sell(prices)

print(f"Stock: TSLA")
print(f"Buy on trading day  {buy_idx + 1} at ${prices[buy_idx]:.4f}")
print(f"Sell on trading day {sell_idx + 1} at ${prices[sell_idx]:.4f}")
print(f"Maximum possible profit: ${max_profit:.4f}")
