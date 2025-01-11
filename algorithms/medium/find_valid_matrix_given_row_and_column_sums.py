from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        grid = [[0 for _ in range(cols)] for _ in range(rows)]
        r, c = 0, 0
        while r < rows and c < cols:
            min_val = min(rowSum[r], colSum[c])
            grid[r][c] = min_val
            rowSum[r] -= min_val
            colSum[c] -= min_val
            if rowSum[r] == 0:
                r += 1
            if colSum[c] == 0:
                c += 1
        return grid

# Main section
for rowSum, colSum in [
                         ([3,8], [4,7]),
                         ([5,7,10], [8,6,8]),
                         ([6,15,24], [12,15,18]),
                         ([7,0,0], [0,0,7]),
                      ]:
    print(f'rowSum, colSum = {rowSum}, {colSum}')
    sol = Solution()
    r = sol.restoreMatrix(rowSum, colSum)
    print(f'r = {r}')
    print('=================')

