from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            val = grid[r][c]
            for dr, dc in directions:
                rnew = r + dr
                cnew = c + dc
                if 0 <= rnew < rows and 0 <= cnew < cols and (rnew, cnew) not in visited and grid[rnew][cnew] > 0:
                    visited.add((rnew, cnew))
                    val += dfs(rnew, cnew)
            return val
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    visited.add((r, c))
                    total = dfs(r, c)
                    res = max(res, total)
        return res

# Main section
for grid in [
               [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]],
               [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]],
               [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
               [[0]],
               [[9]],
               [[0,2,6,7,9,0,4,2,3,7],[6,5,2,7,0,8,10,1,0,7],[1,7,10,0,10,7,2,6,0,6],[2,7,4,1,10,2,7,2,0,3],[1,2,2,3,0,7,1,7,8,4],[6,9,6,3,9,1,6,7,2,10],[9,10,9,8,0,5,2,8,4,0],[8,10,2,3,4,8,1,5,9,6],[7,10,1,0,10,1,1,1,2,5],[1,7,10,8,10,9,4,2,0,8]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.findMaxFish(grid)
    print(f'r = {r}')
    print('==================')


