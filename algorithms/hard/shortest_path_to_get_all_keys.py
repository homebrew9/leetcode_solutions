from typing import List
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        rows = len(grid)
        cols = len(grid[0])
        start = (0,0)
        dq = deque()
        seen = set()
        dq.append(start)
        seen.add(start)
        steps = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                r, c = dq[0]
                for dr, dc in directions:
                    r1 = r + dr
                    c1 = c + dc
                    if 0 <= r1 < rows and 0 <= c1 < cols:
                        if (r1, c1) not in seen:
                            seen.add((r1, c1))
                            dq.append((r1, c1))
                dq.popleft()
            steps += 1
        return steps-1

# Main section
for grid in [
               ['...','...','...'],
               ['.....','.....','.....','.....','.....'],
               #['@.a..', '###.#', 'b.A.B'],
               #['@..aA', '..B#.', '....b'],
               #['@Aa'],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.shortestPathAllKeys(grid)
    print(f'r = {r}')
    print('=====================')


