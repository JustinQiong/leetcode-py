"""
2834. Find the Minimum Possible Sum of a Beautiful Array
Greedy and Math Solution:
If we add 1,2,3 to the nums array, then target-1, target-2, target-3 ...
is not allowed to add into nums. So the first part of the nums array
will be from 1 to target/2. If length of nums is not enough, then add
target, target+1, target+2 ... to nums until the length is equal to n.
"""
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10**9 + 7
        m = target//2
        if n <= m:
            return (n+1)*n//2 % mod
        else:
            return ((m+1)*m//2 + (target+target+n-m-1) * (n-m) // 2) % mod