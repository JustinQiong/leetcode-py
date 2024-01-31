from typing import List

"""
2808. Minimum Seconds to Equalize a Circular Array
Use a map to record each distinct number and the index 
of the number.
Find the maximum gap between each distinct number 
from index i to j. The seconds takes to equalize is (j-i)/2.
Calculate the minimum seconds it takes to equalize all 
the numbers into that target number.
"""

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        mp = {}
        for i, num in enumerate(nums):
            if num not in mp:
                mp[num] = []
            mp[num].append(i)

        n = len(nums)
        res = n + 1

        for _, ides in mp.items():
            secs = 0
            ides.append(ides[0] + n)
            for i in range(1, len(ides)):
                secs = max(secs, (ides[i] - ides[i - 1]) >> 1)
            res = min(res, secs)

        return res
