from typing import List

"""
2917. Find the K-or of an Array
Check each num in nums if (num >> i) & 1 > 0,
If count of 1 bit in position i is >= k, res |= 1 << i.
Return res.
"""
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(31):
            count = sum(1 for num in nums if ((num >> i) & 1) > 0)
            if count >= k:
                res |= 1 << i
        return res