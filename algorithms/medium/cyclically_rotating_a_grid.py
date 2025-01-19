from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def get_layer(r1, c1, r2, c2):
            arr = list()
            for c in range(c1, c2 + 1):
                arr += [grid[r1][c]]
            for r in range(r1 + 1, r2 + 1):
                arr += [grid[r][c2]]
            for c in range(c2 - 1, c1 - 1, -1):
                arr += [grid[r2][c]]
            for r in range(r2 - 1, r1, -1):
                arr += [grid[r][c1]]
            #print(f'\tr1, c1 = ({r1}, {c1}) ; r2, c2 = ({r2}, {c2})')
            return arr
        def set_layer(r1, c1, r2, c2, arr):
            i = 0
            for c in range(c1, c2 + 1):
                grid[r1][c] = arr[i]
                i += 1
            for r in range(r1 + 1, r2 + 1):
                grid[r][c2] = arr[i]
                i += 1
            for c in range(c2 - 1, c1 - 1, -1):
                grid[r2][c] = arr[i]
                i += 1
            for r in range(r2 - 1, r1, -1):
                grid[r][c1] = arr[i]
                i += 1
        rows = len(grid)
        cols = len(grid[0])
        r1, c1 = 0, 0
        r2, c2 = rows - 1, cols - 1
        layer_rows, layer_cols = rows, cols
        while True:
            if layer_rows > 0 and layer_cols > 0:
                arr = get_layer(r1, c1, r2, c2)
                #print(arr)
                shift = k % len(arr)
                arr = arr[shift:] + arr[:shift]
                set_layer(r1, c1, r2, c2, arr)
                r1, c1 = r1 + 1, c1 + 1
                r2, c2 = r2 - 1, c2 - 1
                layer_rows -= 2
                layer_cols -= 2
            else:
                break
        return grid

# Main section
for grid, k in [
                  ([[40,10],[30,20]], 1),
                  ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2),
                  ([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36],[37,38,39,40,41,42],[43,44,45,46,47,48]], 1),
                  ([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36],[37,38,39,40,41,42],[43,44,45,46,47,48]], 12345678),
               ]:
    print(f'grid, k = {grid}, {k}')
    sol = Solution()
    r = sol.rotateGrid(grid, k)
    print(f'r = {r}')
    print('=================')


