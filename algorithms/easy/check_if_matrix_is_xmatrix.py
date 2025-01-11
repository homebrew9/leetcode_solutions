from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        left, right = 0, cols - 1
        for row in range(rows):
            for col in range(cols):
                if (col == left or col == right):
                    if grid[row][col] == 0:
                        return False
                else:
                    if grid[row][col] != 0:
                        return False
            left += 1
            right -= 1
        return True
            
 # Main section
for grid in [
               [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]],
               [[5,7,0],[0,3,1],[0,5,0]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.checkXMatrix(grid)
    print(f'r = {r}')
    print('=================')

