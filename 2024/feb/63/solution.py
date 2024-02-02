from typing import List
"""
63. Unique Paths II
Dynamic Programming Solution:
The transfer equation is
dp[i][j]= dp[i-1][j] + dp[i][j-1]
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [0] * m
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j != 0:
                    dp[j] = dp[j-1] + dp[j]

        return dp[-1]
