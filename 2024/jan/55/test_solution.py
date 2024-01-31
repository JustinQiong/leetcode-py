from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_my_pow(self):
        solution = Solution()
        self.assertAlmostEqual(1024.00000, solution.myPow(2.00000, 10))
        self.assertAlmostEqual(9.26100, solution.myPow(2.10000, 3))
        self.assertAlmostEqual(0.25000, solution.myPow(2.00000, -2))
