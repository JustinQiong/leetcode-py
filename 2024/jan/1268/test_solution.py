from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def test_suggested_products(self):
        solution = Solution()
        self.assertListEqual(
            [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"],
             ["mouse", "mousepad"], ["mouse", "mousepad"]],
            solution.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
