from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        directions = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        dq = deque()
        visited = set()
        start, end = (0,0), (N-1,N-1)
        #print(f'start, end = {start}, {end}')
        dq.append(start)
        visited.add(start)
        steps = 1
        while dq:
            #print(f'\tset = {visited}')
            #print(f'\tdq  = {dq}')
            #print('=====')
            size = len(dq)
            for _ in range(size):
                r, c = dq[0]
                if (r, c) == end:
                    #print('\tin if r, c == end')
                    return steps
                for dr, dc in directions:
                    rnew, cnew = r+dr, c+dc
                    if 0 <= rnew < N and 0 <= cnew < N:
                        if (rnew,cnew) not in visited and grid[rnew][cnew] == 0:
                            visited.add((rnew,cnew))
                            dq.append((rnew,cnew))
                dq.popleft()
            steps += 1
        return -1

# Main section
for grid in [
               [[0,1],[1,0]],
               [[0,0,0],[1,1,0],[1,1,0]],
               [[1,0,0],[1,1,0],[1,1,0]],
               [[0,1,0,1],[1,0,1,0],[1,0,1,1],[1,0,1,0]],
               [[0,1,0,1],[1,0,1,0],[1,1,0,1],[1,1,1,0]],
               [[0,1,0,0,1],[1,0,1,1,0],[1,1,1,0,1],[1,1,0,1,1],[1,1,1,0,0]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.shortestPathBinaryMatrix(grid)
    print(f'r = {r}')
    print('====================')

