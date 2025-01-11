#
# https://www.youtube.com/watch?v=_Lht168GV2M
# Programming Live with Larry
#
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Hamiltonian Path
        R = len(grid)
        C = len(grid[0])

        sx = sy = ex = ey = None
        empty = 0
        for x in range(R):
            for y in range(C):
                if grid[x][y] == 1:
                    sx, sy = x, y
                elif grid[x][y] == 2:
                    ex, ey = x, y
                if grid[x][y] != -1:
                    empty += 1

        seen = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def count(x, y, seen):
            if x == ex and y == ey:
                if len(seen) == empty:
                    return 1
                else:
                    return 0
            total = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != -1 and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    total += count(nx, ny, seen)
                    seen.remove((nx, ny))
            return total

        return count(sx, sy, set([(sx, sy)]))

# Main section
for grid in [
               [[1,0,0,0],[0,0,0,0],[0,0,2,-1]],
               [[1,0,0,0],[0,0,0,0],[0,0,0,2]],
               [[0,1],[2,0]],
               [[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,2,-1,0,0]],
               [[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,2,0,0,0]],
               [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,2]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.uniquePathsIII(grid)
    print(f'r = {r}')
    print('=================')

