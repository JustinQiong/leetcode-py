"""
365. Water and Jug Problem
Breath first solution:
Try 6 scenarios every step
empty jug x
emtpy jug y
fill jug x
fill jug y
pour water from jug x to y
pour water from jug y to x
"""


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        seen = set()
        while stack:
            r_x, r_y = stack.pop()

            if r_x == z or r_y == z or r_x + r_y == z:
                return True

            if (r_x, r_y) in seen:
                continue

            seen.add((r_x, r_y))

            stack.append((0, r_y))
            stack.append((r_x, 0))
            stack.append((x, r_y))
            stack.append((r_x, y))
            stack.append((r_x - min(r_x, y - r_y), r_y + min(r_x, y - r_y)))
            stack.append((r_x + min(x - r_x, r_y), r_y - min(x - r_x, r_y)))

        return False
