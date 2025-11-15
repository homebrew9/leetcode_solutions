from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Intuition: Determine all cells in Island1 and put them in a set.
        # Do a BFS from ALL cells of Island1 and determine the number of
        # steps to reach any cell of Island2.
        def dfs(r, c):
            for dr, dc in directions:
                rnew = r + dr
                cnew = c + dc
                if 0 <= rnew < N and 0 <= cnew < N and (rnew, cnew) not in seen and grid[rnew][cnew] == 1:
                    seen.add((rnew, cnew))
                    dfs(rnew, cnew)
        N = len(grid)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        seen = set()
        found = False
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    seen.add((r, c))
                    dfs(r, c)
                    found = True
                    break
            if found:
                break
        # Now we do a BFS from all cells of Island1 and
        # try to reach Island2
        dq = deque(seen)
        visited = seen.copy()
        flips = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                r, c = dq.popleft()
                for dr, dc in directions:
                    rnew = r + dr
                    cnew = c + dc
                    if 0 <= rnew < N and 0 <= cnew < N and (rnew, cnew) not in visited:
                        if grid[rnew][cnew] == 1:
                            return flips
                        visited.add((rnew, cnew))
                        dq.append((rnew, cnew))
            flips += 1
        return flips # As per the problem constraints, control will never reach here.

# Main section
for grid in [
               [[0,1],[1,0]],
               [[0,1,0],[0,0,0],[0,0,1]],
               [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.shortestBridge(grid)
    print(f'r = {r}')
    print('=====================')




