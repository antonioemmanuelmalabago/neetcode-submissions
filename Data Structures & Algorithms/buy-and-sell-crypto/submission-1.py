# Objective: Find the maximum profit
# Condition: Buy at lowest and sell at highest price
# Algorithm:
# 1. Define left and right points for sliding window
# 2. Iterate through each element using right pointer
#    2.a. If left < right, compute max profit
#    2.a. Else, change left pointer vslue to right
# 3. Increment the right pointer

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        
        return maxProfit

