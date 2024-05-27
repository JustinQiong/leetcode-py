from typing import List

"""
2028. Find Missing Observations
The missing sum mSum=mean * (len(rolls) + n) - sum(rolls)
The missing elements could be x elements of base+1 and y elements of base.
base = mSum//n, x = mSum%n, y = n-x
"""
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        miss = mean * (len(rolls) + n) - sum(rolls)
        if not n <= miss <= 6 * n:
            return []

        quotient, remainder = divmod(miss, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)