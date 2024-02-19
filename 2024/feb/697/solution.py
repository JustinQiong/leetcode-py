from math import inf
from typing import List

"""
697. Degree of an Array
Use a dict to store the occurrence of each number
accompanied with the start and end index of the number.
"""


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = {}
        mx = 0
        for i, num in enumerate(nums):
            if num not in mp:
                mp[num] = (1, i, i)
            else:
                c, s, _ = mp[num]
                c += 1
                mp[num] = (c, s, i)
            ct, _, _ = mp[num]
            mx = max(mx, ct)

        res = inf
        for c, s, e in mp.values():
            if c == mx:
                res = min(res, e - s + 1)

        return res
