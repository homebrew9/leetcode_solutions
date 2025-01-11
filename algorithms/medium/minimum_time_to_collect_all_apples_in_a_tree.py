from typing import List
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        e = defaultdict(list)
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
        print(f'\te = {e}')

        # Return two things:
        # 1) whether there is a child in this path with apple, and
        # 2) sum of costs
        def dfs(node, parent):
            if len(e[node]) == 0:
                return False, 0
            total = 0
            for child in e[node]:
                if child != parent:
                    r, c = dfs(child, node)
                    if r:
                        total += c
            if total > 0 or hasApple[node]:
                return True, total + 2
            else:
                return False, 0

        r, c = dfs(0, -1)
        if r:
            return c - 2
        return 0

# Main section
for n, edges, hasApple in [
                             (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]),
                             #(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False]),
                             #(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False]),
                          ]:
    print(f'n, edges, hasApple = {n}, {edges}, {hasApple}')
    sol = Solution()
    r = sol.minTime(n, edges, hasApple)
    print(f'r = {r}')
    print('==========================')

