from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell = 0
        buy = -prices[0]
        for i in range(1, n):
            sell = max(sell, buy + prices[i] - fee)
            buy = max(buy, sell - prices[i])

        return sell
