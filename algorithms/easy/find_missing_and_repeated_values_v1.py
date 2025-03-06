from typing import List
from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        arr = [elem for lst in grid for elem in lst]
        return [k for k, v in Counter(arr).items() if v == 2] + list(set([i for i in range(1, N*N+1)]) - set(arr))

# Main section
for grid in [
               [[1,3],[2,2]],
               [[9,1,7],[8,9,2],[3,4,6]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.findMissingAndRepeatedValues(grid)
    print(f'r = {r}')
    print('================================')

