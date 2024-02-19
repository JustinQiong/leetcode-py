from typing import List

"""
442. Find All Duplicates in Array
Mark nums[nums[i]-1] to negative if visited a number.
When meet this number again, we will find nums[nums[i]-1] 
is negative. Append the number to the result.
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            n = abs(num)
            if nums[n - 1] < 0:
                res.append(n)
            else:
                nums[n - 1] = -nums[n - 1]

        return res