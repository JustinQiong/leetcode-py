from collections import Counter
from typing import List

"""
2225. Find Players With Zero or One Losses
Use a hash table to record the lose time of each player.
Then find out the players lose 0 or 1 time and sort the players respectively.
"""
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        freq = Counter()
        for winner, loser in matches:
            if winner not in freq:
                freq[winner] = 0
            freq[loser] += 1

        ans = [[], []]

        for key, value in freq.items():
            if value < 2:
                ans[value].append(key)

        ans[0].sort()
        ans[1].sort()
        return ans