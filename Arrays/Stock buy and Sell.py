def maxProfit(prices: list[int]) -> int:
    lowest = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < lowest:
            lowest = prices[i]
        max_profit = max(prices[i]-lowest, max_profit)
    
    return max_profit

prices = [7,1,5,3,6,4] # output 5
res = maxProfit(prices=prices)
print(res)