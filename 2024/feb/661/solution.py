from typing import List

"""
661. Image Smoother  
"""
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total, count = 0, 0
                for x in range(max(i-1, 0), min(i+2, m)):
                    for y in range(max(j-1, 0), min(j+2, n)):
                        total += img[x][y]
                        count += 1
                res[i][j] = total // count
        return res