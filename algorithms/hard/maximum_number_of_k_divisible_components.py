#
# DFS solution. This can be solved by using BFS and Topological Sort as well.
#
from typing import List
from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node, parent):
            sum = 0
            for next_node in self.hsh[node]:
                if next_node != parent:
                    ret = dfs(next_node, node)
                    sum = (ret + sum) % k
            sum = (values[node] + sum) % k
            if sum == 0:
                self.component_count += 1
            return sum
        self.component_count = 0
        self.hsh = defaultdict(list)
        for u, v in edges:
            self.hsh[u] += [v]
            self.hsh[v] += [u]
        dfs(0, -1)
        return self.component_count

# Main section
for n, edges, values, k in [
                              (5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6),
                              (7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3),
                              (1, [], [0], 1),
                           ]:
    print(f'n, edges, values, k = {n}, {edges}, {values}, {k}')
    sol = Solution()
    r = sol.maxKDivisibleComponents(n, edges, values, k)
    print(f'r = {r}')
    print('===================')


