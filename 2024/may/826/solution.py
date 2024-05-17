from typing import List

"""
826. Most Profit Assigning Work
Sort zip(difficulty, profit) and worker array.
Iterate through worker in worker array.
Find the largest job less than or equal the work the worker can do.
Sum up the best profit each worker can do and return.
"""
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        i = res = best = 0
        worker.sort()
        n = len(jobs)
        for w in worker:
            while i < n and w >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            res += best

        return res