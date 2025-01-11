from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        rowData, colData = [], []
        for r in range(rows):
            rowData += [[grid[r].count(0), grid[r].count(1)]]
        #print(f'{rowData}')
        for c in range(cols):
            zeroCount, oneCount = 0, 0
            for r in range(rows):
                if grid[r][c] == 0:
                    zeroCount += 1
                else:
                    oneCount += 1
            colData += [[zeroCount, oneCount]]
        #print(f'{colData}')
        mat = [[None for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                mat[r][c] = rowData[r][1] + colData[c][1] - rowData[r][0] - colData[c][0]
        return mat

# Main section
for grid in [
               [[0,1,1],[1,0,1],[0,0,1]],
               [[1,1,1],[1,1,1]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.onesMinusZeros(grid)
    print(f'r = {r}')
    print('======================')

