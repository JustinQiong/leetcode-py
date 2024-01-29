from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_bubble_sort(self):
        solution = Solution()
        self.assertListEqual([11, 12, 22, 25, 34, 64, 90], solution.bubbleSort([64, 34, 25, 12, 22, 11, 90]))
        self.assertListEqual([11, 12, 12, 13], solution.bubbleSort([13, 11, 12, 12]))
