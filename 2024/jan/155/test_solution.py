from unittest import TestCase
from solution import MinStack


class TestMinStack(TestCase):
    def testStack(self):
        stack = MinStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(3, stack.top())
        self.assertListEqual([1, 2, 3], stack.stack)
        stack.pop()
        self.assertListEqual([1, 2], stack.stack)
        self.assertEqual(1, stack.getMin())
        stack.push(-1)
        self.assertEqual(-1, stack.getMin())
