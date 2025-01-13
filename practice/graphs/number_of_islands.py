from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Using DFS traversal
        def dfs(r, c):
            # Check all termination conditions first
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return
            if grid[r][c] != '1':
                return
            if (r, c) in self.visited:
                return
            # All clear. Set the cell as visited and
            # repeat for the surrounding cells
            self.visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        self.visited = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in self.visited:
                    res += 1
                    dfs(r, c)
        return res
    def numIslands_1(self, grid: List[List[str]]) -> int:
        # Using BFS traversal
        def bfs(r, c):
            dq = deque()
            dq.append((r, c))
            self.visited.add((r, c))
            while dq:
                N = len(dq)
                for _ in range(N):
                    cur = dq[0]
                    for dr, dc in directions:
                        rnew = cur[0] + dr
                        cnew = cur[1] + dc
                        if rnew < 0 or rnew >= rows:
                            continue
                        if cnew < 0 or cnew >= cols:
                            continue
                        if grid[rnew][cnew] == '1' and (rnew, cnew) not in self.visited:
                            dq.append((rnew, cnew))
                            self.visited.add((rnew, cnew))
                    dq.popleft()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        self.visited = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in self.visited:
                    res += 1
                    bfs(r, c)
        return res
    def numIslands_2(self, grid: List[List[str]]) -> int:
        # Using DFS traversal with a stack
        def dfs(r, c):
            stack = list()
            stack.append((r, c))
            while stack:
                cur = stack.pop()
                for dr, dc in directions:
                    r1 = cur[0] + dr
                    c1 = cur[1] + dc
                    if 0 <= r1 < rows and 0 <= c1 < cols:
                        if grid[r1][c1] == '1' and (r1, c1) not in self.visited:
                            self.visited.add((r1, c1))
                            stack.append((r1, c1))
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        self.visited = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in self.visited:
                    self.visited.add((r, c))
                    res += 1
                    dfs(r, c)
        return res

# Main section
for grid in [
               [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']],
               [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']],
               [['1','0','0','0','0'],['0','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','0'],['0','0','0','0','1']],
               [['1','1','1'],['0','1','0'],['1','1','1']],
               [['1','1','1'],['0','0','0'],['1','1','1']],
               [['1','1','1','1','1'],['1','0','0','0','1'],['1','0','0','0','1'],['1','0','0','0','1'],['1','1','1','1','1']],
               [['1','1','0','1','1'],['1','0','0','0','1'],['1','0','0','0','1'],['1','0','0','0','1'],['1','1','0','1','1']],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.numIslands(grid)
    print(f'r  (DFS Recursion) = {r}')
    r1 = sol.numIslands_1(grid)
    print(f'r1 (BFS)           = {r1}')
    r2 = sol.numIslands_2(grid)
    print(f'r2 (DFS Stack)     = {r2}')
    print('==================')

