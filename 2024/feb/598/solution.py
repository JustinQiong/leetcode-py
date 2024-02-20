from typing import List

"""
598. Range Addition II
Find the minimum row of the ops and the minimum column.
The maximum integers in the matrix after performing all
the operations is (minimum row * minimum col)
"""
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minRow = m
        minCol = n
        for op in ops:
            minRow, minCol = min(minRow, op[0]), min(minCol, op[1])

        return minRow * minCol
