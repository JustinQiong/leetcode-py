from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_distinct_difference_array(self):
        solution = Solution()
        self.assertListEqual([-3, -1, 1, 3, 5], solution.distinctDifferenceArray([1, 2, 3, 4, 5]))
        self.assertListEqual([-2, -1, 0, 2, 3], solution.distinctDifferenceArray([3, 2, 3, 4, 2]))
