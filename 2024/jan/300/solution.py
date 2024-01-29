from typing import List

"""
300. Longest Increasing Subsequence
Dynamic Programming Solution:
the longest length of increasing subsequence on 
index i will be the longest length of increasing subsequence
from 0 to i-1 plus one if the number on index i is greater 
than the element on the index from o to i-1.
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = []
        res = 1
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])

        return res
