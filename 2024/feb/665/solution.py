from typing import List

"""
665. Non-decreasing Array
"""
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        times = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                times += 1
                if times > 1:
                    return False

                if i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]

        return True
