from typing import List

"""
64. Minimum Path Sum
Dynamic Programming Solution:
The transfer equation is
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [0] * m
        dp[0] = grid[0][0]
        for i in range(1, m):
            dp[i] = dp[i - 1] + grid[0][i]

        for i in range(1, n):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, m):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]
