from typing import List

"""
2369. Check if There is a Valid Partition For The Array
Dynamic Programming Solution:
The transfer equation is:
In these two scenarios, the array has a valid partition:
1. nums[i]==nums[i-1] and nums[0:i] has valid partition
2. (nums[i]==nums[i+1]==nums[i+2] or nums[i]+2==nums[i+1]+1==nums[i+2])
and nums[0:i] has valid partition
"""


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            if (i >= 2 and dp[i - 2] and nums[i - 2] == nums[i - 1]) \
                    or (i >= 3 and dp[i - 3] and (
                    nums[i - 1] == nums[i - 2] == nums[i - 3] or nums[i - 3] + 2 == nums[i - 2] + 1 == nums[i - 1])):
                dp[i] = True

        return dp[-1]
