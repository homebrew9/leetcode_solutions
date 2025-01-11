#
# Slightly different way of using DFS to solve this problem
# (we start with empty list here). Also note the termination
# condition: (node not in hsh) returns incorrect result for the last graph.
#
from typing import List
from collections import defaultdict

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, arr):
            #if node not in hsh:
            if node == len(graph) - 1:
                arr += [node]
                self.res.append(arr)
                return
            for child in hsh[node]:
                dfs(child, arr + [node])

        hsh = defaultdict(list)
        for i, v in enumerate(graph):
            if len(v) > 0:
                hsh[i] += v
        self.res = list()
        dfs(0, [])
        return self.res

# Main section
for graph in [
                [[1,2],[3],[3],[]],
                [[4,3,1],[3,2,4],[3],[4],[]],
                [[1,5],[2],[3],[],[3],[4]],
             ]:
    print(f'graph = {graph}')
    sol = Solution()
    r = sol.allPathsSourceTarget(graph)
    print(f'r = {r}')
    print('====================')


