from typing import List

"""
304. Range Sum Query 2D - Immutable
Initiate the sums matrix. Each cell stands
for the range sum. When calculate the sum of the
region row1,col1 to row2, col2, the formula will be
sum(row2,col2)-sum(row1-1,col2)-sum(row2,col1-1)+sum(row1-1, col1-1)
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.mSum = [[0] * (n + 1) for _ in range(m + 1)]

        mSum = self.mSum
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                mSum[i][j] = mSum[i - 1][j] + mSum[i][j - 1] - mSum[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        mSum = self.mSum
        return mSum[row2 + 1][col2 + 1] - mSum[row1][col2 + 1] - mSum[row2 + 1][col1] + mSum[row1][col1]
