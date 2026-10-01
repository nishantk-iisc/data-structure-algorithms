prices = [7, 1, 5, 3, 6, 4]

# Output: profit => 5 ---> buy on day 2 (price = 1) and sell on day 5 (price = 6) ==> max profit = 6 - 1 => 5
# return 0 -> no profit

def maxProfit(prices):
    # # Brute force -> all the pair (i, j) returm max profit
    # # Time: O(n^2)
    # max_profit = float('-inf')
    # for i in range(len(prices)):
    #     for j in range(i+1, len(prices)):
    #         profit = prices[j] - prices[i]

    #         if profit > 0:
    #             max_profit = max(max_profit, profit)
    
    # return max_profit if max_profit > float('-inf') else 0

    # optimized solution
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


print(maxProfit(prices))
