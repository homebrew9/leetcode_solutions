from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            for next_node in hsh[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    dfs(next_node)
        hsh = defaultdict(list)
        for u, v in edges:
            hsh[u] += [v]
            hsh[v] += [u]
        cc_set = set()
        for node in range(n):
            seen = set()
            seen.add(node)
            dfs(node)
            cc_set.add(tuple(sorted(seen)))
        # Now the cc_set has tuples representing connected components. We
        # iterate through each connected component and check if each node
        # has (N - 1) connections, where N = size of connected component.
        res = 0
        for cc in cc_set:
            N = len(cc)
            valid = True
            for node in cc:
                if len(hsh[node]) != N - 1:
                    valid = False
                    break
            if valid:
                res += 1
        return res

# Main section
for n, edges in [
                   (6, [[0,1],[0,2],[1,2],[3,4]]),
                   (6, [[0,1],[0,2],[1,2],[3,4],[3,5]]),
                ]:
    print(f'n, edges = {n}, {edges}')
    sol = Solution()
    r = sol.countCompleteComponents(n, edges)
    print(f'r = {r}')
    print('===================')

