#
# Recursive method that updates a global variable.
#
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if not(0 <= r < rows and 0 <= c < cols):
                return
            if (r, c) in self.visited:
                return
            if grid[r][c] >= 0:
                return
            self.visited.add((r, c))
            self.cnt += 1
            dfs(r, c-1)
            dfs(r-1, c)
        rows = len(grid)
        cols = len(grid[0])
        self.visited = set()
        self.cnt = 0
        dfs(rows-1, cols-1)
        return self.cnt

# Main section
for grid in [
               [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
               [[3,2],[1,0]],
               [[17,15,15,11,8,3,2],[14,13,9,9,7,1,-1],[12,11,8,5,1,0,-3],[8,7,7,3,0,-2,-5],[5,5,3,1,-1,-3,-9]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.countNegatives(grid)
    print(f'r = {r}')
    print('====================')

