from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_erase_overlap_intervals(self):
        solution = Solution()
        self.assertEqual(1, solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
        self.assertEqual(2, solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
        self.assertEqual(0, solution.eraseOverlapIntervals([[1, 2], [2, 3]]))
