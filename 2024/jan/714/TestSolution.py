from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_max_profit(self):
        solution = Solution()
        self.assertEqual(8, solution.maxProfit([1, 3, 2, 8, 4, 9], 2))
        self.assertEqual(6, solution.maxProfit([1, 3, 7, 5, 10, 3], 3))
        self.assertEqual(3, solution.maxProfit([1, 6], 2))
