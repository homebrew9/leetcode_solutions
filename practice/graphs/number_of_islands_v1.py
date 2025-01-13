from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            for dr, dc in directions:
                rnew = r + dr
                cnew = c + dc
                if 0 <= rnew < rows and 0 <= cnew < cols:
                    if grid[rnew][cnew] == '1' and (rnew, cnew) not in self.seen:
                        self.seen.add((rnew, cnew))
                        dfs(rnew, cnew)
        rows = len(grid)
        cols = len(grid[0])
        self.seen = set()
        res = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for r in range(rows):
            for c in range(cols):
                #print(f'\tseen = {self.seen}')
                if grid[r][c] == '1' and (r, c) not in self.seen:
                    res += 1
                    self.seen.add((r, c))
                    dfs(r, c)
        return res

# Main section
for grid in [
               [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']],
               [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']],
               [['1','1','1'],['0','1','0'],['1','1','1']],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.numIslands(grid)
    print(f'r = {r}')
    print('=================')

