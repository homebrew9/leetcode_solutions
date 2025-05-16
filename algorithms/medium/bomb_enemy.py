from typing import List

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        pfx_rows = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        pfx_cols = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'W':
                    pfx_rows[r][c][0] = 0
                elif c == 0:
                    pfx_rows[r][c][0] = 1 if grid[r][c] == 'E' else 0
                else:
                    pfx_rows[r][c][0] = pfx_rows[r][c-1][0] + (1 if grid[r][c] == 'E' else 0)
            for c in range(cols-1, -1, -1):
                if grid[r][c] == 'W':
                    pfx_rows[r][c][1] = 0
                elif c == cols - 1:
                    pfx_rows[r][c][1] = 1 if grid[r][c] == 'E' else 0
                else:
                    pfx_rows[r][c][1] = pfx_rows[r][c+1][1] + (1 if grid[r][c] == 'E' else 0)
        for c in range(cols):
            for r in range(rows):
                if grid[r][c] == 'W':
                    pfx_cols[r][c][0] = 0
                elif r == 0:
                    pfx_cols[r][c][0] = 1 if grid[r][c] == 'E' else 0
                else:
                    pfx_cols[r][c][0] = pfx_cols[r-1][c][0] + (1 if grid[r][c] == 'E' else 0)
            for r in range(rows-1, -1, -1):
                if grid[r][c] == 'W':
                    pfx_cols[r][c][1] = 0
                elif r == rows - 1:
                    pfx_cols[r][c][1] = 1 if grid[r][c] == 'E' else 0
                else:
                    pfx_cols[r][c][1] = pfx_cols[r+1][c][1] + (1 if grid[r][c] == 'E' else 0)
        #print(pfx_rows)
        #print(pfx_cols)
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    val = 0
                    if 0 < r < rows-1:
                        val += pfx_cols[r-1][c][0] + pfx_cols[r+1][c][1]
                    elif r == 0 and rows > 1:
                        val += pfx_cols[r+1][c][1]
                    elif r == rows-1 and rows > 1:
                        val += pfx_cols[r-1][c][0]

                    if 0 < c < cols-1:
                        val += pfx_rows[r][c-1][0] + pfx_rows[r][c+1][1]
                    elif c == 0 and cols > 1:
                        val += pfx_rows[r][c+1][1]
                    elif c == cols-1 and cols > 1:
                        val += pfx_rows[r][c-1][0]

                    #print(f'\t(r, c) = ({r}, {c}) ; val = {val}')
                    res = max(res, val)
        return res

# Main section
for grid in [
               [['0','E','0','0'],['E','0','W','E'],['0','E','0','0']],
               [['W','W','W'],['0','0','0'],['E','E','E']],
               [['0']],
               [['0'],['E']],
               [['0'],['E'],'E'],
               [['0','W']],
               [['E','E','0']],
               [['W','W','E','0','0'],['W','E','W','E','W'],['E','E','W','E','E'],['0','W','0','W','W'],['E','W','0','W','E'],['W','W','E','W','W'],['E','0','W','0','0']],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.maxKilledEnemies(grid)
    print(f'r  = {r}')
    print('============================')

