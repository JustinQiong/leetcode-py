from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def testFindWinners(self):
        solution = Solution()
        self.assertListEqual([[1, 2, 10], [4, 5, 7, 8]], solution.findWinners(
            [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
        self.assertListEqual([[1, 2, 5, 6], []], solution.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
