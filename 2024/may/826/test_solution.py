from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def testMaxProfitAssignment(self):
        solution = Solution()
        self.assertEqual(100, solution.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))
        self.assertEqual(0, solution.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]))
