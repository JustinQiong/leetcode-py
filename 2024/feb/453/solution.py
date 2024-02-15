from typing import List

"""
453. Minimum Moves to Equal Array Elements
The operation of increment n-1 elements of the array by 1
is the same as operation of decrement 1 largest element of the array
by 1. So sum each number-min(nums), it is the minimum moves to 
make the array elements equal.
"""
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)

        res = 0
        for num in nums:
            res += num - m

        return res