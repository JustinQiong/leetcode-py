from collections import defaultdict
from typing import List

"""
2831. Find the Longest Equal Subarray
Store the number of numbers need to delete
of each position i to make the subarray of nums[i] from position 0 to i
into a hash table. Calculate the max len of the subarray by sliding the windows
within max deleted number of k.
"""
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_list = defaultdict(list)
        for i, x in enumerate(nums):
            pos_list[x].append(i - len(pos_list[x]))

        ans = 0
        for pos in pos_list.values():
            if len(pos) < ans:
                continue

            left = 0
            for right, p in enumerate(pos):
                while p - pos[left] > k:
                    left += 1
                ans = max(ans, right - left + 1)

        return ans