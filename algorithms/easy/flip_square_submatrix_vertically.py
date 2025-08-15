from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        stack = list()
        for r in range(x, x + k):
            tmp = list()
            for c in range(y, y + k):
                tmp.append(grid[r][c])
            stack.append(tmp)
        for r in range(x, x + k):
            tmp = stack.pop()
            i = 0
            for c in range(y, y + k):
                grid[r][c] = tmp[i]
                i += 1
        return grid

# Main section
for grid, x, y, k in [
                        ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1, 0, 3),
                        ([[3,4,2,3],[2,3,4,2]], 0, 2, 2),
                     ]:
    print(f'grid, x, y, k = {grid}, {x}, {y}, {k}')
    sol = Solution()
    r = sol.reverseSubmatrix(grid, x, y, k)
    print(f'r = {r}')
    print('==============================')





