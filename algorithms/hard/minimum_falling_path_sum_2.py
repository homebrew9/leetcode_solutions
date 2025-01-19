from typing import List
from collections import defaultdict

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def solve(r, c):
            if r == N - 1:
                return grid[r][c]
            if (r, c) in memo:
                return memo[(r, c)]
            min_val = float('inf')
            for c1 in range(N):
                if c1 == c:
                    continue
                tmp = solve(r+1, c1)
                min_val = min(min_val, tmp)
            memo[(r, c)] = grid[r][c] + min_val
            return memo[(r, c)]
        N = len(grid)
        memo = defaultdict(int)
        res = float('inf')
        for c in range(N):
            tmp = solve(0, c)
            res = min(res, tmp)
        return res

# Main section
for grid in [
               [[1,2,3],[4,5,6],[7,8,9]],
               [[7]],
               [[-5,2,4,-2,0],[4,-8,-7,1,-1],[4,-8,-9,1,6],[6,6,7,10,-1],[-4,-8,0,-1,-7]],
               [[-3,10,-8,-8,-1,10,-6,9,2,10],[-2,-3,10,3,2,-5,3,-8,-6,-3],[3,-10,-9,-7,9,10,-3,-9,-1,-8],[7,4,1,-2,-10,-3,6,-8,-4,-1],[-4,-4,8,-6,6,-10,5,0,-6,10],[9,-10,9,7,-1,-1,7,-5,-10,5],[-3,2,2,3,-2,4,-3,-9,2,-2],[-1,-5,-10,-7,0,6,-3,-3,5,-1],[-2,4,9,-4,-8,8,-8,-2,4,-3],[6,-2,10,0,5,3,1,-9,1,7]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.minFallingPathSum(grid)
    print(f'r = {r}')
    print('======================')

