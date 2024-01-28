from unittest import TestCase
from solution import Solution

class TestSolution(TestCase):
    def test_can_measure_water(self):
        solution = Solution()
        self.assertTrue(solution.canMeasureWater(3, 5, 4))
        self.assertFalse(solution.canMeasureWater(2, 6,  5))
        self.assertTrue(solution.canMeasureWater(1, 2,  3))
