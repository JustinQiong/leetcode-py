from typing import List

"""
48. Rotate Image
Rotate the matrix within the center point.
Divide the matrix into four parts, rotate the
sub matrix by row and col separately. Caution
the coordination of rotated cells base on the variation
of i and j through iteration.
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] = \
                matrix[n - j - 1][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]
