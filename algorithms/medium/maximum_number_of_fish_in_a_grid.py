from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            #print(f'\tr, c = {r}, {c}')
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return
            if visited[r][c]:
                return
            if grid[r][c] == 0:
                return
            self.curr_fish += grid[r][c]
            visited[r][c] = True
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        max_fish = 0
        self.curr_fish = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    dfs(r, c)
                    max_fish = max(max_fish, self.curr_fish)
                    self.curr_fish = 0
        return max_fish

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

