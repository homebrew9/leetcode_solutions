#
# Doesn't work. Looks like it will not work if we go from index 0 to N-1.
# We will have to travel in reverse, from N-1 to 0. See version 1.
#
from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        hrow = dict()
        hcol = dict()
        total = 0
        for typ, idx, val in queries:
            print(f'\tStart: typ, idx, val, total = {typ}, {idx}, {val}, {total}')
            if typ == 0:
                if idx in hrow:
                    total -= hrow[idx] * n
                    hrow[idx] = val
                    total += val * n
                else:
                    hrow[idx] = val
                    total += val * n - sum(hcol.values())
            elif typ == 1:
                if idx in hcol:
                    total -= hcol[idx] * n
                    hcol[idx] = val
                    total += val * n
                else:
                    hcol[idx] = val
                    total += val * n - sum(hrow.values())
            print(f'\tEnd  : typ, idx, val, total = {typ}, {idx}, {val}, {total}')
            print('=====')
        return total
    def matrixSumQueries1(self, n: int, queries: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        total = 0
        for typ, idx, val in queries:
            print(f'\tStart: typ, idx, val, total = {typ}, {idx}, {val}, {total}')
            if typ == 0:
                for c in range(n):
                    grid[idx][c] = val
            elif typ == 1:
                for r in range(n):
                    grid[r][idx] = val
            total = 0
            for r in range(n):
                for c in range(n):
                    total += grid[r][c]
            print(f'\tgrid = {grid}')
            print(f'\tEnd  : typ, idx, val, total = {typ}, {idx}, {val}, {total}')
            print('=====')
        return total

# Main section
for n, queries in [
                     (3, [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]),
                     (3, [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]),
                     (8, [[0,6,30094],[0,7,99382],[1,2,18599],[1,3,49292],[1,0,81549],[1,1,38280],[0,0,19405],[0,4,30065],[1,4,60826],[1,5,9241],[0,5,33729],[0,1,41456],[0,2,62692],[0,3,30807],[1,7,70613],[1,6,9506],[0,5,39344],[1,0,44658],[1,1,56485],[1,2,48112],[0,6,43384]]),
                     (3, [[0,2,1],[0,2,2],[0,2,3]]),
                     (3, [[1,2,1],[1,2,2],[1,2,3]]),
                  ]:
    print(f'n, queries = {n}, {queries}')
    sol = Solution()
    r = sol.matrixSumQueries(n, queries)
    print(f'r = {r}')
    print('~~~~~~~~~~')
    r1 = sol.matrixSumQueries1(n, queries)
    print(f'r1 = {r1}')
    print('=================')


