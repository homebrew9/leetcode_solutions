from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        amount = capacity
        for i, v in enumerate(plants):
            print(f'\t>>> i, v = {i}, {v}')
            steps += 1
            amount -= v
            print(f'\t\t>>> amount = {amount}')
            print(f'\t\t>>> i, len = {i}, {len(plants)}')
            if i < len(plants)-1 and amount < plants[i+1]:
                steps += 2 * (i + 1)
                amount = capacity
            print(f'\t\t>>> steps = {steps}')
        return steps

# Main section
sol = Solution()
for plants, capacity in [
                           #([7,7,7,7,7,7,7], 8)
                           ([1,1,1,4,2,3], 4)
                           #([2,2,3,3], 5)
                        ]:
    print(f'plants, capacity = {plants}, {capacity}')
    r = sol.wateringPlants(plants, capacity)
    print(f'r = {r}')
    print('=========================================')

 
