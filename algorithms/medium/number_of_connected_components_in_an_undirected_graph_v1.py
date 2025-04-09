from typing import List
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Besides Union-Find, we can solve this problem using DFS
        def dfs(node):
            for next_node in hsh[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    dfs(next_node)
        hsh = defaultdict(list)
        for u, v in edges:
            hsh[u] += [v]
            hsh[v] += [u]
        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
            dfs(i)
        return res

# Main section
for n, edges in [
                   (5, [[0,1],[1,2],[3,4]]),
                   (5, [[0,1],[1,2],[2,3],[3,4]]),
                   (3, [[2,1],[1,0]]),
                   (4, [[2,3],[1,2],[1,3]]),
                   (3, [[2,1],[1,0],[0,2]]),
                ]:
    print(f'n, edges = {n}, {edges}')
    sol = Solution()
    r = sol.countComponents(n, edges)
    print(f'r = {r}')
    print('========================')

