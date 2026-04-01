# Best Time to Buy and Sell Stock

prices = [7, 1, 5, 3, 6, 4]

def max_profit(prices):
    # Handle empty list prices
    if not prices:
        return 0
    # Initialize variables to track the minimum price and maximum profit
    min_price = prices[0]
    max_profit = 0
    # Loop through the list of prices
    for price in prices:
        # Update the minimum price if the current price is lower than the minimum price
        if price < min_price:
            min_price = price
        # Otherwise, Try selling
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit

print(max_profit(prices))