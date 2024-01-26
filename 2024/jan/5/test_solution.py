from unittest import TestCase
from solution import Solution

class TestSolution(TestCase):
    def test_longest_palindrome(self):
        solution = Solution()
        self.assertEqual("bab", solution.longestPalindrome("babad"))
        self.assertEqual("bb", solution.longestPalindrome("cbbd"))
