from typing import List

"""
238. Product of Array Except Self
Iterate from left to calculate the product on the left.
Then iterate from right to calculate the product on the right.
Multiple them together to calculate the product of array except self.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * right
            right *= nums[i]

        return res