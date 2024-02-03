"""
97. Interleaving String
Dynamic Programming Solution:
The transfer equation is
dp[i][j] = (dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]) or (
                        dp[i - 1][j] and s2[i - 1] == s3[i + j - 1])
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False

        dp = [[False] * (n1 + 1) for _ in range(n2 + 1)]
        dp[0][0] = True

        for i in range(1, n1 + 1):
            dp[0][i] = dp[0][i - 1] and s1[i - 1] == s3[i - 1]

        for j in range(1, n2 + 1):
            dp[j][0] = dp[j - 1][0] and s2[j - 1] == s3[j - 1]

        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                dp[i][j] = (dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]) or (
                        dp[i - 1][j] and s2[i - 1] == s3[i + j - 1])

        return dp[-1][-1]
