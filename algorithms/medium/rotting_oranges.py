from typing import List
from collections import defaultdict, deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dq = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dq.append((r, c))
                    visited.add((r, c))
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        seconds = 0
        while True:
            #print(dq, visited, grid, seconds)
            size = len(dq)
            for _ in range(size):
                row, col = dq.popleft()
                for dr, dc in directions:
                    rnew = row + dr
                    cnew = col + dc
                    if 0 <= rnew < rows and 0 <= cnew < cols and grid[rnew][cnew] == 1 and (rnew, cnew) not in visited:
                        grid[rnew][cnew] = 2
                        dq.append((rnew, cnew))
                        visited.add((rnew, cnew))
            if not dq:
                break
            seconds += 1
        # We are done traversing the grid using BFS. Now check if any fresh orange got left out.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return seconds

# Main section
for grid in [
               [[2,1,1],[1,1,0],[0,1,1]],
               [[2,1,1],[0,1,1],[1,0,1]],
               [[0,2]],
               [[0,0,2,2,1,2,2,1,1,1],[1,2,1,2,1,2,2,0,1,1],[1,1,1,1,0,2,2,2,0,1],[0,0,0,1,2,0,2,1,1,2],[0,2,1,2,2,0,0,0,2,0],[1,2,0,2,0,2,1,1,0,0],[2,0,1,0,1,1,2,1,0,0],[1,0,2,0,0,0,1,1,1,0],[1,1,1,1,1,2,0,1,1,1],[2,2,1,2,1,1,2,0,1,1]],
               [[1,1,2,1,0,2,1,0,0,2],[2,0,1,0,2,2,2,1,2,2],[1,2,0,2,2,2,0,0,2,0],[0,1,1,1,1,1,2,2,1,2],[0,0,2,1,2,2,1,2,1,0],[1,0,0,2,2,0,1,0,1,1],[1,0,2,2,0,0,0,0,2,0],[1,2,1,0,1,1,0,2,1,1],[1,0,1,2,0,2,1,1,2,1],[1,2,2,0,1,1,2,2,1,2]],
               [[2,1,1,0,0,2,2,2,0,0],[0,1,2,1,0,0,1,1,1,1],[2,2,0,2,0,1,0,1,1,0],[1,1,2,0,1,2,0,1,1,2],[0,0,2,2,1,2,2,0,2,0],[1,1,0,2,1,0,2,2,2,2],[1,1,1,1,1,1,2,1,0,1],[2,1,0,0,2,0,1,1,1,2],[0,0,1,1,1,2,2,2,2,1],[1,1,0,1,2,2,2,2,0,1]],
               [[0,2,2,0,0,0,1,0,2,0],[0,0,0,1,1,2,0,0,2,0],[2,2,0,2,1,1,0,0,2,2],[0,1,0,0,1,1,1,0,2,1],[1,0,2,1,2,0,2,1,0,1],[1,2,2,1,1,1,0,2,0,1],[1,0,1,2,1,0,0,0,1,2],[1,2,1,1,1,2,2,0,2,2],[1,2,2,2,0,2,2,1,0,1],[1,1,2,0,0,0,0,0,0,2]],
               [[0,1,1,2,1,2,1,0,2,0],[1,1,1,0,0,0,1,1,0,1],[1,1,0,1,1,0,2,1,0,1],[1,2,2,0,1,2,0,2,0,2],[2,1,0,1,1,2,2,0,0,1],[2,1,2,0,2,0,0,2,2,1],[0,0,1,1,0,2,0,1,0,1],[2,2,2,0,0,0,1,0,0,1],[0,1,2,2,1,1,1,1,1,0],[1,2,2,1,2,0,2,0,2,1]],
               [[0,0,0,2,2,0,2,2,2,0],[0,2,2,1,0,2,0,2,0,1],[0,2,0,2,0,0,0,1,1,0],[1,0,0,2,2,2,2,2,2,1],[0,1,0,1,1,0,0,2,1,1],[0,2,1,1,2,2,2,0,2,2],[1,1,0,2,1,2,0,1,0,2],[2,2,2,1,1,2,2,1,1,1],[2,0,1,0,2,2,1,0,0,2],[0,1,1,0,2,0,1,2,0,2]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.orangesRotting(grid)
    print(f'r = {r}')
    print('=================')

