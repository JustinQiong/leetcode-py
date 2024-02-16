from typing import List

"""
283. Move Zeroes
Two pointers solution with i, j
i is point to each element of the array.
j is point to the element not zero.
Swap the element of i and j.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
