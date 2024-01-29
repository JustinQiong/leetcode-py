from typing import List


class Solution:

    def bubbleSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return arr

        for i in range(n):
            swap = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap = True

            if not swap:
                break

        return arr
