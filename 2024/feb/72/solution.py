"""
72. Edit Distance
Dynamic Solution:
if words[i]==words[j]
dp[i][j]=dp[i-1][j-1]
else
dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        if n1 * n2 == 0:
            return n1 + n2

        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]

        for i in range(n1 + 1):
            dp[0][i] = i

        for j in range(n2 + 1):
            dp[j][0] = j

        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[-1][-1]
