from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_find_min_arrow_shots(self):
        solution = Solution()
        self.assertEqual(2, solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
        self.assertEqual(4, solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
        self.assertEqual(2, solution.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))