"""
232. Implement Queue using Stacks
Use two stacks sin and sout.
Push new element into sout.
When come to pop and peek element, if sout is not empty,
pop out sout. Otherwise, pop out elements in sin and push them into sout.
"""


class MyQueue:

    def __init__(self):
        self.sin = []
        self.sout = []

    def push(self, x: int) -> None:
        self.sin.append(x)

    def pop(self) -> int:
        if self.sout:
            return self.sout.pop()
        self.in2Out()
        return self.sout.pop()

    def peek(self) -> int:
        if self.sout:
            return self.sout[-1]
        self.in2Out()
        return self.sout[-1]

    def empty(self) -> bool:
        return not self.sin and not self.sout

    def in2Out(self):
        sin = self.sin
        sout = self.sout
        while sin:
            sout.append(sin.pop())
