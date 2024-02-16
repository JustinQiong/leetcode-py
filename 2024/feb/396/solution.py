from typing import List

"""
396. Rotate Function
Calculate sum by iterate through nums first.
And the sum of rotated nums can be calculated
base on the former sum.
f = f + sum - nums[n-i]*n
"""


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = 0
        n = len(nums)

        sm = 0
        for i, num in enumerate(nums):
            f += i * num
            sm += num
        res = f
        for i in range(1, n):
            f = f + sm - nums[n - i] * n
            res = max(res, f)

        return res
