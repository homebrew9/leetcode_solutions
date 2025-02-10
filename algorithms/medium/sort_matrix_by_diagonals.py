from typing import List
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        def get_array(row, col):
            arr = list()
            r, c = row, col
            while r < N:
                while c < N:
                    arr.append(grid[r][c])
                    c += 1
                    break
                r += 1
            return arr
        def set_array(row, col, arr):
            r, c = row, col
            i = 0
            while r < N:
                while c < N:
                    grid[r][c] = arr[i]
                    i += 1
                    c += 1
                    break
                r += 1
        N = len(grid)
        for r in range(N):
            arr = get_array(r, 0)
            arr.sort(reverse=True)
            set_array(r, 0, arr)
        for c in range(1, N):
            arr = get_array(0, c)
            arr.sort()
            set_array(0, c, arr)
        return grid

# Main section
for grid in [
               [[1,7,3],[9,8,2],[4,5,6]],
               [[0,1],[1,2]],
               [[1]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.sortMatrix(grid)
    print(f'r = {r}')
    print('=====================')

