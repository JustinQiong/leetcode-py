
"""
2079. Watering Plants
Iterate through plants array.
Minus total water with water each plant
needed. If water is not enough to the next plant,
refill the water and plus the steps to river and
come back to current plant.
"""
from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        steps = 0
        n = len(plants)
        for i, x in enumerate(plants):
            steps += 1
            water -= x
            if i < n - 1 and water < plants[i + 1]:
                water = capacity
                steps += 2 * (i + 1)

        return steps