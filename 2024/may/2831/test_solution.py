from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def testLongestEqualSubarray(self):
        solution = Solution()
        self.assertEqual(3, solution.longestEqualSubarray([1, 3, 2, 3, 1, 3], 3))
        self.assertEqual(4, solution.longestEqualSubarray([1, 1, 2, 2, 1, 1], 2))
