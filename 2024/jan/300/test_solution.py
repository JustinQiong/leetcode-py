from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_length_of_lis(self):
        solution = Solution()
        self.assertEqual(4, solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(4, solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
        self.assertEqual(1, solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
