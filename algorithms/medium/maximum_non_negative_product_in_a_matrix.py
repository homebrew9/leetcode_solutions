from typing import List
from functools import cache

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        @cache
        def solve(r, c):
            # Return maximum and minimum products ending at (r, c)
            if r == rows - 1 and c == cols - 1:
                return grid[r][c], grid[r][c]
            if r >= rows or c >= cols:
                return MIN, MAX
            if grid[r][c] == 0:
                return 0, 0
            max1, min1 = solve(r + 1, c) # From below
            max2, min2 = solve(r, c+1)   # From right
            mx, mn = max(max1, max2)*grid[r][c], min(min1, min2)*grid[r][c]
            return (mx, mn) if grid[r][c] > 0 else (mn, mx)
        MIN, MAX = -10**20, 10**20
        rows = len(grid)
        cols = len(grid[0])
        MOD = 10**9 + 7
        res, _ = solve(0, 0)
        if res < 0:
            return -1
        return res % MOD

# Main section
for grid in [
               [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]],
               [[1,-2,1],[1,-2,1],[3,-4,1]],
               [[1,3],[0,-4]],
               [[3,4,1,2,2,2,4,1,2,1,1,1,4,4,2],[2,3,2,4,1,1,2,4,2,1,2,1,1,3,1],[1,4,2,4,3,2,2,1,1,2,2,4,3,2,3],[3,2,4,4,3,4,3,4,1,4,1,2,2,1,3],[3,1,1,2,2,4,2,1,4,2,1,2,2,2,4],[2,2,3,3,2,1,4,4,3,4,1,3,2,3,2],[3,3,3,1,3,3,4,4,2,2,1,2,1,3,2],[2,2,1,2,3,1,4,4,1,3,4,3,4,1,3],[1,3,2,2,4,3,1,1,4,1,2,1,1,4,2],[2,2,4,1,1,2,3,1,2,4,1,4,4,4,1],[3,2,3,2,2,2,4,4,2,4,4,1,4,2,3],[2,3,2,4,2,2,2,1,3,4,4,1,1,4,3],[2,3,3,1,4,4,4,1,2,1,4,4,4,1,2],[2,4,2,3,2,3,3,1,4,3,4,2,3,2,2],[4,3,3,4,1,3,4,3,4,2,4,1,1,3,3]],
               [[2]],
               [[3,4]],
               [[4],[2]],
               [[-1,-4,2],[4,3,-1],[2,-4,4],[1,-1,-4]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.maxProductPath(grid)
    print(f'r = {r}')
    print('===============================')






