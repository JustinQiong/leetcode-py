from typing import List

"""
118. Pascal's Triangle
Calculate row i base on the values in row i-1
with the index of j and j-1.
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1]
            for j in range(1, i + 1):
                if j == i:
                    row.append(1)
                else:
                    row.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(row)

        return res