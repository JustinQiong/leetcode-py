from typing import List

"""
448. Find All Numbers Disappeared in an Array
Use an array to store the occurrence of each number
between 1 to len(nums). Return the array with the occurrence
of 0.
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tb = [0] * n
        for num in nums:
            tb[num - 1] += 1

        res = []
        for i, count in enumerate(tb):
            if count == 0:
                res.append(i + 1)

        return res
