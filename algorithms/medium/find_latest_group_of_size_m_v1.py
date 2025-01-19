#
# This is similar to Union Find. Check the UF solution, which might be more intuitive.
# In this solution, we are setting the length of 1-group at the range boundaries.
# The value inside the range might be outdated.
# ======================================
# Union Find Solution
# ======================================
#
from typing import List

class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        return True

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        n, ans = len(arr), -1
        uf = UnionFindSet(n)
        for step, i in enumerate(arr):
            print(f'step, i = {step}, {i}')
            i -= 1
            uf.ranks[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if uf.ranks[uf.find(j)] == m:
                        ans = step
                    if uf.ranks[j]:
                        uf.union(i, j)
            print(f'\tuf.parents = {uf.parents}')
            print(f'\tuf.ranks   = {uf.ranks}')
        return ans

# Main section
for arr, m in [
                 ([3,5,1,2,4], 1),
                 ([3,1,5,4,2], 2),
                 ([2,1], 2),
                 ([1], 1),
              ]:
    print(f'arr, m = {arr}, {m}')
    sol = Solution()
    r = sol.findLatestStep(arr, m)
    print(f'r = {r}')
    print('======================')


