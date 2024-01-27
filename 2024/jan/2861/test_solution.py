from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_max_number_of_alloys(self):
        solution = Solution()
        self.assertEqual(2, solution.maxNumberOfAlloys(3, 2, 15, [[1, 1, 1], [1, 1, 10]], [0, 0, 0], [1, 2, 3]))
        self.assertEqual(5, solution.maxNumberOfAlloys(3, 2, 15, [[1, 1, 1], [1, 1, 10]], [0, 0, 100], [1, 2, 3]))
        self.assertEqual(2, solution.maxNumberOfAlloys(2, 3, 10, [[2, 1], [1, 2], [1, 1]], [1, 1], [5, 5]))
