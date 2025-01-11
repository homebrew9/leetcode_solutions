from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N = len(grid)
        rows_max = [max(grid[r]) for r in range(N)]
        cols_max = list()
        for c in range(N):
            cols_max.append(grid[0][c])
            for r in range(N):
                if grid[r][c] > cols_max[c]:
                    cols_max[c] = grid[r][c]
        #print(rows_max)
        #print(cols_max)
        res = 0
        for r in range(N):
            for c in range(N):
                res += min(rows_max[r], cols_max[c]) - grid[r][c]
        return res

# Main section
for grid in [
               [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]],
               [[0,0,0],[0,0,0],[0,0,0]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.maxIncreaseKeepingSkyline(grid)
    print(f'r = {r}')
    print('==================')

