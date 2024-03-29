def maxProfit(prices):
    i = 0
    profit = 0
    min_price = 0
    max_profit = 0
    while i < len(prices):
        if prices[i] > min_price:
            max_profit += max(profit, prices[i] - min_price)
            min_price = prices[i]
            profit = 0
        i += 1
    return max_profit

prices = [1,2,3,4,5]
print(maxProfit(prices))