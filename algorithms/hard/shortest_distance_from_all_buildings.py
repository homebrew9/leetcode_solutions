from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dq = deque()
        seen = defaultdict(dict)
        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total += 1
                    dq.append(((r,c),(r,c),0))  # (root_node, curr_node, distance_from_root_to_curr)
                    seen[(r,c)] = {(r,c): 0}    # seen[curr] = {root1: dist1, root2: dist2, ...}
        found = False
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while dq:
            size = len(dq)
            for _ in range(size):
                root, curr, dist = dq.popleft()
                for dr, dc in directions:
                    r1 = curr[0] + dr
                    c1 = curr[1] + dc
                    if 0 <= r1 < rows and 0 <= c1 < cols and grid[r1][c1] == 0:
                        if (r1, c1) in seen:
                            if root not in seen[(r1, c1)]:
                                seen[(r1, c1)][root] = dist + 1
                                dq.append((root, (r1, c1), dist + 1))
                        else:
                            seen[(r1, c1)] = {root: dist + 1}
                            dq.append((root, (r1, c1), dist + 1))
        res = float('inf')
        for k, v in seen.items():
            if len(v) == total and grid[k[0]][k[1]] == 0:
                res = min(res, sum(seen[k].values()))
        return -1 if res == float('inf') else res

# Main section
for grid in [
               [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]],
               [[1,0]],
               [[1]],
               [[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]],
            ]:
    print(f'grid = {grid}')
    sol = Solution()
    r = sol.shortestDistance(grid)
    print(f'r = {r}')
    print('========================')

