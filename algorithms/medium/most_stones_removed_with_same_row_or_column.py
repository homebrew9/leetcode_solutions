from typing import List
from collections import defaultdict
from itertools import chain

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # All stones with the same row and same column belong
        # to the same connected component. We store this data first.
        rows = defaultdict(list)
        cols = defaultdict(list)
        for s, (r, c) in enumerate(stones):
            rows[r].append(s)
            cols[c].append(s)
        seen = set()
        n = len(stones)
        
        # The dfs function explores a connected component of each
        # stone by making recursive calls to adjacent stones. It
        # returns 1 or 0 depending on whether the component was
        # already explored, thus allowing them to be counted.
        def dfs(s):
            if s in seen:
                return 0
            seen.add(s)
            r, c = stones[s]
            for ss in chain(rows[r], cols[c]):
                dfs(ss)
            return 1
        
        # Count the number of connected components
        cnt = 0
        for s in range(n):
            cnt += dfs(s)
        
        # In each component, one stone remains
        return (n - cnt)

# Main section
for stones in [
                 [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]],
                 [[0,0],[0,2],[1,1],[2,0],[2,2]],
                 [[0,0]],
                 [[0,0],[1,0],[0,1]],
                 [[0,0],[1,1]],
                 [[0,0],[1,1],[1,0]],
              ]:
    print(f'stones = {stones}')
    sol = Solution()
    r = sol.removeStones(stones)
    print(f'r = {r}')
    print('====================')

