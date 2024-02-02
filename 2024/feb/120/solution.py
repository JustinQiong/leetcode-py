from typing import List

"""
120. Triangle
Dynamic Programming Solution:
The transfer equation is
dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        return min(dp[-1])
