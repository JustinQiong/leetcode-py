from typing import List

"""
322. Coin Change
Dynamic Programming Solution:
Iterate through all the possibilities of coins to form 1 to amount.
Update the minimum number of coins in each amount.
Return dp[-1], it is the minimum coin number of amount if 
it is not infinite.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1