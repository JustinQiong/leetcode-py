from typing import List

"""
59. Spiral Matrix II
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col, dirIdx = 0, 0, 0
        for i in range(n * n):
            res[row][col] = i + 1

            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            # change direction if meet the edge
            if r < 0 or r >= n or c < 0 or c >= n or res[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4
                dx, dy = dirs[dirIdx]

            row, col = row + dx, col + dy

        return res