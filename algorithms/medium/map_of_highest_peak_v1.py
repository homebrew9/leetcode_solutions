from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # We an use BFS to assign the heights. One small change - we store the
        # current height in the deque itself, along with the cell location.
        rows = len(isWater)
        cols = len(isWater[0])
        height = [[None for _ in range(cols)] for _ in range(rows)]
        dq = deque()
        seen = set()
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    dq.append((r, c, 0))
                    seen.add((r, c))
                    height[r][c] = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while dq:
            size = len(dq)
            for _ in range(size):
                r, c, h = dq.popleft()
                for dr, dc in directions:
                    rnew = r + dr
                    cnew = c + dc
                    if 0 <= rnew < rows and 0 <= cnew < cols and height[rnew][cnew] is None:
                        dq.append((rnew, cnew, h + 1))
                        seen.add((rnew, cnew))
                        height[rnew][cnew] = h + 1
        return height

# Main section
for isWater in [
         [[0,1],[0,0]],
         [[0,0,1],[1,0,0],[0,0,0]],
         [[1,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]],
         [[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]],
         [[0,1,0,1,0],[1,1,1,0,1],[0,0,0,0,0],[0,1,1,0,1],[1,0,1,0,1]],
         [[0,1,1,1,0,0,0,0,0,1],[1,0,0,0,1,0,1,1,0,0],[1,1,1,0,0,0,0,0,1,1],[1,0,1,0,1,0,0,0,0,1],[1,0,0,1,0,1,1,1,0,1],[0,0,1,0,0,0,1,0,1,0],[0,1,1,1,1,0,1,1,0,1],[0,1,0,0,0,1,1,1,1,0],[1,0,1,1,1,0,0,0,0,1],[1,1,1,0,1,1,1,1,0,0]],
         [[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]],
    ]:
    print(f'isWater = {isWater}')
    sol = Solution()
    r = sol.highestPeak(isWater)
    print(f'r = {r}')
    print('======================')


