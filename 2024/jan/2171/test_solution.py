from unittest import TestCase
from solution import Solution

class TestSolution(TestCase):
    def test_minimum_removal(self):
        solution = Solution()
        self.assertEqual(4, solution.minimumRemoval([4, 1, 6, 5]))
        self.assertEqual(7, solution.minimumRemoval([2, 10, 3, 2]))
