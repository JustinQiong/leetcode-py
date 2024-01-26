from typing import List

"""
34. Find First and Last Position of Element in Sorted Array
Binary search solution:
Find the leftmost element less or equals to target
and the rightmost element greater or equals to target by binary search.
Check if the leftmost one or the rightmost one is equals to target.
Otherwise return -1.
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(ns: List[int], t: int) -> int:
            left, right = 0, len(ns) - 1
            res = -1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if ns[mid] >= t:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return res if res == -1 or nums[res] == t else -1

        def last(ns: List[int], t: int) -> int:
            left, right = 0, len(ns) - 1
            res = -1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if ns[mid] <= t:
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return res if res == -1 or nums[res] == t else -1

        return [first(nums, target), last(nums, target)]
