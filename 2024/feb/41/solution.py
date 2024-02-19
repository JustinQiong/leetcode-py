from typing import List

"""
41. First Missing Positive
Time complexity O(n) and space complexity O(1) solution:

Use the index of array nums to mark the number existence
from 1 to n=len(nums). If meet number n, mark nums[n-1] to negative.
Check the first positive index of number in nums array. i+1 is the
first missing positive.
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for num in nums:
            m = abs(num)
            if m <= n:
                nums[m - 1] = -abs(nums[m - 1])

        for i, num in enumerate(nums):
            if num > 0:
                return i + 1

        return n + 1