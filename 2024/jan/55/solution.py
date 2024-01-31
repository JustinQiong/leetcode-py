"""
50. Pow(x, n)
Calculate pow of x**n by calculating pow of y=x**(n//2) recursively.
And if n is even, y*y is the pow of x**n.
If n is odd, y*y*x is the pow of x**n
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def mul(m):
            if m == 0:
                return 1.0
            y = mul(m // 2)
            return y * y if m % 2 == 0 else y * y * x

        return mul(n) if n >= 0 else 1/mul(-n)
