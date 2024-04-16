def maxProfit(prices):
    profit, min_price = 0, prices[0]
    for price in prices[1:]:
        if price > min_price:
            profit += price - min_price
        min_price = price
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))