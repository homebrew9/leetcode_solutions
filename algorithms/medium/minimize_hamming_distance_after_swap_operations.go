from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.fa[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

class Solution:
    def minimumHammingDistance(
        self,
        source: List[int],
        target: List[int],
        allowedSwaps: List[List[int]],
    ) -> int:
        n = len(source)
        uf = UnionFind(n)
        for a, b in allowedSwaps:
            uf.union(a, b)

        sets = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            f = uf.find(i)
            sets[f][source[i]] += 1

        ans = 0
        for i in range(n):
            f = uf.find(i)
            if sets[f][target[i]] > 0:
                sets[f][target[i]] -= 1
            else:
                ans += 1
        return ans

# Main section
for source, target, allowedSwaps in [
                                       ([1,2,3,4], [2,1,4,5], [[0,1],[2,3]]),
                                       ([1,2,3,4], [1,3,2,4], []),
                                       ([5,1,2,4,3], [1,5,4,2,3], [[0,4],[4,2],[1,3],[1,4]]),
                                       ([2,3,1], [1,2,2], [[0,2],[1,2]]),
                                    ]:
    print(f'source, target, allowedSwaps = {source}, {target}, {allowedSwaps}')
    sol = Solution()
    r = sol.minimumHammingDistance(source, target, allowedSwaps)
    print(f'r = {r}')
    print('==================================')


















