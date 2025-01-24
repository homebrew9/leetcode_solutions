from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def inside_grid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        def dfs(r, c, orig_r, orig_c):
            for dr, dc in directions:
                r1, c1 = r, c
                while inside_grid(r1 + dr, c1 + dc):
                    r1 += dr
                    c1 += dc
                    if (r1, c1) in visited:
                        break
                    if grid[r1][c1] == 1 and (r1, c1) not in visited:
                        visited.add((r1, c1))
                        self.hsh[(orig_r, orig_c)] += 1
                        dfs(r1, c1, orig_r, orig_c)
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        self.hsh = defaultdict(int)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    visited.add((r, c))
                    self.hsh[(r, c)] = 1
                    dfs(r, c, r, c)
        res = 0
        for k, v in self.hsh.items():
            if v > 1:
                res += v
        return res

# Main section
for grid in [
               [[1,0],[0,1]],
               [[1,0],[1,1]],
               [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]],
               [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.countServers(grid)
    print(f'r = {r}')
    print('=======================')


