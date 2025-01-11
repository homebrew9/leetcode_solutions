from typing import List
from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for node1, node2, cost in roads:
            graph[node1][node2] = graph[node2][node1] = cost
        #print(f'\tgraph = {graph}')

        res = float('inf')
        vis = set()
        dq = deque([1])
        while dq:
            #print('============================')
            #print(f'\t\tdq, vis, res = {dq}, {vis}, {res}')
            node = dq.popleft()
            #print(f'\t\tafter popleft, dq = {dq}')
            for adj, scr in graph[node].items():
                #print(f'\t\t\tadj = {adj}')
                if adj not in vis:
                    #print(f'\t\t\t\tadj: {adj} is not in vis: {vis}')
                    dq.append(adj)
                    vis.add(adj)
                #print(f'\t\t\tres = min(res, scr) = min({res},{scr}) = {min(res, scr)}\n')
                res = min(res, scr)
        return res

# Main section
for n, roads in [
                   (4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]),
                   (4, [[1,2,2],[1,3,4],[3,4,7]]),
                ]:
    print(f'n, roads = {n}, {roads}')
    sol = Solution()
    r = sol.minScore(n, roads)
    print(f'r = {r}')
    print('==============')

