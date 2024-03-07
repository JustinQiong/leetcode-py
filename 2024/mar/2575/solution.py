from typing import List

"""
2575. Find the Divisibility Array of a String
If curr is the remainder of each number. The remainder
of current position is the remainder of the former positions
multiple 10 and plus the current number then mod m.
The equation is as below:
curr = (curr * 10 + int(x)) % m
Then mark the res array by checking if curr is 0 or not.
"""


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        curr = 0
        res = []
        for i, n in enumerate(word):
            curr = (curr * 10 + int(n)) % m
            res.append(1 if curr == 0 else 0)

        return res
