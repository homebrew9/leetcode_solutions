from typing import List
from collections import defaultdict

class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        def dfs(r, c, orig_r, orig_c):
            for dr, dc in directions:
                rnew = r + dr
                cnew = c + dc
                if 0 <= rnew < N and 0 <= cnew < N and grid[rnew][cnew] != -1 and (rnew, cnew) not in visited:
                    visited.add((rnew, cnew))
                    cnt = hsh[(orig_r, orig_c)][0] + 1
                    total = hsh[(orig_r, orig_c)][1] + grid[rnew][cnew]
                    hsh[(orig_r, orig_c)] = [cnt, total]
                    dfs(rnew, cnew, orig_r, orig_c)
        N = len(grid)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        grand_total = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] != -1:
                    grand_total += grid[r][c]
        hsh = defaultdict(list)
        for r in range(N):
            for c in range(N):
                if grid[r][c] != -1 and (r, c) not in visited:
                    visited.add((r, c))
                    hsh[(r, c)] = [1, grid[r][c]]
                    dfs(r, c, r, c)
        #print(hsh)
        res = 0
        for k, v in hsh.items():
            num, total = v[0], v[1]
            res += (grand_total - total) * num
        return res

# Main section
for grid in [
               [[-1,1,-1],[5,-1,4],[-1,3,-1]],
               [[-1,3,4],[-1,-1,-1],[3,-1,-1]],
               [[1]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.sumRemoteness(grid)
    print(f'r = {r}')
    print('=======================')


