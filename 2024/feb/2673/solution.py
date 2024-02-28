from typing import List

"""
2673. Make Costs of Paths Equal in a Binary Tree
Iterate from backward of cost array by steps of 2.
Accumulate the increment to make cost[i] and cost[i+1] equal.
Accumulate costs of path max(cost[i], cost[i+1]) to
cost[i//2].
"""


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        for i in range(n - 2, 0, -2):
            res += abs(cost[i] - cost[i + 1])
            cost[i // 2] += max(cost[i], cost[i + 1])

        return res
