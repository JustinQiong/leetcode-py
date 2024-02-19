from math import inf
from typing import List

"""
414. Third Maximum Number
Use variable first, second, third 
to record the 1st, 2nd and 3rd maximum number.
Update them through iterating the nums list.
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        first, second, third = -inf, -inf, -inf

        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif second < num < first:
                second, third = num, second
            elif third < num < second:
                third = num

        return third if third != -inf else first