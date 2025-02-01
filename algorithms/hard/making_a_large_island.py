from typing import List
from collections import deque, defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Do a BFS and store information of all islands in a dictionary. The key is the "root" cell.
        # And the value is a list of cells in that island. Then update the grid and set the value of
        # each island cell to (root_x, root_y, island_size). Then iterate through all cells with value
        # 0 and check all 4 directions to determine the size of the largest island.
        # Todo: Study how Union-Find has been used to solve this problem.
        def bfs(r, c):
            dq = deque()
            dq.append((r, c))
            visited.add((r, c))
            while dq:
                size = len(dq)
                for _ in range(size):
                    row, col = dq.popleft()
                    for dr, dc in directions:
                        r1 = row + dr
                        c1 = col + dc
                        if 0 <= r1 < N and 0 <= c1 < N and (r1, c1) not in visited and grid[r1][c1] == 1:
                            visited.add((r1, c1))
                            dq.append((r1, c1))
                            hsh[(r, c)].append((r1, c1))
        def update_grid():
            for k, v in hsh.items():
                root_r, root_c = k
                size = len(v)
                for r, c in v:
                    grid[r][c] = (root_r, root_c, size)
        def check_all_zeros():
            for r in range(N):
                for c in range(N):
                    if grid[r][c] == 0:
                        cc_set = set()
                        for dr, dc in directions:
                            r1 = r + dr
                            c1 = c + dc
                            if 0 <= r1 < N and 0 <= c1 < N and type(grid[r1][c1]) == tuple:
                                cc_set.add(grid[r1][c1])
                        total_size = sum([item[2] for item in cc_set]) + 1
                        self.res = max(self.res, total_size)
        N = len(grid)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        hsh = defaultdict(list)
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1 and (r, c) not in visited:
                    hsh[(r, c)] = [(r, c)]
                    bfs(r, c)
        if len(hsh) == 0:
            return 1
        update_grid()
        self.res = max([len(v) for v in hsh.values()])
        check_all_zeros()
        return self.res

# Main section
for grid in [
               [[1,0],[0,1]],
               [[1,1],[1,0]],
               [[1,1],[1,1]],
               [[1,1,1,0,1,1],[1,1,1,0,1,1],[1,1,1,0,0,0],[0,0,0,1,1,0],[1,1,1,0,0,0],[1,1,1,0,0,0]],
               [[1,1,1,0,1,1],[1,1,1,1,1,1],[1,1,1,0,1,1],[0,0,0,0,0,0],[1,1,1,0,0,0],[1,1,1,0,0,0]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.largestIsland(grid)
    print(f'r = {r}')
    print('=========================')

