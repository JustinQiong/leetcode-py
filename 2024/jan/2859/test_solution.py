from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_sum_indices_with_kset_bits(self):
        solution = Solution()
        self.assertEqual(13, solution.sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1))
        self.assertEqual(1, solution.sumIndicesWithKSetBits([4, 3, 2, 1], 2))

