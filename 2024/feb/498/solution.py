from typing import List

"""
498. Diagonal Traverse
Matrix with m*n cells will have m+n-1 diagonals.
Calculate the start cell of each diagonal by checking
if i % 2 == 0. If the diagonal direction is from top to bottom,
do x+=1, y-=1 until the coordinate is out of the range.
Otherwise, do x-=1, y+=1.
"""
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        for i in range(m+n-1):
            if i % 2:
                x = 0 if i < n else i-n+1
                y = i if i < n else n-1
                while x < m and y >= 0:
                    res.append(mat[x][y])
                    x += 1
                    y -= 1
            else:
                x = i if i < m else m-1
                y = 0 if i < m else i-m+1
                while y < n and x >= 0:
                    res.append(mat[x][y])
                    x -= 1
                    y += 1

        return res