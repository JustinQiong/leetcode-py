from typing import List

"""
119. Pascal's Triangle II
Response array res is initialized with rowIndex+1 elements of 1.
Iterate through res, calculate the res with the equation of
 res[j], pre = res[j] + pre, res[j]
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex+1)
        if rowIndex == 0:
            return res

        for i in range(rowIndex):
            pre = 1
            for j in range(1, i+1):
                res[j], pre = res[j] + pre, res[j]

        return res