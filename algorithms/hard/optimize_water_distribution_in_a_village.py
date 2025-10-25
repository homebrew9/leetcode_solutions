from typing import List

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Add a virtual node "0". Now create edges from 0 to node[i]
        # with the cost wells[i]. These are the "wells" edges. We are
        # given the "pipes" edges. Append these two and sort on cost
        # ascending. Then Union Find nodes, adding the costs until
        # all nodes are connected. The sum of costs is the answer.
        edges = list()
        for i, v in enumerate(wells):
            edges.append((0, i + 1, v))
        edges.extend([tuple(item) for item in pipes])
        edges.sort(key=lambda x: (x[2],x[0],x[1]))
        uf = UnionFind(n)
        res = 0
        for a, b, cost in edges:
            merged = uf.union(a, b)
            if merged:
                res += cost
            if uf.count == 1:
                #return res
                break
        return res

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n + 1))
        self.count = n + 1
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.count -= 1
            return True
        return False

# Main section
for n, wells, pipes in [
                          (3, [1,2,2], [[1,2,1],[2,3,1]]),
                          (2, [1,1], [[1,2,1],[1,2,2]]),
                       ]:
    print(f'n, wells, pipes = {n}, {wells}, {pipes}')
    sol = Solution()
    r = sol.minCostToSupplyWater(n, wells, pipes)
    print(f'r = {r}')
    print('=====================')


