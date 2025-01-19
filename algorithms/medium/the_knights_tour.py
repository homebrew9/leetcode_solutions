from typing import List

class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        # Classic backtracking
        def solve(r, c, i):
            grid[r][c] = i
            if i == m * n - 1:
                return True
            for dr, dc in directions:
                rnew = r + dr
                cnew = c + dc
                res = True
                tries = 0
                if 0 <= rnew < m and 0 <= cnew < n and grid[rnew][cnew] == -1:
                    tries += 1
                    res = solve(rnew, cnew, i+1)
                    if res is True:
                        break
            if tries == 0 or res is False:
                grid[r][c] = -1
                return False
            return True
        grid = [[-1 for _ in range(n)] for _ in range(m)]
        directions = [(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1)]
        solve(r, c, 0)
        #print(grid)
        return grid

# Main section
for m, n, r, c in [
                     (1, 1, 0, 0),
                     (3, 4, 0, 0),
                     (5, 5, 0, 0),
                     (5, 5, 2, 2),
                  ]:
    print(f'm, n, r, c = {m}, {n}, {r}, {c}')
    sol = Solution()
    r = sol.tourOfKnight(m, n, r, c)
    print(f'r = {r}')
    print('==================')


