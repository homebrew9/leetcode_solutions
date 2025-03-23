from typing import List
from collections import defaultdict
from heapq import heapify, heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((w, v))
            adj[v].append((w, u))
        MOD = 10**9 + 7
        min_heap = [(0, 0)] # (cost, node)
        heapify(min_heap)
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        path_count = [0] * n
        path_count[0] = 1
        while min_heap:
            cost, node = heappop(min_heap)
            for nei_cost, nei in adj[node]:
                if cost + nei_cost < min_cost[nei]:
                    min_cost[nei] = cost + nei_cost
                    path_count[nei] = path_count[node]
                    heappush(min_heap, (cost + nei_cost, nei))
                elif cost + nei_cost == min_cost[nei]:
                    path_count[nei] = (path_count[nei] + path_count[node]) % MOD
        return path_count[n-1]

# Main section
for n, roads in [
                   (7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]),
                   (2, [[1,0,10]]),
                   (6, [[0,1,1],[0,5,6],[0,4,3],[0,2,9],[1,3,2],[2,4,10],[3,5,3],[4,5,3]]),
                ]:
    print(f'n, roads = {n}, {roads}')
    sol = Solution()
    r = sol.countPaths(n, roads)
    print(f'r = {r}')
    print('===================')

