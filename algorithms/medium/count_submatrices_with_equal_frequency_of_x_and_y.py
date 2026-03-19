from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        xcount, ycount = 0, 0
        hsh = defaultdict(tuple)
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    xcount += 1 if grid[r][c] == 'X' else 0
                    ycount += 1 if grid[r][c] == 'Y' else 0
                    hsh[(r, c)] = (xcount, ycount) # type: ignore
                elif r == 0:
                    xc, yc = hsh[(r, c-1)] # type: ignore
                    xc += 1 if grid[r][c] == 'X' else 0
                    yc += 1 if grid[r][c] == 'Y' else 0
                    hsh[(r, c)] = (xc, yc) # type: ignore
                elif c == 0:
                    xc, yc = hsh[(r-1, c)] # type: ignore
                    xc += 1 if grid[r][c] == 'X' else 0
                    yc += 1 if grid[r][c] == 'Y' else 0
                    hsh[(r, c)] = (xc, yc) # type: ignore
                else:
                    left_xc, left_yc = hsh[(r, c-1)] # type: ignore
                    up_xc, up_yc = hsh[(r-1, c)] # type: ignore
                    diag_xc, diag_yc = hsh[(r-1, c-1)] # type: ignore
                    xc = left_xc + up_xc - diag_xc
                    yc = left_yc + up_yc - diag_yc
                    xc += 1 if grid[r][c] == 'X' else 0
                    yc += 1 if grid[r][c] == 'Y' else 0
                    hsh[(r, c)] = (xc, yc) # type: ignore
                xc, yc = hsh[(r, c)] # type: ignore
                if xc >= 1 and xc == yc:
                    res += 1
                #print(r, c, res)
        return res

# Main section
for grid in [
               [['X','Y','.'],['Y','.','.']],
               [['X','X'],['X','Y']],
               [['.','.'],['.','.']],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.numberOfSubmatrices(grid)
    print(f'r = {r}')
    print('===============================')











