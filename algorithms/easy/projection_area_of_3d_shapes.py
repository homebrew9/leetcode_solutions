#
# Beautiful problem. Requires some imagination about 3D structures!
#
from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy_area, xz_area, yz_area = 0, 0, 0
        for v in grid:
            xy_area += sum([1 if i >= 1 else 0 for i in v])
            xz_area += max(v)
        n = len(grid)
        for c in range(n):
            max_val = float('-inf')
            for r in range(n):
                if grid[r][c] > max_val:
                    max_val = grid[r][c]
            yz_area += max_val
        #print(f'xy_area, xz_area, yz_area = {xy_area}, {xz_area}, {yz_area}')
        return xy_area + xz_area + yz_area

# Main section
for grid in [
               [[1,2],[3,4]],
               [[2]],
               [[1,0],[0,2]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.projectionArea(grid)
    print(f'r = {r}')
    print('=====================')

