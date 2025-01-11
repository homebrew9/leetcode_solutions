from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # [1] This check significantly improves runtime i.e. we
        # can use the path (0,0) -> (0,n-1) -> (m-1,n-1)
        if k >= m + n - 2:
            return m + n - 2

        # [2] We use a deque to store and update a BFS state that is
        # (steps done so far, x, y, obstacles we can destroy)
        # x = column, y = row
        dq = deque([(0,0,0,k)])

        # [3] We also keep track of visited cells
        seen = set()

        #print(f'\tdq = {dq}')
        while dq:
            #print(f'\tQ = {dq}')
            steps, x, y, k = dq.popleft()
            # [4] Successfully reached lower right corner
            if (x, y) == (n-1, m-1):
                return steps

            # [5] Scan all possible directions
            for dx, dy in [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]:
                #print(f'\t\t(dx, dy) = ({dx}, {dy})')
                # [6] Check boundaries and obstacles
                if 0 <= dx < n and 0 <= dy < m and k - grid[dy][dx] >= 0:
                    # [7] Make (and remember) a step
                    new = (dx, dy, k - grid[dy][dx])
                    #print(f'\t\t\tnew = {new}')
                    if not new in seen:
                        seen.add(new)
                        dq.append((steps+1,) + new)
            #print(f'\tseen = {seen}')
            #print(f'\tdq = {dq}')
        return -1

# Main section
for grid, k in [
                  ([[0,0,1],[0,0,0],[1,0,0]], 1),
                  ([[0,0,1],[0,0,0],[0,0,0],[1,0,0]], 1),
                  ([[0,0,1],[1,0,1],[0,1,1],[1,1,0]], 1),
                  ([[0,0,1],[1,0,1],[0,1,1],[1,1,0]], 2),
                  ([[0,0,0,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,0]], 1),
                  ([[0,0,0,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,0]], 2),
               ]:
    print(f'grid, k = {grid}, {k}')
    sol = Solution()
    r = sol.shortestPath(grid, k)
    print(f'r = {r}')
    print('================')

