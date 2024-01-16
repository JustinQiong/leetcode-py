from typing import List

"""
452. Minimum Number of Arrows to Burst Balloons
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda a: a[1])

        pos = points[0][1]
        res = 1
        for point in points:
            if point[0] > pos:
                pos = point[1]
                res += 1

        return res
