from typing import List

"""
303. Range Sum Query - Immutable
Accumulate sum before each position.
When calling the method sumRange, 
return the sum of right+1 minus sum of left.
"""
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sums = [0] * (n+1)
        _sums = self.sums
        for i in range(1, len(_sums)):
            _sums[i] = _sums[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        _sums = self.sums
        return _sums[right+1] - _sums[left]