from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        # Dijkstra's algorithm
        marked_set = set(marked)
        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))
        best = [float('inf')] * n
        done = [False] * n
        h = list()
        best[s] = 0
        heapq.heappush(h, (0, s))   # (distance, node)
        while len(h) > 0:
            d, node = heapq.heappop(h)
            if node in marked_set:
                return d
            if done[node]:
                continue
            done[node] = True
            for v, w in adj_list[node]:
                if best[v] > d + w:
                    best[v] = d + w
                    heapq.heappush(h, (best[v], v))
        return -1

# Main section
for n, edges, s, marked in [
                              (4, [[0,1,1],[1,2,3],[2,3,2],[0,3,4]], 0, [2,3]),
                              (5, [[0,1,2],[0,2,4],[1,3,1],[2,3,3],[3,4,2]], 1, [0,4]),
                              (4, [[0,1,1],[1,2,3],[2,3,2]], 3, [0,1]),
                              (3, [[1,2,5],[0,2,6],[0,1,1],[0,2,4],[0,2,8],[2,1,8],[0,2,1]], 2, [0]),
                              (2, [[0,1,3],[0,1,3],[0,1,7],[1,0,4],[0,1,2],[1,0,1],[1,0,8],[1,0,4],[1,0,10],[1,0,10],[1,0,9]], 0, [1]),
                           ]:
    print(f'n, edges, s, marked = {n}, {edges}, {s}, {marked}')
    sol = Solution()
    r = sol.minimumDistance(n, edges, s, marked)
    print(f'r = {r}')
    print('========================')

