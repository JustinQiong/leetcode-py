from typing import List

"""
73. Set Matrix Zeroes
Inplace solution:
Use two variables to store if the first row and first column should
be set to zero or not. Then iterate through each cell mark if the row
and column should be set to zero or not in the first row and first column
respectively. Accordingly replace the matrix with the mark in first row and 
first column. At last, replace the first column and first row base on
the variables assigned at the very beginning.
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        col0 = any(matrix[i][0] == 0 for i in range(m))
        row0 = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if row0:
            for i in range(n):
                matrix[0][i] = 0

        if col0:
            for i in range(m):
                matrix[i][0] = 0
