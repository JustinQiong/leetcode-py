from heapq import heappop, heappush
from typing import List

"""
373. Find K Pairs with Smallest Sums
minimum heap solution:
sum nums1[i]+nums2[j] from 0 to the last element.
pop out the minimum element in the heap within k size.
"""


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        m = len(nums1)
        n = len(nums2)
        hp = [(nums1[i] + nums2[0], i, 0) for i in range(min(m, k))]
        while hp and len(ans) < k:
            _, i, j = heappop(hp)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(hp, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans
