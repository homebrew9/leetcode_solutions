from typing import List
from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def solve(r, c):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if c == cols - 1:
                return grid[r][c] + solve(r+1, c)
            if r == rows - 1:
                return grid[r][c] + solve(r, c+1)
            return grid[r][c] + min(solve(r, c+1), solve(r+1, c))
        rows = len(grid)
        cols = len(grid[0])
        res = solve(0, 0)
        return res
    def minPathSum_1(self, grid: List[List[int]]) -> int:
        def solve(r, c):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if (r, c) in memo:
                return memo[(r, c)]
            if c == cols - 1:
                val = grid[r][c] + solve(r+1, c)
            elif r == rows - 1:
                val = grid[r][c] + solve(r, c+1)
            else:
                val = grid[r][c] + min(solve(r, c+1), solve(r+1, c))
            memo[(r, c)] = val
            return memo[(r, c)]
        memo = dict()
        rows = len(grid)
        cols = len(grid[0])
        res = solve(0, 0)
        return res

# Main section
for grid in [
               [[1,3,1],[1,5,1],[4,2,1]],
               [[1,2,3],[4,5,6]],
               [[168,125,23,79,66],[87,50,191,78,101],[94,35,60,90,171]],
               [[78,172,18,47,191,59,123],[74,132,18,138,120,182,34],[124,82,172,134,34,31,70],[187,199,72,134,40,58,66]],
               [[87,128,108,85,19,76,33,102],[56,136,151,66,98,32,159,97],[62,67,103,173,146,21,14,81],[163,166,112,175,131,104,147,20],[129,34,181,73,79,77,150,93]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.minPathSum(grid)
    r1 = sol.minPathSum_1(grid)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('============================')


