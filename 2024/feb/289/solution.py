from typing import List

"""
289. Game of Life
Iterate through the cells on the board.
Calculate the neighbours with 0 and 2 are dies.
1 and -1 are lives.
Mark the cell from live to death to -1.
Mark the cell from death to live to 2.
Iterate through the cells again to modify
the cell with value -1 to 0 and 2 to 1.
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):
                dies, lives = 0, 0
                for x in range(8):
                    dx, dy = directs[x]
                    r, c = i + dx, j + dy
                    if 0 <= r < m and 0 <= c < n:
                        cell = board[r][c]
                        if cell == 0 or cell == 2:
                            dies += 1

                        if cell == 1 or cell == -1:
                            lives += 1

                if board[i][j] == 1 and (lives < 2 or lives > 3):
                    board[i][j] = -1

                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
