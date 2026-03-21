from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        MAX = 10**20
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                kgrid = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        kgrid.append(grid[x][y])
                kmin = MAX
                kgrid.sort()
                for t in range(1, len(kgrid)):
                    if kgrid[t] == kgrid[t - 1]:
                        continue
                    kmin = min(kmin, kgrid[t] - kgrid[t - 1])
                if kmin != MAX:
                    res[i][j] = kmin
        return res

# Main section
for grid, k in [
                  ([[1,8],[3,-2]], 2),
                  ([[3,-1]], 1),
                  ([[1,-2,3],[2,3,5]], 2),
               ]:
    print(f'grid, k = {grid}, {k}')
    sol = Solution()
    r = sol.minAbsDiff(grid, k)
    print(f'r = {r}')
    print('===============================')
















