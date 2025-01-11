from typing import List
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            if i not in self.visited:
                return
            for x in self.hsh[i]:
                if x not in self.visited:
                    self.visited.add(x)
                    dfs(x)
        n = len(isConnected)
        self.hsh = defaultdict(list)
        for i, v in enumerate(isConnected):
            for j, w in enumerate(v):
                if i != j and w == 1:
                    self.hsh[i] += [j]
        print(f'\thsh = {self.hsh}')
        self.visited = set()
        res = 0
        for i in range(n):
            print(f'\ti, visited = {i}, {self.visited}')
            if i not in self.visited:
                self.visited.add(i)
                res += 1
                dfs(i)
        return res

# Main section
for isConnected in [
                      [[1,1,0],[1,1,0],[0,0,1]],
                      [[1,0,0],[0,1,0],[0,0,1]],
                      [[1,1,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,0,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,1]],
                      [[1,1,0,0,0],[1,1,0,1,0],[0,0,1,1,0],[0,1,1,1,0],[0,0,0,0,1]],
                   ]:
    print(f'isConnected = {isConnected}')
    sol = Solution()
    r = sol.findCircleNum(isConnected)
    print(f'r = {r}')
    print('================')

