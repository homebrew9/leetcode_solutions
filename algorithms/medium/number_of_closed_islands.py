from collections import deque

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def bfs(r, c):
            dq = deque()
            dq.append((r, c))
            visited.add((r, c))
            is_valid = True
            while dq:
                size = len(dq)
                for _ in range(size):
                    row, col = dq.popleft()
                    for dr, dc in directions:
                        rnew = row + dr
                        cnew = col + dc
                        if not (0 <= rnew < rows) or not (0 <= cnew < cols):
                            is_valid = False
                            continue
                        if grid[rnew][cnew] == 0 and not (rnew, cnew) in visited:
                            visited.add((rnew, cnew))
                            dq.append((rnew, cnew))
            return 1 if is_valid else 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visited:
                    val = bfs(r, c)
                    res += val
        return res

# Main section
for grid in [
               [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]],
               [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]],
               [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]],
               [[1,0,0,1,0,0,1,0,1,1],[1,1,0,1,1,1,0,1,1,0],[0,1,0,0,1,1,1,0,0,1],[0,0,1,1,0,0,0,0,1,1],[0,1,1,1,0,0,1,0,0,0],[1,0,1,0,0,0,0,1,1,1],[1,0,1,1,1,1,1,1,0,0],[0,1,0,1,0,1,1,1,1,1],[0,0,0,0,1,1,1,1,1,1],[1,1,1,0,1,0,1,1,0,1]],
               [[0,1,1,0,0],[1,1,0,1,1],[0,0,0,0,1],[1,1,1,1,1],[0,1,0,1,0]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.closedIsland(grid)
    print(f'r = {r}')
    print('===================================')













