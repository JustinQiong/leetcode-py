from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_k_smallest_pairs(self):
        solution = Solution()
        self.assertListEqual([[1, 2], [1, 4], [1, 6]], solution.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
        self.assertListEqual([[1, 1], [1, 1]], solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
        self.assertListEqual([[1, 3], [2, 3]], solution.kSmallestPairs([1, 2], [3], 3))
