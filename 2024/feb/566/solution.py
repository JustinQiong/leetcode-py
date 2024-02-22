from typing import List

"""
566. Reshape the Matrix
res[i // c][i % c] = mat[i // n][i % n]
"""
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        res = [[None] * c for _ in range(r)]
        for i in range(m * n):
            res[i // c][i % c] = mat[i // n][i % n]

        return res