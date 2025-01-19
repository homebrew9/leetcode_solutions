from typing import List
from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # Let's try BFS to solve this problem
        rows = len(grid)
        cols = len(grid[0])
        start_row, start_col = None, None
        for r in range(rows):
            found = False
            for c in range(cols):
                if grid[r][c] == '*':
                    start_row, start_col = r, c
                    found = True
                    break
            if found:
                break
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        steps = 0
        dq = deque()
        seen = set()
        dq.append((start_row, start_col))
        seen.add((start_row, start_col))
        while dq:
            size = len(dq)
            for _ in range(size):
                r, c = dq.popleft()
                if grid[r][c] == '#':
                    return steps
                for dr, dc in directions:
                    rnew, cnew = r + dr, c + dc
                    if 0 <= rnew < rows and 0 <= cnew < cols and grid[rnew][cnew] != 'X' and (rnew, cnew) not in seen:
                        seen.add((rnew, cnew))
                        dq.append((rnew, cnew))
            steps += 1
        return -1

# Main section
for grid in [
               [['X','X','X','X','X','X'],['X','*','O','O','O','X'],['X','O','O','#','O','X'],['X','X','X','X','X','X']],
               [['X','X','X','X','X'],['X','*','X','O','X'],['X','O','X','#','X'],['X','X','X','X','X']],
               [['X','X','X','X','X','X','X','X'],['X','*','O','X','O','#','O','X'],['X','O','O','X','O','O','X','X'],['X','O','O','O','O','#','O','X'],['X','X','X','X','X','X','X','X']],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.getFood(grid)
    print(f'r = {r}')
    print('====================')


