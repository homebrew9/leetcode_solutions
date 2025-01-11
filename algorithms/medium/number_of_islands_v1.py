from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islandCount = 0
        rows = len(grid)
        cols = len(grid[0])
        self.vis = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(grid, rows, cols, r, c):
            #print(f'\trows, cols, r, c = {rows}, {cols}, {r}, {c} ; vis = {self.vis}')
            if r < 0 or r > rows - 1:
                return
            if c < 0 or c > cols - 1:
                return
            #print(f'\t(r,c) = ({r},{c})')
            #print(f'\tvis[r][c] = {self.vis[r][c]}')
            #print('=====')
            if self.vis[r][c] or grid[r][c] == '0':
                return
            self.vis[r][c] = True
            dfs(grid, rows, cols, r-1, c)
            dfs(grid, rows, cols, r+1, c)
            dfs(grid, rows, cols, r, c+1)
            dfs(grid, rows, cols, r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not self.vis[r][c]:
                    self.islandCount += 1
                    dfs(grid, rows, cols, r, c)

        return self.islandCount

# Main section
for grid in [
               [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']],
               [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']],
               [['1','1','1'],['1','1','0'],['1','0','1']],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.numIslands(grid)
    print(f'r = {r}')
    print('==========================')

