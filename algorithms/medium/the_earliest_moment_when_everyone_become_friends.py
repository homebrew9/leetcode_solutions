from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort()
        for ts, a, b in logs:
            uf.union(a, b)
            if uf.count == 1:
                return ts
        return -1

class UnionFind:
    # Path compression + Union Find by ranking
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.count = n
    def find(self, x):
        if x == self.root[x]:
            return x
        val = self.find(self.root[x])
        self.root[x] = val
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # If chain lengths (ranks) are different, then attach the shorter chain to
            # the longer chain. Otherwise, just pick one root and update rank.
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

# Main section
for logs, n in [
                  ([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6),
                  ([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4),
                  ([[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]], 4),
               ]:
    print(f'logs, n = {logs}, {n}')
    sol = Solution()
    r = sol.earliestAcq(logs, n)
    print(f'r = {r}')
    print('=====================')





































