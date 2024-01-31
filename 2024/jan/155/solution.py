"""
155. Min Stack
Use a stack to store the element pushed into the stack.
Use another stack to store the minimum element in the stack.
If val is less than top element of the min stack,
push val into the min stack. Otherwise, push the top element
into the min stack again.
When come to the pop operation, just pop both stack and min stack.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
