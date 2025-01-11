from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        res = [None for _ in range(cols)]
        for c in range(cols):
            max_len = 0
            for r in range(rows):
                max_len = max(max_len, len(str(grid[r][c])))
            res[c] = max_len
        return res

# Main section
for grid in [
               [[1],[22],[333]],
               [[-15,1,3],[15,7,12],[5,6,-2]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.findColumnWidth(grid)
    print(f'r = {r}')
    print('==================')

