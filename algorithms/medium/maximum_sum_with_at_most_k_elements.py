from typing import List
from sortedcontainers import SortedList
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        sl = SortedList()
        rows = len(grid)
        for r in range(rows):
            t = limits[r]
            if t > 0:
                arr = sorted(grid[r])[-t:]
                for elem in arr:
                    sl.add(elem)
        if k == 0:
            return 0
        return sum(sl[-k:])

# Main section
for grid, limits, k in [
                            ([[1,2],[3,4]], [1,2], 2),
                            ([[5,3,7],[8,2,6]], [2,2], 3),
                            ([[0,1]], [0], 0),
                       ]:
    print(f'grid, limits, k = {grid}, {limits}, {k}')
    sol = Solution()
    r = sol.maxSum(grid, limits, k)
    print(f'r = {r}')
    print('===================')

