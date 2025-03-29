from typing import List
from heapq import heappush, heappop

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()
        min_heap = [(grid[0][0], 0, 0)] # val, r, c
        visit = set([(0, 0)])
        res = [0] * len(queries)
        points = 0
        for limit, index in q:
            while min_heap and min_heap[0][0] < limit:
                val, r, c = heappop(min_heap)
                points += 1
                neighbors = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
                for nr, nc in neighbors:
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit):
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        visit.add((nr, nc))
            res[index] = points
        return res

# Main section
for grid, queries in [
                        ([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]),
                        ([[5,2,1],[1,1,2]], [3]),
                        ([[15,15,19,16,13],[6,5,10,6,1],[14,19,14,19,11],[1,10,15,20,11],[19,7,9,16,2]], [44,47,29,41,19,40,39,25,45,60]),
                     ]:
    print(f'grid, queries = {grid}, {queries}')
    sol = Solution()
    r = sol.maxPoints(grid, queries)
    print(f'r = {r}')
    print('========================')

