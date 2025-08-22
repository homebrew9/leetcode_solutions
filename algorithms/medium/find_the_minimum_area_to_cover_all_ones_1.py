from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        min_row, min_col = float('inf'), float('inf')
        max_row, max_col = float('-inf'), float('-inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    min_row = min(min_row, r)
                    min_col = min(min_col, c)
                    max_row = max(max_row, r)
                    max_col = max(max_col, c)
        min_area = (max_row - min_row + 1) * (max_col - min_col + 1)
        return min_area

# Main section
for grid in [
               [[0,1,0],[1,0,1]],
               [[1,0],[0,0]],
            ]:
    print(f'grid  = {grid}')
    sol = Solution()
    r = sol.minimumArea(grid)
    print(f'r = {r}')
    print('==============================')






