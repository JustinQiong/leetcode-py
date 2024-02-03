from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_is_interleave(self):
        solution = Solution()
        self.assertTrue(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
        self.assertFalse(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
        self.assertTrue(solution.isInterleave("", "", ""))
