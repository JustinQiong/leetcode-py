"""
2864. Maximum Odd Binary Number
Count ones in s. The maximum odd number
will be one '1' at the right most position and
the other '1' at the left most position.
"""
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        count = s.count('1')
        return '1'*(count-1)+'0'*(n-count)+'1'