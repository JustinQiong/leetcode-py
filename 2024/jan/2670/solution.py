from typing import List

"""
2670. Find the Distinct Difference Array
Iterate through nums from back and front directions.
Add the visited number into a set. Update the distinct
numbers at each index and calculate the difference between
prefix and suffix.
"""
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        st = set()
        n = len(nums)
        res = [0] * n
        for i in range(n - 1, 0, -1):
            st.add(nums[i])
            res[i - 1] = len(st)

        st.clear()

        for i in range(n):
            st.add(nums[i])
            res[i] = len(st) - res[i]

        return res
