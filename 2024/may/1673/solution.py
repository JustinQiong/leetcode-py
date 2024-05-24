from typing import List

"""
1673. Find the Most Competitive Subsequence
Monotonic Stack Solution:
Iterate through nums and compare nums[i] with x 
which is the top element of the stack. If nums[i] is less than
x, replace x with nums[i]. After the iteration, return
the monotonic stack.
"""
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        m = 0
        n = len(nums)
        for i, x in enumerate(nums):
            while m and nums[m - 1] > x and m + n - i > k:
                m -= 1

            if m < k:
                nums[m] = x
                m += 1

        del nums[m:]
        return nums