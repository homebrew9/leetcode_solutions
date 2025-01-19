# 
# Notice how this implementation of Dijkstra's algorithm uses a separate 2D grid instead of
# a set to avoid retracing its step!
#
from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra's Algorithm
        rows = len(heights)
        cols = len(heights[0])
        grid = [[None for _ in range(cols)] for _ in range(rows)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        # Each element of min heap is of form: (dist, row, col)
        h = [(0,0,0)]
        heapq.heapify(h)
        grid[0][0] = 0
        while h:
            dist, row, col = heapq.heappop(h)
            for dr, dc in directions:
                rnew = row + dr
                cnew = col + dc
                if 0 <= rnew < rows and 0 <= cnew < cols:
                    dnew = max(dist, abs(heights[rnew][cnew] - heights[row][col]))
                    if grid[rnew][cnew] is None or dnew < grid[rnew][cnew]:
                        grid[rnew][cnew] = dnew
                    else:
                        continue
                    heapq.heappush(h, (dnew, rnew, cnew))
        return grid[rows-1][cols-1]

# Main section
for heights in [
                  [[1,2,2],[3,8,2],[5,3,5]],
                  [[1,2,3],[3,8,4],[5,3,5]],
                  [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
               ]:
    print(f'heights = {heights}')
    sol = Solution()
    r = sol.minimumEffortPath(heights)
    print(f'r = {r}')
    print('======================')


