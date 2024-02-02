from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_min_distance(self):
        solution = Solution()
        self.assertEqual(3, solution.minDistance("horse", "ros"))
        self.assertEqual(5, solution.minDistance("intention", "execution"))
