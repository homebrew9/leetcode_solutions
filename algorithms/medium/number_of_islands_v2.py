from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = [[False for _ in range(C)] for _ in range(R)]
        dq = deque()
        
        def bfs(r, c):
            #print(f'\t\tbfs(r, c) = bfs({r},{c})')
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            while dq:
                size = len(dq)
                for i in range(size):
                    r, c = dq[0]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '1' and not visited[nr][nc]:
                            dq.append((nr, nc))
                            visited[nr][nc] = True
                    dq.popleft()

        cnt = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and not visited[r][c]:
                    cnt += 1
                    dq.append((r, c))
                    visited[r][c] = True
                    bfs(r, c)
            #print(f'\tvisited = {visited}')
        return cnt

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

