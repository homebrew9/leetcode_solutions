#
# Good challenging problem. Make sure the concept of "wait time" or "delay time" is
# understood properly. Once that is accounted for, the rest is standard Dijkstra.
#

from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # Early exit if the second cell is unreachable
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        directions = [(1,0), (-1,0), (0,1), (0,-1)]  # Possible moves
        rows, cols = len(grid), len(grid[0])
        time_map = [[float('inf') for _ in range(cols)] for _ in range(rows)]  # Track minimum time to each cell
        pq = [(0,0,0)]  # Min-heap for (time, row, col)
        heapq.heapify(pq)

        while pq:
            time, row, col = heapq.heappop(pq)
            # Return the time if we've reached the bottom-right corner
            if (row, col) == (rows - 1, cols - 1):
                return time
            # Skip if a better (lower) time already exists for this cell
            if time > time_map[row][col]:
                continue
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Calculate the earliest valid time to enter the neighbor cell
                    # If the difference is odd, then wait time = 0 because we can do
                    # back-and-forth between the current and previous cells for 2n time
                    # and then jump to target cell in 2n+1 time.
                    wait_time = 0 if (grid[nr][nc] - time) % 2 == 1 else 1
                    next_time = max(grid[nr][nc] + wait_time, time + 1)
                    # Update time if this path is faster (i.e. time is lower)
                    if next_time < time_map[nr][nc]:
                        heapq.heappush(pq, (next_time, nr, nc))
                        time_map[nr][nc] = next_time

# Main section
for grid in [
               [[0,1,3,2],[5,1,2,5],[4,3,8,6]],
               [[0,2,4],[3,2,1],[1,0,4]],
               [[0,1,2,7,1,10,6,1,5,4],[5,8,1,7,10,2,4,7,4,1],[7,5,5,8,6,4,2,1,8,6],[9,8,1,9,9,3,1,2,5,8],[6,8,6,9,5,2,10,4,10,5],[6,1,2,2,9,2,10,1,3,7],[7,5,9,5,9,9,7,9,8,5],[8,9,7,10,8,4,9,3,5,10],[3,5,1,6,9,2,3,4,8,7],[8,9,9,1,7,10,2,10,10,3]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.minimumTime(grid)
    print(f'r = {r}')
    print('====================')


