# Goal: Find the maximum profit
# Maximum profit = buy low, sell high
# 1. Find the min price, 2. Find the max price
# Clue: If not profittable, set max profit to 10
# Restriction: time

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1 # L-buy, R-sell
        maxProfit = 0

        while R < len(prices):
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
                maxProfit = max(maxProfit, profit)
            else:
                L = R
            R += 1
        
        return maxProfit