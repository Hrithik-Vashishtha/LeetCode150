def maxProfit(prices):
    profit, min_price = 0, prices[0]
    for price in prices:
        if price <= min_price:
            min_price = price
        else:
            profit += (price - min_price)
            min_price = 999999
    return profit
prices = [1,2,3,4,5]
print(maxProfit(prices))