from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def set_value(r, c):
            min_val = float('inf')
            for dr, dc in directions:
                rnew = r + dr
                cnew = c + dc
                if 0 <= rnew < rows and 0 <= cnew < cols and isWater[rnew][cnew] is not None:
                    min_val = min(min_val, isWater[rnew][cnew])
            if min_val == float('inf'):
                return 1
            else:
                return min_val + 1
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        rows = len(isWater)
        cols = len(isWater[0])
        water_cells = list()
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    water_cells.append((r, c))
                else:
                    isWater[r][c] = None
        # Set the height of all cells around water_cells to 1
        water_cells_set = set(water_cells)
        for r, c in water_cells:
            isWater[r][c] = 0
            for dr, dc in directions:
                rnew = r + dr
                cnew = c + dc
                if 0 <= rnew < rows and 0 <= cnew < cols and (rnew, cnew) not in water_cells_set:
                    isWater[rnew][cnew] = 1
        #print(isWater)
        # Now reset the remaining columns. We start from any water cell
        # and use BFS to reset the values for all remaining columns. For a
        # cell with None value, we check all 4-directions and set its value.
        dq = deque()
        seen = set()
        for cell in water_cells:
            dq.append(cell)
            seen.add(cell)
        while dq:
            size = len(dq)
            for _ in range(size):
                r, c = dq.popleft()
                # Set the current cell's value if it is None
                if isWater[r][c] == None:
                    isWater[r][c] = set_value(r, c)
                # Add the surrounding cells in the deque
                for dr, dc in directions:
                    rnew = r + dr
                    cnew = c + dc
                    if 0 <= rnew < rows and 0 <= cnew < cols and (rnew, cnew) not in seen:
                        seen.add((rnew, cnew))
                        dq.append((rnew, cnew))
        return isWater

# Main section
for isWater in [
         [[0,1],[0,0]],
         [[0,0,1],[1,0,0],[0,0,0]],
         [[1,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]],
         [[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]],
         [[0,1,0,1,0],[1,1,1,0,1],[0,0,0,0,0],[0,1,1,0,1],[1,0,1,0,1]],
         [[0,1,1,1,0,0,0,0,0,1],[1,0,0,0,1,0,1,1,0,0],[1,1,1,0,0,0,0,0,1,1],[1,0,1,0,1,0,0,0,0,1],[1,0,0,1,0,1,1,1,0,1],[0,0,1,0,0,0,1,0,1,0],[0,1,1,1,1,0,1,1,0,1],[0,1,0,0,0,1,1,1,1,0],[1,0,1,1,1,0,0,0,0,1],[1,1,1,0,1,1,1,1,0,0]],
    ]:
    print(f'isWater = {isWater}')
    sol = Solution()
    r = sol.highestPeak(isWater)
    print(f'r = {r}')
    print('======================')


