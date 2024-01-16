from typing import List


"""
435. Non-overlapping Intervals
Greedy solution:
Sort the intervals list with the right edge of the range.
If the interval[i] is not overlapping with the interval[i-1],
update the right edge of the range. Otherwise remove the interval[i].
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a: a[1])

        right = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= right:
                right = intervals[i][1]
            else:
                res += 1

        return res