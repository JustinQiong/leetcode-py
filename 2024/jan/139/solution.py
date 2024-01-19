from typing import List

"""
139. Word Break
Dynamic Programming Solution:
Iterate all the substring of s.
Store the wordDict in a set.
Check if the both the substring is in the set and the prefix part
of s str is consist of the word in the set. If it is, mark dp[i]
to True otherwise False. Return dp[-1], it is the result of if 
str s can be broke into words in wordDict or not.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        st = set()
        for word in wordDict:
            st.add(word)

        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in st:
                    dp[j] = True

        return dp[-1]