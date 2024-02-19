from typing import List

"""
485. Max Consecutive Ones
if num is 0, len initialize to 0, 
else increment len by 1.
Calculate the max len and return.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        res = 0
        for num in nums:
            if num == 0:
                n = 0
            else:
                n += 1
                res = max(res, n)

        return res