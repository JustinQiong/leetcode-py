from math import inf
from heapq import heappop, heappush
from typing import List

"""
1976. Number of Ways to Arrive at Destination
Dijkstra Algo to find the shortest path from
0 to n-1. Use array ways to store number of shortest paths
of node i.
"""
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        e = [[] for _ in range(n)]
        for x, y, t in roads:
            e[x].append((y, t))
            e[y].append((x, t))

        dis = [0] + [inf] * (n - 1)
        ways = [1] + [0] * (n - 1)

        q = [(0, 0)]
        mod = 10 ** 9 + 7
        while q:
            t, p = heappop(q)
            for x, c in e[p]:
                if c + t < dis[x]:
                    dis[x] = c + t
                    ways[x] = ways[p]
                    heappush(q, (c + t, x))
                elif c + t == dis[x]:
                    ways[x] = (ways[x] + ways[p]) % mod

        return ways[-1]