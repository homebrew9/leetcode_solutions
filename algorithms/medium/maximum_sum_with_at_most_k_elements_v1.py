#
# Another solution using heap instead of SortedList
#
from typing import List
import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        rows = len(grid)
        arr = list()
        for r in range(rows):
            h = [-x for x in grid[r]]
            heapq.heapify(h)
            for _ in range(limits[r]):
                arr.append(heapq.heappop(h))
        heapq.heapify(arr)
        res = 0
        for _ in range(k):
            res += -heapq.heappop(arr)
        return res

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

