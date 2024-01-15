from typing import List

'''
714. Best Time to Buy and Sell Stock with Transaction Fee
Dynamic Programming Solution:
The maximum profit of day n has two conditions:
1. day n-1 has stock in hand
2. day n-1 has no stock in hand
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell = 0
        buy = -prices[0]
        for i in range(1, n):
            sell = max(sell, buy + prices[i] - fee)
            buy = max(buy, sell - prices[i])

        return sell
