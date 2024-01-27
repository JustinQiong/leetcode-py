from typing import List

"""
2861. Maximum Number of Alloys
Binary search solution:
Try each machine from 1 to maximum number of alloys.
If the spend is less than or equal to budget, try the range
from [mid+1, right]. Otherwise try the range from [left, mid-1].
Find the maximum valid alloy numbers.
"""


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:
        left, right, res = 1, 2 * 10 ** 8, 0

        while left <= right:
            mid = left + (right - left) // 2
            valid = False
            for i in range(k):
                spend = 0
                for j, (com, sto, cos) in enumerate(zip(composition[i], stock, cost)):
                    spend += max(com * mid - sto, 0) * cos

                if spend <= budget:
                    valid = True
                    break

            if valid:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
