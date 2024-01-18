from typing import List

"""
2171. Removing Minimum Number of Magic Beans
Sort the beans array and sum the array.
Iterate through each element and find the minimum number of 
the beans to remove which is total-(n-i)*beans[i]
"""
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        total = sum(beans)
        res = total
        for i in range(n):
            res = min(res, total - (n - i) * beans[i])

        return res