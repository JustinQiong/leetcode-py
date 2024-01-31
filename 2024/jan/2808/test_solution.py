from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_minimum_seconds(self):
        solution = Solution()
        self.assertEqual(1, solution.minimumSeconds([1, 2, 1, 2]))
        self.assertEqual(2, solution.minimumSeconds([2, 1, 3, 3, 2]))
        self.assertEqual(0, solution.minimumSeconds([5, 5, 5, 5]))
