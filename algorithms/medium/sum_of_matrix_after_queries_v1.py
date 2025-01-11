from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        N = len(queries)
        rset = set()
        cset = set()
        total = 0
        for i in range(N-1, -1, -1):
            typ, ind, val = queries[i]
            if typ == 0:
                if ind not in rset:
                    total += val * (n - len(cset))
                    rset.add(ind)
            elif typ == 1:
                if ind not in cset:
                    total += val * (n - len(rset))
                    cset.add(ind)
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
    print('=================')


