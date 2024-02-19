from typing import List

"""
495. Teemo Attacking
If time gap is less than duration, the poisoned
duration will be the time gap, otherwise the poisoned duration
will be the duration.
"""
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        n = len(timeSeries)
        for i in range(n):
            if i == n-1:
                res += duration
            else:
                res += min(duration, timeSeries[i+1]-timeSeries[i])

        return res
