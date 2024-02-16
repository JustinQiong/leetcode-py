from typing import List

"""
189. Rotate Array
Reverse array 3 times.
1. Reverse nums from 0 to len(nums)-1.
2. Reverse nums from 0 to k % n - 1.
3. Reverse nums from k % n to n - 1
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(ns, start, end):
            while start < end:
                ns[start], ns[end] = ns[end], ns[start]
                start += 1
                end -= 1

        n = len(nums)
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k % n - 1)
        reverse(nums, k % n, n - 1)
