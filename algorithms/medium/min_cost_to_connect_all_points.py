from collections import defaultdict
from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm without heap bloat.
        N = len(points)
        min_dist = [float('inf')] * N
        visited = [False] * N
        total_cost = 0
        h = []
        
        min_dist[0] = 0
        heapq.heappush(h, (0, 0))
        
        for _ in range(N):
            while True:
                d, u = heapq.heappop(h)
                if not visited[u]:
                    break
            visited[u] = True
            total_cost += d
            
            for v in range(N):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist  # ←← Critical update!
                        heapq.heappush(h, (dist, v))
        return total_cost

    def minCostConnectPoints_1(self, points: List[List[int]]) -> int:
        # Use Kruskal's algorithm to determine Minimum Spanning Tree.
        # Edges are the lines between two points, and weights are
        # the Manhattan Distances.
        N = len(points)
        edges = list()
        for i in range(N):
            for j in range(i + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                edges.append((x1, y1, x2, y2, dist))
        edges.sort(key=lambda x: x[4])
        res = 0
        uf = UnionFind(points)
        for x1, y1, x2, y2, dist in edges:
            if not uf.are_connected(x1, y1, x2, y2):
                res += dist
                uf.union(x1, y1, x2, y2)
        return res

class UnionFind:
    def __init__(self, points):
        self.hsh = defaultdict(tuple)
        for x, y in points:
            self.hsh[(x, y)] = (x, y)
    def find(self, x, y):
        if self.hsh[(x, y)] != (x, y):
            x1, y1 = self.hsh[(x, y)]
            self.hsh[(x, y)] = self.find(x1, y1)
        return self.hsh[(x, y)]
    def union(self, x1, y1, x2, y2):
        ax1, ay1 = self.find(x1, y1)
        bx1, by1 = self.find(x2, y2)
        if (ax1, ay1) != (bx1, by1):
            self.hsh[(ax1, ay1)] = (bx1, by1)
    def are_connected(self, x1, y1, x2, y2):
        return self.find(x1, y1) == self.find(x2, y2)

# Main section
for points in [
                 [[0,0],[2,2],[3,10],[5,2],[7,0]],
                 [[3,12],[-2,5],[-4,1]],
                 [[-18,-21],[47,87],[47,89],[-95,18],[-63,74],[-26,22],[19,56],[-51,-39],[-8,-9],[-74,40]],
                 [[-51,-97],[-97,39],[-28,88],[-85,12],[-1,-30],[-99,-79],[67,-19],[-72,53],[-24,-55],[60,-93],[-10,38],[-80,-38],[-69,-4],[4,-55],[98,12]],
              ]:
    print(f'points = {points}')
    sol = Solution()
    r = sol.minCostConnectPoints(points)
    r1 = sol.minCostConnectPoints_1(points)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===========================')






